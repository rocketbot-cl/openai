import json
import os
import base64
import subprocess
from r_openai import OpenAI

class openaiObject():
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = self.create_client()

    def create_client(self):
        return OpenAI(
            api_key=self.api_key
        )
    
    def get_auth(self):
        '''
        Authenticate with OpenAI API
        '''
        self.client.models.list()
        print("Authentication successful")

    def get_completions(self, prompt, model, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop):
        '''
        Get text completions from OpenAI API
        '''
        
        response = self.client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=int(max_tokens),
            temperature=float(temperature),
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
        )
        
        result = response.choices[0].text
        
        return result
    
    def get_transcript(self, audio_file):
        '''
        Get text transcript from OpenAI API
        '''
        audio_ = open(audio_file, "rb")
        transcript = self.client.audio.transcriptions.create(model="whisper-1", file=audio_)
        print("Transcript: ", transcript)
        
        result = transcript.text.encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
        
        return result
    
    def get_audio_translations(self, audio_file):
        '''
        Get audio translations from OpenAI API
        '''
        audio_ = open(audio_file, "rb")
        translation = self.client.audio.translations.create(model="whisper-1", file=audio_)

        result = translation.text.encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
        
        return result
    
    def get_chat_completions(self, model, messages, temperature, n, stop, max_tokens, only_text=False, schema_dict=None):
        '''
        Get chat completions from OpenAI API
        '''
        import json

        kwargs = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "n":n,
            "stop": stop,
            "max_tokens": max_tokens
        }

        if schema_dict:
            schema = self.__parse_to_openai_schema__(schema_dict)
            kwargs["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "response",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": schema,
                        "required": list(schema.keys()),
                        "additionalProperties": False
                    }
                }
            }
            
        try:
            response = self.client.chat.completions.create(**kwargs)
        except Exception as e:
            if "'max_tokens' is not supported with this model" in str(e):
                kwargs.pop("max_tokens", None)
                kwargs["extra_body"] = {"max_completion_tokens": max_tokens}
                response = self.client.chat.completions.create(**kwargs)
            else:
                raise e

        if only_text:
            response = response.choices[0].message.content
        else:
            response = self.completion_response_to_json(response)
        
        return response
    
    def completion_response_to_json(self, response):
        '''
        Convert completion response to JSON
        '''
        return json.dumps(response, default=lambda o: o.__dict__, ensure_ascii=False)
    
    def encode_image(self, image_file):
        '''
        Encode image file to base64
        '''
        with open(image_file, "rb") as image:
            image = base64.b64encode(image.read()).decode("utf-8")
        
        return image
    
    def upload_file(self, file_path):
        '''
        Loads a File into OpenAI and returns it's file id.
        '''
        with open(file_path, "rb") as skill_file:
            uploaded_file = self.client.files.create(file=skill_file, purpose="user_data")
        return uploaded_file.id

    def update_vector_store(self, vector_store_id: str = "", name: str = "", file_ids: list = []):
        '''
        Crea o actualiza un Vector Store de forma 100% sincrónica.
        El método se bloquea hasta que OpenAI termine de indexar todos los archivos.
        Devuelve el ID del Vector Store listo para usar.
        '''
        if not vector_store_id:
            vector_store = self.client.beta.vector_stores.create(name=name)
            vector_store_id = vector_store.id
            response = {"vector_store_id": vector_store_id}

        elif name:
            self.client.vector_stores.update(
                vector_store_id=vector_store_id,
                name=name
            )
            
        if file_ids:
            response_received = self.client.beta.vector_stores.file_batches.create_and_poll(
                vector_store_id=vector_store_id,
                file_ids=file_ids
            )

            response = response_received.model_dump_json()

        return response
        
    def list_openai_files(self, file_types = "file_id"):
        '''
        Lista todos los archivos almacenados en la nube de OpenAI.
        Devuelve una lista con los objetos de tipo File.
        '''

        if file_types == "file_id":
            files_list = self.client.files.list().data
        
        else:
            files_list = [vector_store for vector_store in self.client.beta.vector_stores.list(limit=100)]

        return files_list
        
    def delete_openai_file(self, file_id: str, file_type = "file_id"):
        '''
        Elimina un archivo específico de la nube de OpenAI utilizando su ID.
        Devuelve el estado de la eliminación.
        '''
        if file_type == "file_id":
            deletion_status = self.client.files.delete(file_id)
        else:
            deletion_status = self.client.beta.vector_stores.delete(file_id)
        return deletion_status
        
    def run_robot_with_historial(self, model: str = "", prompt = "", system_instructions= "", max_tokens = 1024, temperature = 1.0, conversation_id = "", file_ids = [], image_files = [], vector_store_ids = [],schema_dict=None):
        '''
        Comprime una carpeta en ZIP y la ejecuta con el Code Interpreter de OpenAI Assistants.
        ''' 

        user_message = {
            "role": "user",
            "content": [
                {"type": "input_text", "text": f"{prompt}"}
            ]
        }

        for image_file in image_files:
            image_file["type"] = "input_image"
            user_message["content"].append(
                image_file #{"file_id": image_file, "detail": "auto"}
            )

        for file_id in file_ids:
            user_message["content"].append(
                {"type": "input_file", "file_id": file_id}
            )
                    
        tools = []
        if vector_store_ids:
            tools.append({"type": "file_search", "vector_store_ids": vector_store_ids})

        if file_ids:
            tools.append({"type": "code_interpreter", "container": {"type": "auto"}})
        
        response_kwargs = {
        "instructions": system_instructions,
        "model": model,
        "input": [user_message],
        "temperature":temperature,
        "max_output_tokens": max_tokens,
        }

        if tools:
            response_kwargs["tools"] = tools

        if schema_dict:
            schema = self.__parse_to_openai_schema__(schema_dict)
            response_kwargs["text"] = {
                "format":{
                    "type": "json_schema",
                    "name": "response",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": schema,
                        "required": list(schema.keys()),
                        "additionalProperties": False
                    
                    }
                }
            }

        if not conversation_id:
            conversation = self.client.conversations.create()
            conversation_id = conversation.id

        response_kwargs["conversation"] = conversation_id


        response_obj = self.client.responses.create(**response_kwargs)

        response = {
            "conversation_id": conversation_id, 
            "output": response_obj.output_text

        }

        return json.dumps(response, ensure_ascii=False)
    
    def __parse_to_openai_schema__(self, schema_dict):

        properties = {}
        for key, value in schema_dict.items():
            if isinstance(value, dict):
                item_schema = self.__parse_to_openai_schema__(value)
                properties[key] = {
                    "type": "object",
                    "properties": item_schema,
                    "required": list(item_schema.keys()),
                    "additionalProperties": False
                }
                
            elif isinstance(value, list):
                if len(value) > 0:
                    first_item = value[0]
                    if isinstance(first_item, dict):
                        nested_props = self.__parse_to_openai_schema__(first_item)
                        item_schema = {
                            "type": "object",
                            "properties": nested_props,
                            "required": list(nested_props.keys()),
                            "additionalProperties": False
                        }
                    else:
                        item_schema = {"type": first_item.strip().lower()}
                else:
                    item_schema = {"type": "string"}
                    
                properties[key] = {
                    "type": "array",
                    "items": item_schema
                }
                
            else:
                mapped_type = value.strip().lower()
                properties[key] = {
                    "type": mapped_type
                }
        return properties
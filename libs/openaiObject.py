import json
import base64
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

        response = self.__make_request__(kwargs)

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

    def __make_request__(self, kwargs):
        try:
            response = self.client.chat.completions.create(**kwargs)
            return response
        
        except Exception as e:
            if "'max_tokens' is not supported with this model" in str(e):
                max_tokens =  kwargs.pop("max_tokens", None)
                kwargs["extra_body"] = {"max_completion_tokens": max_tokens}

            elif "Unsupported value: 'temperature' does not support" in str(e):
                kwargs["temperature"] = 1

            else:
                raise e
            
            return self.__make_request__(kwargs)
            
    
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
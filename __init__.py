# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

__author__ = "David Cuello <david@rocketbot.com> | Nicolas Garcia <nicolas.garcia@rocketbot.com>"
__version__ = "3.0.0"

try:
    import requests
    import os
    import sys
    import json
    import traceback

    base_path = tmp_global_obj["basepath"]
    cur_path = base_path + 'modules' + os.sep + 'OpenAI' + os.sep + 'libs' + os.sep
    import platform


    os_type = platform.system().lower()
    if os_type == "windows":
        cur_path_platform = os.path.join(cur_path, 'Windows', 'x64' if sys.maxsize > 2**32 else 'x86')
        if cur_path_platform not in sys.path:
            sys.path.append(cur_path_platform)
    
    elif os_type == "linux":
        cur_path_platform = os.path.join(cur_path, 'Linux')
        if cur_path_platform not in sys.path:
            sys.path.append(cur_path_platform)
    
    elif os_type == "darwin":
        cur_path_platform = os.path.join(cur_path, 'macos')
        if cur_path_platform not in sys.path:
            sys.path.append(cur_path_platform)
        try:
            from macos_mock_classes import load_mock_classes
            load_mock_classes()
        except Exception as e:
            PrintException()
            raise e
        
        
    import r_openai as openai 
    from openaiObject import openaiObject
    global mod_openai

    """
        Obtengo el modulo que fueron invocados
    """
    module = GetParams("module")

    class OpenAI_RB_old:
        def __init__(self, api_key):
            self.api_key = api_key
            self.get_auth()
            
        def get_auth(self):
            '''
            Authenticate with OpenAI API
            '''
            import r_openai as openai
            openai.api_key = self.api_key
            openai.Model.list()
            print("Authentication successful")

        def get_completions(self, prompt, model, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop):
            '''
            Get text completions from OpenAI API
            '''
            import r_openai as openai
            response = openai.Completion.create(
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
            import r_openai as openai
            audio_ = open(audio_file, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_)
            
            result = transcript["text"].encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
            
            return result
        
        def get_audio_translations(self, audio_file):
            '''
            Get audio translations from OpenAI API
            '''
            import r_openai as openai
            audio_ = open(audio_file, "rb")
            translation = openai.Audio.translate("whisper-1", audio_)

            result = translation["text"]
            
            return result

        def get_chat_completions(self, model, messages, temperature, n, stop, max_tokens):
            '''
            Get chat completions from OpenAI API
            '''
            import r_openai as openai
            import json

            response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            n=n,
            stop=stop,
            max_tokens=max_tokens
            )
            
            response_dict = json.loads(json.dumps(response))
            
            return response_dict
        
    def parse_to_openai_schema(schema_dict):

        properties = {}
        for key, value in schema_dict.items():
            if isinstance(value, dict):
                item_schema = parse_to_openai_schema(value)
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
                        nested_props = parse_to_openai_schema(first_item)
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
    
    try:
        if module == "Connect":
            api_key = GetParams("api_key")
            result = GetParams("result_var")

            try:
                mod_openai = openaiObject(api_key)
                auth = mod_openai.get_auth()
                SetVar(result, True)

            except Exception as e:
                traceback.print_exc()
                PrintException()
                SetVar(result, False)
                raise e
            
        if module == "Completion":
            prompt = GetParams("prompt")
            model = GetParams("model")
            temperature = float(GetParams("temperature")) if GetParams("temperature") else 0
            max_tokens = int(GetParams("max_tokens")) if GetParams("max_tokens") else 256
            stop = GetParams("stop_sequence") if GetParams("stop_sequence") else None
            result = GetParams("result_var")

            response = mod_openai.get_completions(prompt, model, max_tokens, temperature, 1, 0, 0, stop)
            
            response = response.replace("\n", "")
            
            SetVar(result, response)


        if module == "whisper":
            audio_file = GetParams("audio_file")
            result = GetParams("result_var")

            response = mod_openai.get_transcript(audio_file)

            SetVar(result, response)
            
        if module == "translate":
            audio_file = GetParams("audio_file")
            result = GetParams("result_var")
            
            response = mod_openai.get_audio_translations(audio_file)
            SetVar(result, response)
            
        if module == "chat":
            import ast

            model = GetParams("model")
            messages = eval(GetParams("messages")) if GetParams("messages") else None
            temperature = float(GetParams("temperature")) if GetParams("temperature") else 1
            n = int(GetParams("n")) if GetParams("n") else 1
            stop = GetParams("stop_sequence") if GetParams("stop_sequence") else None
            max_tokens = int(GetParams("max_tokens")) if GetParams("max_tokens") else 256
            result = GetParams("result_var")
            only_text = GetParams("only_text") or False
            image_path = GetParams("image_path") or None
            detail = GetParams("detail")
            schema_dict = GetParams("schema")

            if not messages:
                raise Exception("Messages parameter is required")
            
            if not detail:
                detail = "low"
            if image_path:
                base64_image = mod_openai.encode_image(image_path)
                extension = image_path.split(".")[-1]
                
                for message in reversed(messages):
                    if message["role"] == "user":
                        message["content"] = [
                            {
                                "type": "text",
                                "text": message["content"]
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": detail
                                }
                            }
                        ]
                        break

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {mod_openai.api_key}"
                }

                payload = {
                    "model": model,
                    "messages": messages,
                    "max_tokens": max_tokens,
                }

                if schema_dict:
                    try:
                        schema_dict = ast.literal_eval(schema_dict)
                        schema = parse_to_openai_schema(schema_dict)
                    except Exception as e:
                        print("An error has ocurred while trying to parse the schema")
                        raise e
                    
                    payload["response_format"] = {
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

                response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

                if response.json().get("error"):
                    raise Exception(response.json().get("error").get("message"))
                
                if only_text:
                    response = response.json()["choices"][0]["message"]["content"]
                else:
                    response = response.json()

            else:
                if schema_dict:
                    schema_dict = ast.literal_eval(schema_dict)
                response = mod_openai.get_chat_completions(model, messages, temperature, n, stop, max_tokens, only_text, schema_dict)

            
            SetVar(result, response)

        if module == "OpenAI":
            # This is an old version of the command, it is not visible anymore in the package.json in Rocketbot v2023, 
            # but it is still used by some users so it is kept here. Please do not delete it.
            prompt = GetParams("prompt")
            model = GetParams("model")
            if not model:
                model = "text-davinci-003"

            max_tokens = GetParams("max_tokens")
            if not max_tokens:
                max_tokens = 256
            temperature = GetParams("temperature")
            if not temperature:
                temperature = 0
            top_p = GetParams("top_p")
            if not top_p:
                top_p = 1
            frequency_penalty = GetParams("frequency_penalty")
            if not frequency_penalty:
                frequency_penalty = 0
            presence_penalty = GetParams("presence_penalty")
            if not presence_penalty:
                presence_penalty = 0
            stop = GetParams("stop_sequence")

            var_ = GetParams("result_var")
            openai.api_key = GetParams("api_key")
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=int(max_tokens),
                temperature=float(temperature),
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                stop=stop,
            )
            print(response.choices[0].text)
            SetVar(var_, json.loads(json.dumps(response)))


    except Exception as e:
        PrintException()
        raise e

except Exception as e:
    traceback.print_exc()
    raise e
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

__author__ = "David Cuello <david@rocketbot.com>"
__version__ = "1.0.1"

import requests
import os
import sys
import json

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'OpenAI' + os.sep + 'libs' + os.sep

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32 and cur_path_x64 not in sys.path:
    sys.path.append(cur_path_x64)
elif sys.maxsize <= 2**32 and cur_path_x86 not in sys.path:
    sys.path.append(cur_path_x86)
    
import openai 
global mod_openai

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

class OpenAI_RB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.get_auth()
        
    def get_auth(self):
        '''
        Authenticate with OpenAI API
        '''
        openai.api_key = self.api_key
        openai.Model.list()
        print("Authentication successful")

    def get_completions(self, prompt, model, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop):
        '''
        Get text completions from OpenAI API
        '''
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
        audio_ = open(audio_file, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_)
        
        result = transcript["text"].encode().decode('unicode_escape').encode('latin-1').decode('utf-8')
        
        return result


try:
    if module == "Connect":
        api_key = GetParams("api_key")
        result = GetParams("result_var")

        try:
            mod_openai = OpenAI_RB(api_key)
            SetVar(result, True)

        except Exception as e:
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
        
        SetVar(result, response)


    if module == "whisper":
        audio_file = GetParams("audio_file")
        result = GetParams("result_var")

        response = mod_openai.get_transcript(audio_file)

        SetVar(result, response)
        
        
    if module == "OpenAI":
        # This is an old version of the command, it is not visible anymore in the package.json, but it is still used by some users so it is kept here. Please do not delete it.
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
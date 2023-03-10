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

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")


try:
    if module == "OpenAI":
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
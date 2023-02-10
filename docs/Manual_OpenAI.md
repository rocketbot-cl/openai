# OpenAI
  
This module connects to the OpenAI API. You can query natural language models and get a response based on the context you provide.  

*Read this in other languages: [English](Manual_OpenAI.md), [Español](Manual_OpenAI.es.md).*
  
![banner](imgs/Banner_OpenAI.png)
## How to install this module
  
Installation can be:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The name of the folder must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh the browser to be able to use the new module.
2. Automatic: When you enter Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, find the desired module and press install.  


## How to use this module
To use this module, you need to go to OpenAI and get an API key. Go to https://platform.openai.com/account/api-keys to get a key.


## Description of the commands

### Ask
  
This command asks OpenAI for an answer. You need to have an OpenAI key. Go to https://platform.openai.com/account/api-keys to get a key.
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Prompt to OpenAI. The more information and context you provide, the better and more complete the answer will be.|Prompt to OpenAI|
|Secret API key|Secret API key needed to connect. It is obtained from the page https//platform.openai.com/account/api-keys|000-000|
|Model|OpenAI model to use.|Model|
|Temperature|Default 0. Value between 0 and 1. The higher the value, the more creative the answers will be, but they can also be more incoherent.|0|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.||
|Variable where to save the result of OpenAI|Variable where to save the result of OpenAI|Variable|

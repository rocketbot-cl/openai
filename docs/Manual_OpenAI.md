# OpenAI
  
This module connects to the OpenAI API. You can perform actions such as making a query to a natural language model, transcribing an audio or translating an audio to English.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*
  
![banner](imgs/Banner_OpenAI.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to OpenAI
  
This command connects to OpenAI with the specified secret API key.
|Parameters|Description|example|
| --- | --- | --- |
|Secret API key|Secret API key needed to connect. It is obtained from the page https//platform.openai.com/account/api-keys|000-000|
|Variable where the result of the connection will be stored|Variable where the result of the connection will be stored. It will return True if the connection was successful|Variable|

### Make query
  
This command allows you to make a query to OpenAI. The connection command must be executed previously.
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Prompt to OpenAI. The more information and context you provide, the better and more complete the answer will be.|Prompt to OpenAI|
|Model|OpenAI model to use.|Model|
|Temperature|Default 0. Value between 0 and 1. The higher the value, the more creative the answers will be, but they can also be more incoherent.|0|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.| |
|Variable where to save the result of OpenAI|Variable where to save the result of OpenAI|Variable|

### Transcribe audio
  
This command transcribes an audio to text. The connection command must be executed previously.
|Parameters|Description|example|
| --- | --- | --- |
|Audio file|Path to the audio file to be transcribed|C:/Users/User/Desktop/audio.mp3|
|Variable where the result will be stored|Variable where the result of the transcription will be stored|Variable|

### Translate audio
  
This command translates an audio to text in English. The connection command must be executed previously.
|Parameters|Description|example|
| --- | --- | --- |
|Audio file|Path to the audio file to be translated to English|C:/Users/User/Desktop/audio.mp3|
|Variable where the result will be stored|Variable where the result of the translation will be stored|Variable|

### Make a query in chat
  
This command allows you to make a chat query to OpenAI. The connection command must be executed previously.
|Parameters|Description|example|
| --- | --- | --- |
|Messages|Conversation messages in JSON format.|[{"role": "system", "content": "You are a very helpful assistant."}, 
{"role": "user", "content": "Explain asynchronous programming in the style of pirate Blackbeard."}]|
|Model|OpenAI model to use.|Model|
|Temperature|Default 0. Value between 0 and 2. The higher the value, the more creative the answers will be, but they can also be more incoherent.|1|
|Number of responses|How many chat completion choices to generate for each input message.|1|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.| |
|Variable where to save the result of OpenAI|Variable where to save the result of OpenAI|Variable|

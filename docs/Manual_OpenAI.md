# OpenAI
  
This module connects to the OpenAI API. You can perform actions such as making a query to a natural language model, transcribing an audio or translating an audio to English.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*
  
![banner](imgs/Banner_OpenAI.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module

Before using this module, you must obtain your apikey from the OpenAI API Platform.

1. Go to [OpenAI API Platform](https://platform.openai.com/docs/overview) and log in or sign up.
2. Go to Dashboard -> [API keys](https://platform.openai.com/api-keys) and create a new secret key with any name you want and All permisions.
3. Copy the apikey and use it in the `Connect to OpenAI` command
4. Run the command and if the result is True, you are ready to use the OpenAI commands.

Note: If you get this error message: 

`You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.`

You need to upgrade your plan in the OpenAI API Platform, you can do it [here](https://platform.openai.com/settings/organization/billing/overview)

For more information about the OpenAI API, you can check the [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/introduction)


## Description of the commands

### Connect to OpenAI
  
This command connects to OpenAI with the specified secret API key.
|Parameters|Description|example|
| --- | --- | --- |
|Secret API key|Secret API key needed to connect. It is obtained from the page https//platform.openai.com/account/api-keys|000-000|
|Variable where the result of the connection will be stored|Variable where the result of the connection will be stored. It will return True if the connection was successful|Variable|

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
|Messages|Conversation messages in JSON format.|[{"role": "system", "content": "You are a very helpful assistant."}, {"role": "user", "content": "Explain asynchronous programming in the style of pirate Blackbeard."}]|
|Image file to send to chat (optional)|If you attach an image, the AI will use it to respond to the query.|C:/Desktop/image.jpg|
|Model|OpenAI model to use.|gpt-3.5-turbo|
|Temperature|Default 0. Value between 0 and 2. The higher the value, the more creative the answers will be, but they can also be more incoherent.|1|
|Number of responses|How many chat completion choices to generate for each input message.|1|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.| |
|Variable where to save the result of OpenAI|Variable where to save the result of OpenAI|Variable|
|Get only text from the response|If activated, only the text of the response will be obtained, without the rest of the information.|False|

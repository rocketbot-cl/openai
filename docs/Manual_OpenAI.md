



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

For more information about the OpenAI API, you can check the [OpenAI API 
Documentation](https://platform.openai.com/docs/api-reference/introduction)

## Description of the commands

### Connect to OpenAI
  
This command connects to OpenAI with the specified secret API key.
|Parameters|Description|example|
| --- | --- | --- |
|Secret API key|Secret API key needed to connect. It is obtained from the page https//platform.openai.com/account/api-keys|000-000|
|Variable where the result of the connection will be stored|Variable where the result of the connection will be stored. It will return True if the connection was successful|Variable|

### Make query (deprecated)
  
This command allows you to make a query to OpenAI. The connection command must be executed previously. This command is deprecated, it is recommended to use the 'Make query in chat' command.
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
|Image file to send to chat (optional)|If you attach an image, the AI will use it to respond to the query.|C:/Desktop/image.jpg|
|Nivel de detalle|Image Analysis Depth.|Low|
|Model|OpenAI model to use.|gpt-3.5-turbo|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Temperature|Default 0. Value between 0 and 2. The higher the value, the more creative the answers will be, but they can also be more incoherent.|1|
|Number of responses|How many chat completion choices to generate for each input message.|1|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.| |
|Get only text from the response|If activated, only the text of the response will be obtained, without the rest of the information.|False|
|Variable where to save the result of OpenAI|Variable where to save the result of OpenAI|Variable|

### Make a query with history
  
Queries OpenAI keeping a conversation thread by its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Message / Prompt|The main text of your query. Required. This message is sent under the 'user' role. If there are linked files or images, they will be associated with this text.|Write the main task or question|
|System instructions (optional)|Base behavior or system context that will guide the model's responses.|You are an expert technical assistant...|
|Model|OpenAI model to use. Requires a model compatible with the Responses API and attached tools (e.g., gpt-4o).|gpt-4o|
|Conversation ID (optional)|ID of an existing conversation. Allows maintaining the conversation context, creating a threaded conversation. If not provided, a new conversation will be generated.|conv_abc123|
|File IDs (optional)|List of File IDs of files to be analyzed, modified or executed using the 'code_interpreter' tool from OpenAI. If you don't want to reuse a file, you can provide its path, which will cause the module to upload and download it automatically upon command completion.|[file-abc123, C:/path/file.pdf]|
|Vector Store IDs (optional)|List of Vector Store IDs with the files to be read or used as context using the 'file_search' tool.|["vs-123", "vs-456"]|
|Image File IDs (optional)|List of dictionaries with Image File IDs and image Analysis Depth. The available types in the detail field are 'low', 'high', 'auto' and 'original'.|["{"file_id": file-img123, "detail": "auto"}", {...}]|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Length of the response|Maximum length of the response. Default 1024.|1024|
|Temperature|Default 0. Value between 0 and 1. The higher the value, the more creative the answers will be, but they can also be more incoherent.|0|
|Assign result to variable|Variable where the result of the command will be stored|Variable|

### Upload file
  
Uploads a local file to OpenAI and returns its File Id.
|Parameters|Description|example|
| --- | --- | --- |
|Local file path|Select the file to upload|C:/path/document.pdf|
|Assign result to variable|Variable where the File Id returned by OpenAI will be saved.|Variable|

### Update or Create Vector Store
  
Creates or updates a Vector Store for OpenAI to read and extract information from files within it.
|Parameters|Description|example|
| --- | --- | --- |
|Vector Store ID (optional)|If provided, files will be added to this existing Vector Store. If empty, a new one is created.|vs-abc123|
|Name (optional)|Assign a name to the Vector Store.|vector_store_name|
|File IDs to add to the Vector Store.|List of File IDs to add to the Vector Store.|[file-12344, file-12345]|
|Assign result to variable|Variable where the result of the command will be stored|Variable|

### List Files / Vector Stores
  
Queries the OpenAI API and returns a list of uploaded files or Vector Stores created in the account.
|Parameters|Description|example|
| --- | --- | --- |
|Resource to list|Select whether you want to view the uploaded Files Ids or the Vector Stores ids.|Files (File ID)|
|Assign result to variable|Variable where the result of the command will be stored|Variable|

### Delete File / Vector Store
  
Calls the OpenAI API to delete a resource by ID to clean up storage.
|Parameters|Description|example|
| --- | --- | --- |
|Resource to delete|Select whether you want to delete a File or a Vector Store.|Files (File ID)|
|Identifier|The File ID or Vector Store ID you want to delete.|file-123 / vs-123|
|Assign result to variable|Variable where the result of the command will be stored|Variable|

### Ask
  
This command asks OpenAI for an answer. You need to have an OpenAI key. Go to https://platform.openai.com/account/api-keys to get a key.
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Prompt to OpenAI. The more information and context you provide, the better and more complete the answer will be.|Prompt to OpenAI|
|Secret API key|Secret API key needed to connect. It is obtained from the page https//platform.openai.com/account/api-keys|000-000|
|Model|OpenAI model to use.|Model|
|Temperature|Default 0. Value between 0 and 1. The higher the value, the more creative the answers will be, but they can also be more incoherent.|0|
|Length of the response|Maximum length of the response. Default 256.|256|
|Stop sequence|Optional text sequence in which if it appears, the response stops.| |
|Assign result to variable|Variable where the result of the command will be stored|Variable|

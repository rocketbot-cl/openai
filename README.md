



# OpenAI
  
This module connects to the OpenAI API. You can perform actions such as making a query to a natural language model, transcribing an audio or translating an audio to English.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Connect to OpenAI  
This command connects to OpenAI with the specified secret API key.

2. Make query (deprecated)  
This command allows you to make a query to OpenAI. The connection command must be executed previously. This command is deprecated, it is recommended to use the 'Make query in chat' command.

3. Transcribe audio  
This command transcribes an audio to text. The connection command must be executed previously.

4. Translate audio  
This command translates an audio to text in English. The connection command must be executed previously.

5. Make a query in chat  
This command allows you to make a chat query to OpenAI. The connection command must be executed previously.

6. Make a query with history  
Queries OpenAI keeping a conversation thread by its ID.

7. Upload file  
Uploads a local file to OpenAI and returns its File Id.

8. Update or Create Vector Store  
Creates or updates a Vector Store for OpenAI to read and extract information from files within it.

9. List Files / Vector Stores  
Queries the OpenAI API and returns a list of uploaded files or Vector Stores created in the account.

10. Delete File / Vector Store  
Calls the OpenAI API to delete a resource by ID to clean up storage.

11. Ask  
This command asks OpenAI for an answer. You need to have an OpenAI key. Go to https://platform.openai.com/account/api-keys to get a key.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**openai**](https://pypi.org/project/openai/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)
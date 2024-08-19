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

2. Transcribe audio  
This command transcribes an audio to text. The connection command must be executed previously.

3. Translate audio  
This command translates an audio to text in English. The connection command must be executed previously.

4. Make a query in chat  
This command allows you to make a chat query to OpenAI. The connection command must be executed previously.



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
# OpenAI
  
Este módulo se conecta a la API de OpenAI. Puedes ejecutar acciones como realizar una consulta a un modelo de lenguaje natural, transcribir un audio o traducir un audio al inglés.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Conectar a OpenAI  
Este comando conecta a OpenAI con la API key secreta especificada.

2. Transcribir audio  
Este comando transcribe un audio a texto. Debe ejecutarse el comando de conexión previamente.

3. Traducir audio  
Este comando traduce un audio a texto en inglés. El comando de conexión debe ser ejecutado previamente.

4. Realizar consulta en chat  
Este comando permite realizar una consulta en formato de chat a OpenAI. Debe ejecutarse el comando de conexión previamente.



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
# OpenAI
  
Este módulo se conecta a la API de OpenAI. Puedes realizar consultas a modelos de lenguaje natural y obtener una respuesta basada en el contexto que le entregues.  

*Read this in other languages: [English](Manual_OpenAI.md), [Español](Manual_OpenAI.es.md).*
  
![banner](imgs/Banner_OpenAI.png)

## Como instalar este módulo
  
La instalación puede ser:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  




## Como usar este módulo
Para usar este módulo, tienes que ingresar a OpenAI y obtener una clave de API. Ve a https://platform.openai.com/account/api-keys para obtener una clave.


## Descripción de los comandos

### Preguntar
  
Este comando Consulta a OpenAI para obtener una respuesta. Necesitas tener una clave de OpenAI. Ve a https://platform.openai.com/account/api-keys para obtener una clave.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta|Consulta a OpenAI. Mientras mas informacion y contexto se proporcione, mejor y más completa será la respuesta.|Consulta a OpenAI|
|API key secreta|API key secreta necesaria para conectarse. Se obtiene de la pagina https//platform.openai.com/account/api-keys|000-000|
|Modelo|Modelo de OpenAI a usar.|Modelo|
|Temperatura|Por defecto 0. Valor entre 0 y 1. Cuanto mayor sea el valor, las respuestas serán más creativas, pero también pueden llegar a ser más incoherentes.|0|
|Longitud de la respuesta|Longitud máxima de la respuesta. Por defecto 256.|256|
|Secuencia de fin|Secuencia de texto opcional en la cual si aparece, la respuesta se detiene.||
|Variable donde se almacena el resultado de OpenAI|Variable donde se almacena el resultado de OpenAI|Variable|

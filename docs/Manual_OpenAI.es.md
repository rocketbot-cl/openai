# OpenAI
  
Este módulo se conecta a la API de OpenAI. Puedes realizar consultas a modelos de lenguaje natural y obtener una respuesta basada en el contexto que le entregues.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*
  
![banner](imgs/Banner_OpenAI.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar a OpenAI
  
Este comando conecta a OpenAI con la API key secreta especificada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API key secreta|API key secreta necesaria para conectarse. Se obtiene de la pagina https//platform.openai.com/account/api-keys|000-000|
|Variable donde se almacenará el resultado de la conexión|Variable donde se almacenará el resultado de la conexión. Devolverá True si la conexión fue exitosa|Variable|

### Realizar consulta
  
Este comando permite realizar una consulta a OpenAI. Debe ejecutarse el comando de conexión previamente.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta|Consulta a OpenAI. Mientras mas informacion y contexto se proporcione, mejor y más completa será la respuesta.|Consulta a OpenAI|
|Modelo|Modelo de OpenAI a usar.|Modelo|
|Temperatura|Por defecto 0. Valor entre 0 y 1. Cuanto mayor sea el valor, las respuestas serán más creativas, pero también pueden llegar a ser más incoherentes.|0|
|Longitud de la respuesta|Longitud máxima de la respuesta. Por defecto 256.|256|
|Secuencia de fin|Secuencia de texto opcional en la cual si aparece, la respuesta se detiene.| |
|Variable donde se almacena el resultado de OpenAI|Variable donde se almacena el resultado de OpenAI|Variable|

### Transcribir audio
  
Este comando transcribe un audio a texto.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo de audio|Ruta al archivo de audio que se desea transcribir|C:/Users/User/Desktop/audio.mp3|
|Variable donde se almacenará el resultado|Variable donde se almacenará el resultado de la transcripción|Variable|

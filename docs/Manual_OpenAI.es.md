# OpenAI
  
Este módulo se conecta a la API de OpenAI. Puedes ejecutar acciones como realizar una consulta a un modelo de lenguaje natural, transcribir un audio o traducir un audio al inglés.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*

![banner](imgs/Banner_OpenAI.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Como usar este modulo

Antes de usar este módulo, debes obtener tu apikey de la plataforma OpenAI API.

1. Ve a [OpenAI API Platform](https://platform.openai.com/docs/overview) e inicia sesión o regístrate.
2. Ve a Dashboard -> [API keys](https://platform.openai.com/api-keys) y crea una nueva clave secreta con el nombre que desees y todos los permisos.
3. Copia la apikey y úsala en el comando `Conectar a OpenAI`
4. Ejecuta el comando y si el resultado es True, estás listo para usar los comandos de OpenAI.

Nota: Si obtienes este mensaje de error:

`You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.`

Necesitas actualizar tu plan en la plataforma OpenAI API, puedes hacerlo [aquí](https://platform.openai.com/settings/organization/billing/overview)

Para obtener más información sobre la API de OpenAI, puedes consultar la [Documentación de la API de OpenAI](https://platform.openai.com/docs/api-reference/introduction)

## Descripción de los comandos

### Conectar a OpenAI
  
Este comando conecta a OpenAI con la API key secreta especificada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API key secreta|API key secreta necesaria para conectarse. Se obtiene de la pagina https//platform.openai.com/account/api-keys|000-000|
|Variable donde se almacenará el resultado de la conexión|Variable donde se almacenará el resultado de la conexión. Devolverá True si la conexión fue exitosa|Variable|

### Transcribir audio
  
Este comando transcribe un audio a texto. Debe ejecutarse el comando de conexión previamente.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo de audio|Ruta al archivo de audio que se desea transcribir|C:/Users/User/Desktop/audio.mp3|
|Variable donde se almacenará el resultado|Variable donde se almacenará el resultado de la transcripción|Variable|

### Traducir audio
  
Este comando traduce un audio a texto en inglés. El comando de conexión debe ser ejecutado previamente.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo de audio|Ruta al archivo de audio que se desea traducir al inglés|C:/Users/User/Desktop/audio.mp3|
|Variable donde se almacenará el resultado|Variable donde se almacenará el resultado de la traducción|Variable|

### Realizar consulta en chat
  
Este comando permite realizar una consulta en formato de chat a OpenAI. Debe ejecutarse el comando de conexión previamente.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Mensajes|Mensajes de la conversación en formato JSON.|[{"role": "system", "content": "Eres un ayudante muy útil."}, {"role": "user", "content": "Explique la programación asíncrona al estilo del pirata Barbanegra."}]|
|Archivo de imagen a enviar al chat (opcional)|Si adjuntas una imagen la IA la usará para responder a la consulta.|C:/Desktop/image.jpg|
|Modelo|Modelo de OpenAI a usar.|gpt-3.5-turbo|
|Temperatura|Por defecto 1. Valor entre 0 y 2. Cuanto mayor sea el valor, las respuestas serán más creativas, pero también pueden llegar a ser más incoherentes.|1|
|Cantidad de respuestas|Cuántas opciones de finalización de chat se generan para cada mensaje de entrada.|1|
|Longitud de la respuesta|Longitud máxima de la respuesta. Por defecto 256.|256|
|Secuencia de fin|Secuencia de texto opcional en la cual si aparece, la respuesta se detiene.| |
|Variable donde se almacena el resultado de OpenAI|Variable donde se almacena el resultado de OpenAI|Variable|
|Obtener solo texto de la respuesta|Si se activa, solo se obtendrá el texto de la respuesta, sin el resto de información.|False|

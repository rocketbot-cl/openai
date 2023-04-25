# OpenAI
  
Este módulo conecta-se à API da OpenAI. Pode executar ações como fazer uma consulta a um modelo de linguagem natural, transcrever um áudio ou traduzir um áudio para inglês.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*
  
![banner](imgs/Banner_OpenAI.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar-se ao OpenAI
  
Este comando conecta a OpenAI con la API key secreta especificada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Secret API key|Secret API key necessária para se conectar. Ela é obtida na página https//platform.openai.com/account/api-keys|000-000|
|Variável onde o resultado da conexão será armazenado|Variável onde o resultado da conexão será armazenado. Ele retornará True se a conexão for bem-sucedida|Variável|

### Fazer uma consulta
  
Este comando permite fazer uma consulta à OpenAI. O comando de conexão deve ser executado previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Prompt para OpenAI. Quanto mais informações e contexto você fornecer, melhor e mais completa será a resposta.|Prompt para OpenAI|
|Modelo|Modelo OpenAI a usar.|Modelo|
|Temperatura|Padrão 0. Valor entre 0 e 1. Quanto maior o valor, mais criativas serão as respostas, mas também podem ser mais incoerentes.|0|
|Comprimento da resposta|Comprimento máximo da resposta. Padrão 256.|256|
|Sequência de parada|Sequência de texto opcional na qual, se aparecer, a resposta para.| |
|Variável onde salvar o resultado do OpenAI|Variável onde salvar o resultado do OpenAI|Variável|

### Transcrever áudio
  
Este comando transcreve um áudio para texto. O comando de conexão deve ser executado previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo de áudio|Caminho para o arquivo de áudio que será transcrito|C:/Users/User/Desktop/audio.mp3|
|Variável onde o resultado será armazenado|Variável onde o resultado da transcrição será armazenado|Variável|

### Traduzir áudio
  
Este comando traduz um áudio para texto em inglês. O comando de conexão deve ser executado previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo de áudio|Caminho para o arquivo de áudio que deseja traduzir para o inglês|C:/Users/User/Desktop/audio.mp3|
|Variável onde o resultado será armazenado|Variável onde o resultado da tradução será armazenado|Variável|
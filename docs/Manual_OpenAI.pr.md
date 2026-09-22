



# OpenAI
  
Este módulo conecta-se à API da OpenAI. Pode executar ações como fazer uma consulta a um modelo de linguagem natural, transcrever um áudio ou traduzir um áudio para inglês.  

*Read this in other languages: [English](Manual_OpenAI.md), [Português](Manual_OpenAI.pr.md), [Español](Manual_OpenAI.es.md)*
  
![banner](imgs/Banner_OpenAI.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

Antes de usar este módulo, você deve obter sua apikey da Plataforma OpenAI API.

1. Acesse a [Plataforma OpenAI API](https://platform.openai.com/docs/overview) e faça login ou cadastre-se.
2. Acesse Dashboard -> [API keys](https://platform.openai.com/api-keys) e crie uma nova chave secreta com o nome que desejar e todas as permissões.
3. Copie a apikey e use-a no comando `Conectar a OpenAI`
4. Execute o comando e se o resultado for True, você está pronto para usar os comandos OpenAI.

Nota: Se você receber esta mensagem de erro:

`You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.`

Você precisa atualizar seu plano na Plataforma OpenAI API, você pode fazer isso [aqui](https://platform.openai.com/settings/organization/billing/overview)

Para obter mais informações sobre a API da OpenAI, você pode consultar a 
[Documentação da API da OpenAI](https://platform.openai.com/docs/api-reference/introduction)
## Descrição do comando

### Conectar-se ao OpenAI
  
Este comando conecta a OpenAI con la API key secreta especificada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Secret API key|Secret API key necessária para se conectar. Ela é obtida na página https//platform.openai.com/account/api-keys|000-000|
|Variável onde o resultado da conexão será armazenado|Variável onde o resultado da conexão será armazenado. Ele retornará True se a conexão for bem-sucedida|Variável|

### Fazer uma consulta (obsoleto)
  
Este comando permite fazer uma consulta à OpenAI. O comando de conexão deve ser executado previamente. Este comando está obsoleto, é recomendável usar o comando 'Fazer consulta no chat'.
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

### Fazer uma consulta em chat
  
Este comando permite fazer uma consulta em formato de chat para OpenAI. O comando de conexão deve ser executado previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Mensagens|Mensagens da conversa em formato JSON.|[{"role": "system", "content": "Você é um assistente muito útil."}, 
{"role": "user", "content": "Explique a programação assíncrona no estilo do pirata Barba Negra."}]|
|Arquivo de imagem para enviar ao chat (opcional)|Se você anexar uma imagem, a IA a usará para responder à consulta.|C:/Desktop/image.jpg|
|Nível de detalhe|Profundidade de análise de imagem.|Low|
|Modelo|Modelo OpenAI a usar.|gpt-3.5-turbo|
|Esquema de resposta (opcional)|Formato do conteúdo gerado (opcional). 
Os tipos possíveis são "string", "number", "integer", "boolean" e "array". 
Para indicar um objeto aninhado, você pode usar outro dicionário com a mesma estrutura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Temperatura|Padrão 0. Valor entre 0 e 2. Quanto maior o valor, mais criativas serão as respostas, mas também podem ser mais incoerentes. Deixar vazio ao usar modelos de raciocínio (o1, o3, gpt-5, etc.) ao estes usarem automaticamente 1 de temperatura.|0|
|Quantidade de respostas|Quantas opções de conclusão de chat gerar para cada mensagem de entrada.|1|
|Comprimento da resposta|Comprimento máximo da resposta. Padrão 256. Modelos de raciocínio (o1, o3, gpt-5, etc.) podem retornar respostas vazias se um valor alto não for definido, podendo precisar de até 8000.|256|
|Sequência de parada|Sequência de texto opcional na qual, se aparecer, a resposta para.| |
|Obter apenas texto da resposta|Se ativado, apenas o texto da resposta será obtido, sem o restante das informações.|False|
|Variável onde salvar o resultado do OpenAI|Variável onde salvar o resultado do OpenAI|Variável|

### Obter modelos
  
Este comando recupera os modelos disponíveis. O comando de conexão deve ser executado previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável onde o resultado será armazenado|Variável onde o resultado dos modelos será armazenado|Variável|

### Perguntar
  
Este comando pergunta à OpenAI para obter uma resposta. Você precisa ter uma chave OpenAI. Vá para https://platform.openai.com/account/api-keys para obter uma chave.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Prompt to OpenAI. The more information and context you provide, the better and more complete the answer will be.|Prompt to OpenAI|
|Chave secreta da API|Chave secreta da API necessária para conectar. É obtido na página https//platform.openai.com/account/api-keys|000-000|
|Modelo|Modelo OpenAI para usar.|Modelo|
|Temperatura|Padrão 0. Valor entre 0 e 1. Quanto maior o valor, mais criativas serão as respostas, mas também podem ser mais incoerentes.|0|
|Comprimento da resposta|Comprimento máximo da resposta. Padrão 256.|256|
|Sequência de parada|Sequência de texto opcional na qual, se aparecer, a resposta para.| |
|Variável onde salvar o resultado do OpenAI|Variável onde salvar o resultado do OpenAI|Variável|

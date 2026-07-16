



# OpenAI
  
Este módulo conecta-se à API da OpenAI. Pode executar ações como fazer uma consulta a um modelo de linguagem natural, transcrever um áudio ou traduzir um áudio para inglês.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Conectar-se ao OpenAI  
Este comando conecta a OpenAI con la API key secreta especificada.

2. Fazer uma consulta (obsoleto)  
Este comando permite fazer uma consulta à OpenAI. O comando de conexão deve ser executado previamente. Este comando está obsoleto, é recomendável usar o comando 'Fazer consulta no chat'.

3. Transcrever áudio  
Este comando transcreve um áudio para texto. O comando de conexão deve ser executado previamente.

4. Traduzir áudio  
Este comando traduz um áudio para texto em inglês. O comando de conexão deve ser executado previamente.

5. Fazer uma consulta em chat  
Este comando permite fazer uma consulta em formato de chat para OpenAI. O comando de conexão deve ser executado previamente.

6. Fazer consulta com histórico  
Consulta a OpenAI mantendo o tópico de uma conversa por meio de seu ID.

7. Enviar arquivo  
Carrega um arquivo local no OpenAI e retorna seu File Id para uso posterior.

8. Atualizar ou Criar Vector Store  
Cria ou atualiza um Vector Store para permitir que o OpenAI possa lê-lo e extrair informações dos arquivos dentro dele.

9. Listar Arquivos / Vector Stores  
Consulta a API da OpenAI e retorna uma lista de arquivos ou Vector Stores.

10. Excluir Arquivo / Vector Store  
Chama a API da OpenAI para deletar um recurso pelo ID e limpar o armazenamento.

11. Perguntar  
Este comando pergunta à OpenAI para obter uma resposta. Você precisa ter uma chave OpenAI. Vá para https://platform.openai.com/account/api-keys para obter uma chave.  




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
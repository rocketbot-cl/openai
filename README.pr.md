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

2. Transcrever áudio  
Este comando transcreve um áudio para texto. O comando de conexão deve ser executado previamente.

3. Traduzir áudio  
Este comando traduz um áudio para texto em inglês. O comando de conexão deve ser executado previamente.

4. Fazer uma consulta em chat  
Este comando permite fazer uma consulta em formato de chat para OpenAI. O comando de conexão deve ser executado previamente.



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
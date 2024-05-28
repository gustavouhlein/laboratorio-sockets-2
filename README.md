# Sistema de Compartilhamento de Arquivos com Sockets

Este projeto consiste em um sistema de compartilhamento de arquivos utilizando sockets em Python.

## Funcionamento

### Servidor (`server.py`)

O servidor aguarda conexões de clientes e envia a lista de arquivos disponíveis na pasta 'Arquivos - Servidor'. Quando um cliente solicita um arquivo específico, o servidor o envia ao cliente.

### Cliente (`client.py`)

O cliente se conecta ao servidor e recebe a lista de arquivos disponíveis. O usuário escolhe um arquivo da lista e o cliente solicita esse arquivo ao servidor. Após receber o arquivo, o cliente o salva na pasta 'Arquivos - Cliente'.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para implementar a lógica do servidor e do cliente.
- **Sockets**: Utilizados para a comunicação entre o servidor e o cliente.
- **Pickle**: Biblioteca para serialização de objetos Python, utilizada para enviar e receber a lista de arquivos.
- **OS**: Biblioteca para interação com o sistema operacional, utilizada para manipulação de arquivos e pastas.

## Executando o Projeto

1. Execute o servidor executando o script `server.py`.
2. Execute o cliente executando o script `client.py`.
3. Siga as instruções no terminal do cliente para escolher e receber arquivos do servidor.

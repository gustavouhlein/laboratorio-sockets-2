import socket
import os
import pickle

def send_file(client_socket, filename):
    # Monta o caminho completo do arquivo
    filepath = os.path.join("Arquivos - Servidor", filename)

    try:
        # Tenta abrir o arquivo e enviá-lo ao cliente
        with open(filepath, 'rb') as file:
            data = file.read()
            client_socket.sendall(data)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, informa o cliente
        print(f"Arquivo '{filename}' não encontrado.")
        # Envia uma mensagem indicando que o arquivo não foi encontrado
        client_socket.sendall(b'FileNotFoundError')

def send_file_list(client_socket):
    # Obtém a lista de arquivos disponíveis na pasta 'arquivos'
    folder_path = "Arquivos - Servidor"
    file_list = os.listdir(folder_path)

    # Serializa a lista e envia ao cliente
    file_list_data = pickle.dumps(file_list)
    client_socket.sendall(file_list_data)

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor aguardando conexões em {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão recebida de {addr}")

        # Envia a lista de arquivos disponíveis ao cliente
        send_file_list(client_socket)

        # Recebe o nome do arquivo escolhido pelo cliente
        filename = client_socket.recv(1024).decode('utf-8')

        print(f"Solicitado arquivo: {filename}")

        # Envia o arquivo escolhido ao cliente
        send_file(client_socket, filename)

        # Fecha a conexão com o cliente
        client_socket.close()
        print(f"Conexão encerrada com {addr}")

if __name__ == "__main__":
    main()

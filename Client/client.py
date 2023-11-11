import socket
import pickle
import os

def receive_file(client_socket, filename):
    # Recebe os dados do arquivo do servidor
    data = client_socket.recv(1024)

    if data == b'FileNotFoundError':
        # Se o arquivo não for encontrado, exibe uma mensagem
        print(f"Arquivo '{filename}' não encontrado no servidor.")
    else:
        # Caso contrário, salva o arquivo na pasta 'Arquivos - Cliente'
        client_folder = "Arquivos - Cliente"
        os.makedirs(client_folder, exist_ok=True)
        filepath = os.path.join(client_folder, filename)

        with open(filepath, 'wb') as file:
            while data:
                file.write(data)
                data = client_socket.recv(1024)
            print(f"Arquivo '{filename}' recebido e salvo em '{client_folder}'.")

def receive_file_list(client_socket):
    # Recebe a lista de arquivos disponíveis do servidor
    file_list_data = client_socket.recv(1024)
    file_list = pickle.loads(file_list_data)

    if not file_list:
        print("Nenhum arquivo disponível no servidor.")
        return None

    print("Arquivos disponíveis:")
    for idx, filename in enumerate(file_list, start=1):
        print(f"{idx}. {filename}")

    while True:
        try:
            # Cliente escolhe qual arquivo deseja obter
            choice = int(input("Digite o número do arquivo que deseja obter : "))
            if 0 <= choice <= len(file_list):
                break
            else:
                print("Escolha inválida. Digite um número válido.")
        except ValueError:
            print("Digite um número válido.")

    return file_list[choice - 1]

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Recebe a lista de arquivos disponíveis
    selected_filename = receive_file_list(client_socket)

    if selected_filename is not None:
        # Envia o nome do arquivo escolhido ao servidor
        client_socket.sendall(selected_filename.encode('utf-8'))

        # Recebe o arquivo escolhido e salva na pasta 'Arquivos - Cliente'
        receive_file(client_socket, selected_filename)

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == "__main__":
    main()

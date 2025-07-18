import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'  # IP do servidor
port = 12345         # Porta do servidor
client_socket.connect((host, port)) 

while True:
    mensagem = input("Digite uma mensagem para enviar ao servidor (ou 'sair' para encerrar): ")
    client_socket.send(mensagem.encode())  # Envia a mensagem ao servidor
    
    if mensagem.lower() == 'sair':
        print("Encerrando a conexão com o servidor.")
        break
    
    response = client_socket.recv(1024)  # Recebe a resposta do servidor
    print(f"Servidor respondeu: {response.decode()}")
    
client_socket.close()  # Fecha a conexão com o servidor
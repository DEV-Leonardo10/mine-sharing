import socket

# Criando o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definindo o IP e a porta do servidor
host = '26.248.116.171'  # IP local
port = 12345         # Porta que o servidor irá escutar

# Bind o socket ao IP e à porta
server_socket.bind((host, port))

# Colocando o servidor em modo de escuta (pode aceitar até 5 conexões simultâneas)
server_socket.listen(5)

print(f"Servidor escutando em {host}:{port}...")

# Aguardando a conexão de um cliente
client_socket, client_address = server_socket.accept()
print(f"Conexão estabelecida com {client_address}")

client_socket.send(b'Bem-vindo ao servidor!')

while True:
    mensagem = client_socket.recv(1024)  # Recebe até 1024 bytes
    if mensagem.lower() == 'sair':
        print("encerrou a conexão.")
        break
    
    print(f"Cliente disse: {mensagem.decode()}")
    
    
    resposta = input("Digite uma resposta para enviar ao cliente: ")
    client_socket.send(resposta.encode())



# Fechar a conexão após o envio
client_socket.close()

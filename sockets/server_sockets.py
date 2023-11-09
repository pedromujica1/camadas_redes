import socket

port = 10500

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('0.0.0.0',port))
server.listen()



print(f'=== Servidor aguardando conexões na porta {port} ===')

conn, addr = server.accept()
print(f'Conexão recebeida de {addr}')

while True: 
        
    #recebe os dados enviados pelo cliente
    data = conn.recv(4096)
    msg_client = data.decode().split()

    if msg_client[1] == '+':    
        resultado= (int(msg_client[0]) + int(msg_client[2]))
    elif msg_client[1] == '-':
        resultado = (int(msg_client[0]) - int(msg_client[2]))
    elif msg_client[1] == '*':  
        resultado = (int(msg_client[0]) * int(msg_client[2]))
    elif msg_client[1] == '/':  
        resultado = (int(msg_client[0]) / int(msg_client[2]))  


    msg = str(resultado)
    conn.send(msg.encode())
    #Encerra a conexão
conn.close()

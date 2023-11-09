import socket

port = 10500

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind vinculo endereço ip e porta a uma socket
server.bind(('0.0.0.0',port))

#Deixa o server pronto e preparado para receber conexoes
server.listen()



print(f'=== Servidor aguardando conexões na porta {port} ===')

conn, addr = server.accept()
print(f'Conexão recebeida de {addr}')

while True: 
        

    #recebe os dados enviados pelo cliente
    data = conn.recv(4096)
    print(f'Recebido: {data.decode()}')

    msg=input(': ')
    conn.send(msg.encode())
    #Encerra a conexão
conn.close()

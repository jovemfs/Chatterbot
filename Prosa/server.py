import socket #comunicacao

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()
client, end = server.accept()

final = False

while not final:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'E':
        final = True
    else:
        print(msg)
    client.send(input('Msg: ').encode('utf-8'))

client.close()
server.close()

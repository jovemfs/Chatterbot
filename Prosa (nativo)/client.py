import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8888))

final = False
print('Digite E para encerrar a conversa.')

while not final:
    client.send(input('Msg: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'E':
        final = True
    else:
        print(msg)

client.close()
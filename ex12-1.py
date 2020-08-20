import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter URL host:')
try:
    mysock.connect((host, 80))
except:
    print('Invalid host, quitting')
    quit()
cmd = 'GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

char_count = 0
while char_count <= 3000:
    data = mysock.recv(512)
    char_count = char_count + len(data)
    if len(data) < 1:
        break
    print(data.decode(),end='')
print('Number of characters:', char_count)

mysock.close()

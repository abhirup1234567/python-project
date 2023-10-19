import socket
import sys
import os
import tqdm
try:
    ip='127.0.0.1'
    port=3999
    server=socket.socket()
    server.bind((ip,port))
    server.listen(5)
    print(f'[*] Listening as {ip}:{port}')
except socket.error:
    print('Unable to create server')
    sys.exit()
client,addr=server.accept() # Connection established
print(f'[+] {addr} is connected...')
recv=client.recv(1024)
recv=recv.decode()
info=recv.split('<>')
filename=info[0]
filesize=int(info[1])
print(f'Recv : {recv}')
print(f'Info : {info}')
print(f'File name : {filename}')
print(f'File name : {filesize}')
progress=tqdm.tqdm(range(int(filesize)),f'Sending {filename}')
with open(filename,'wb') as file:
    while True:
        bytes_read=client.recv(4096)
        if not bytes_read:
            break
        file.write(bytes_read)
        progress.update(len(bytes_read))

import socket
import sys
import os
import tqdm

sep='<>'
BUFFER_SIZE=4096
try:
    ip='127.0.0.1'
    port=3999
    client=socket.socket()
    print(f'[*] Connecting to {ip}:{port}....')
    client.connect((ip,port))
    print(f'[+] Connected')
except socket.error:
    print('Unable to create client')
    sys.exit()
filename='file.jpg'
filesize=os.path.getsize(filename)
filesize=str(filesize)
client.send(f'{filename}{sep}{filesize}'.encode())
progress=tqdm.tqdm(range(int(filesize)),f'Sending {filename}')
with open(filename,'rb') as file:  
    while True:
        bytes_read=file.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client.sendall(bytes_read)
        progress.update(len(bytes_read))

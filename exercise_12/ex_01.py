import socket
import re

url = input('Enter a web page: ')


try:
    if re.search('.*/.*?', url):
        pureurl = re.match('.*/.*?', url)
        pure_url = pureurl.group()
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((pure_url[:13], 80))
        cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data)<1:
                break
            print(data.decode(), end='')
        mysock.close()
    else:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((url, 80))
        cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if len(data)<1:
                break
            print(data.decode(), end='')
        mysock.close()
except:
    print('Invalid url')
    exit()
    
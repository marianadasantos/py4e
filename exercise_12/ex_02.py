import socket
import re

count = dict()
url = input('Enter a web page: ')

try:
    if re.search('.*/.*?', url):
        pureurl = re.match('.*/.*?', url)
        pure_url = pureurl.group()
        print(pure_url[:-1])
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((pure_url[:-1], 80))
        cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(3000)
            for line in data:
                new_data = data.decode().split()
                for word in new_data:
                    count[word] = count.get(word, 0) +1
            print(count)
            mysock.close()
    else:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((url, 80))
except:
    print('Invalid url')
    exit()
    
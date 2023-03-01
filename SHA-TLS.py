import ssl
import socket

hostname = 'example.com'
port = 443

context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.send(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
        response = ssock.recv(1024)
        print(response)

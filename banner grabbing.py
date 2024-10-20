import socket

ip = input("Digite o IP:")
porta = int(input ("Digite a porta:"))

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print (banner)

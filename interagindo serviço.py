import socket

print ("Interagindo com FTP SERVER")

ip = input("Digite o IP:")
porta = int(input ("Digite a porta:"))
usuario = input ("Digite login:")
senha = input ("Digite senha:")
user = "USER "+usuario+"\r\n"
passw = "PASS "+senha+"\r\n"

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print (banner)


print("enviado usuario")
meusocket.send (user.encode())
banner = meusocket.recv(1024)
print(banner)

print("Enviado senha")
meusocket.send (passw.encode())
banner = meusocket.recv(1024)
print(banner)

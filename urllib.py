import urllib.request, urllib.parse, urllib.error

url = input("Digite url:")

site = urllib.request.urlopen(url)
server = site.info()

print ("O servidor web esta rodando")
print (server['server'])

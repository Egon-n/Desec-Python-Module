import requests

url = input("Digite a url:")

site = requests.get (url)
status = site.status_code

if (status == 200):
    print ("Pagina existe")

else:
    print ("Pagina não existe")

    

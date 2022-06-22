import xmlrpc.client
proxy=xmlrpc.client.ServerProxy("http://localhost:9000")
hola= proxy.list_contents("E:")
numero= len(hola)
print(hola)
print("el numero de carpetas es: ", numero)

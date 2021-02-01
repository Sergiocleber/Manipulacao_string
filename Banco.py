from extratorArgumentoUrl import ExtratorArgumentoUrl
'''
url = “https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700”

argumento = "Sergio Cleber Monentengro"
#            012345 6789
listaUrl = argumento.split("")
print(listaUrl)
'''
url = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500 "
#                       find

'''
argumentosUrl = ExtratorArgumentoUrl(url)
moedaOrigem, moedaDestino = argumentosUrl.extrairArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaOrigem, moedaDestino, valor)
'''''
#index = url.find("moedadestino") + len ("moedadestino") + 1
#substring = url[index:]
#print(substring)

#ExtratorArgumentoUrl.urlEhValida("a")

#string = "bytebank"
#stringNova = string.replace("byte","sergio", 1)
#print (stringNova)

banco1 = "bytebank"
banco2 = "Bytebank"
#print (banco1 == banco2)
urlByteBank = "https://bytebank.com"
url1        ="hhtps://buscasites.com/busca?q=https://bytebank.com"
url2        ="https://bitebank.com.br"
url3        ="https://bytebank.com/cambio/teste/teste"
print(url3.startswith(urlByteBank))
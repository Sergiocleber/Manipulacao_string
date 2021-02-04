import re
email1 = "Meu numero é 12344-1234"
email2 = "Fale comifgo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "dsadsadadsadasdasdasd 12341234 dsdasdsadsadasd 9888-1245 fdfdsfsfdsfdsfdwfsdfdfef 9876-1234 "

padrao = "[0-9]{4,5}[-]*[0-9]{4}" # Expressão regular, onde é possivel pegar numero de celular, telefone e consegue identificar se tem hifen ou não

retorno = re.findall(padrao,email4)
print(retorno)

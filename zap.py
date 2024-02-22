import pywhatkit as kt

mamae = "+5547999368853"

msg = input("digite a mensagem a ser enviada: ")
contato = input("digite o contato a ser enviado: ")

if "mamãe" in contato or "mãe" in contato:
    kt.sendwhatmsg_instantly(mamae, msg)
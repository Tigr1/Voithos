from twilio.rest import Client

# Seus credenciais da conta Twilio
account_sid = 'SKcbff8d12ea7add9d3824aeca36ead5be'
auth_token = 'c10c983e0152860df62ed3790c63414d'

# Inicializar o cliente Twilio
client = Client(account_sid, auth_token)

# Número de telefone que você está ligando (pizzaria, por exemplo)
numero_destino = '+5547991211500'  # Substitua pelo número da pizzaria

# Número de telefone que será utilizado para realizar a ligação (você)
numero_origem = '+5547999368853'  # Substitua pelo seu número registrado no Twilio

# URL do TwiML que define a ação a ser tomada quando a chamada é atendida
# Neste exemplo, apenas reproduziremos uma mensagem de áudio
url = 'http://demo.twilio.com/docs/voice.xml'

# Fazer a chamada telefônica
ligacao = client.calls.create(
    twiml='<Response><Say>Olá, gostaria de fazer um pedido por telefone.</Say></Response>',
    to=numero_destino,
    from_=numero_origem
)

print(ligacao.sid)
from twilio.rest import Client

account_sid = "seu account_sid, pegue na sua conta do twilio"
auth_token = "seu token, pegue na sua conta do twilio"
meu_numero = "seu numero pessoal - o numero que você verificou no twilio"
numero_twilio = "seu numero do twilio"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language="pt-BR">
Oiie Renato, essa ligação está automatizado.
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)
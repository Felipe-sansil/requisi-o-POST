import requests

#Declaração de variaveis
nome_completo = "Felipe Santos da Silva"
email = "********"
cpf = "********"

# URL requisição
url = "https://tranquil-rex-******************"

# Parametros da requisição
params = {
    "nome": nome_completo.replace(" ", ""),
    "email": email,
    "cpf": cpf
}

#Fazendo POST
response = requests.post(url, params=params)

if response.status_code == 200:
    
    data = response.json()
    
    codigo_hash = data.get("codigoHash")
    pergunta = data.get("pergunta")

    #Saida de dados
    print("Código Hash:", codigo_hash)
    print("Pergunta:", pergunta)

    # Aqui você pode inserir a resposta à pergunta
    resposta = input("Sua resposta: ")

else:
    print("Erro na requisição:", response.status_code, response.text)

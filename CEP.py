# o programa pede um cep para o usuario e fornece o endereço equivalente
# acessa uma API

import requests 
#aceita requisições via internet

cep = input ("Digite o CEP (sem traços): ")

resposta = requests.get( "https://viacep.com.br/ws/%s/json/" %(cep) )
# envia o cep para a API viacep

if resposta.status_code != 200 : 
  print("Erro no acesso a API viacep!")
# no codigo 200 o acesso é feito com sucesso
else : 
  dados = resposta.json()
  print ('dados: ', dados)
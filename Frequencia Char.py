# função que recebe uma string e conta a frequência que os caracteres aparecem, retornando em dicionario
#considere maiusculos e minusculos como equivalentes

def contaCaracteres (texto) :
  textoMin = texto.lower ()

  freqs = {}  #criando um dicionario
  # ou => freqs = dics ()

  for c in textoMin :
    if c not in freqs :
      freqs [c] = 0
      
    freqs [c] += 1

  return freqs 

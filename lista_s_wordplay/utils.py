def has_no_caractere(palavra, caractere):

    for c in palavra:
        if c == caractere:
            return False
        
    return True


def avoids(palavra, letras_proibidas):

    for letra in letras_proibidas:
        if letra in palavra:
            return False
        
    return True

def contem_letra(palavra, letra):
   
   if letra in palavra:
      return True


def uses_only(palavra, letras_permitidas): #err0
   
   for letra in letras_permitidas:
        if not contem_letra(palavra, letra):
           
    
        return True

   

def to_lower(text):
  new_text = ''
  for char in text:
    if is_upper_letter(char):
      code = ord(char)
      new_code = code + 32
      lower_char = chr(new_code)
      new_text += lower_char
    else:
      new_text += char

  return new_text


def is_upper_letter(char):
  return ord(char) >= 65 and ord(char) <= 90
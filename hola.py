import re

texto = " un texto      que  es       mas  largo"
palabras = re.sub(r'\s+', ' ', texto).strip().split(' ')

n = len(palabras)

print("Número de palabras:", n)

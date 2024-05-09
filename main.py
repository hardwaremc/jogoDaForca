palavra='python'

letras_usuario = []

chances = 5

ganhou = False

while True:
  for letra in palavra:
      if letra.lower() in letras_usuario:
        print(letra, end=" ")
      else:
        print("_", end=" ")
  print(f"VocÊ tem {chances} chances")

  tentativa = input("Chute uma letra: ")

  letras_usuario.append(tentativa.lower())

  if tentativa.lower() not in palavra.lower():
    chances -= 1

  ganhou = True

  for letra in palavra:
    if letra.lower() not in letras_usuario:
      ganhou = False

  if tentativa == 0 or ganhou:
      break


palavra = "gato"  # Palavra secreta
progresso = ["_"] * len(palavra)  # Estado atual da palavra
erros = []
tentativas = 5

while tentativas > 0 and "_" in progresso:
    letra = input("Digite uma letra: ").lower()

    acerto = processar_letra(letra, palavra, progresso, erros)
    if not acerto:
        tentativas -= 1

# Mostra resultado final
if "_" not in progresso:
    print("Parabéns! Você venceu. Palavra:", palavra)
else:
    print("Você perdeu! A palavra era:", palavra)
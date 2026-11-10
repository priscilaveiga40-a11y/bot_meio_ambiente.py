perguntas = [
    ("Qual cor de lixeira é usada para PAPEL? (A) Azul  (B) Vermelho", "A", "Azul é para papel e Vermelho para plástico."),
    ("O que significa os 3 Rs? (A) Reciclar, Reflorestar, Renovar  (B) Reduzir, Reutilizar, Reciclar", "B", "Primeiro reduzimos o lixo, depois reutilizamos e por fim reciclamos."),
    ("Qual o principal gás do efeito estufa? (A) Oxigênio  (B) Gás Carbônico (CO2)", "B", "O CO2 retém o calor na atmosfera e aquece o planeta.")
]

pontos = 0
print("--- QUIZ AMBIENTAL ---")

for p, correta, dica in perguntas:
    resp = input(f"\n{p}\nResposta: ").strip().upper()
    if resp == correta:
        print("Acertou!")
        pontos += 1
    else:
        print(f"Errou! A certa era {correta}.")
    print(f"Explicação: {dica}")

print(f"\nFim! Você acertou {pontos} de {len(perguntas)}.")

bot.run("")

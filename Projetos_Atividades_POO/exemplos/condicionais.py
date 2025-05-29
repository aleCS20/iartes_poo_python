nota = float(input("Digite uma nota: "))
faltas = int(input("Quantidade de faltas: "))

if nota > 9.5 or faltas == 0:
    print(f"Aprovado por mérito com nota {nota:.2f}")
elif nota > 7.0 and faltas < 15:
    print(f"Aprovado com nota {nota:.2f}")
else:
    print(f"Reprovado com nota: {nota:.2f}")

# analisador_texto.py
# Autor: ALESSANDRO BARBOSA DE OLIVEIRA

import string

# --- Funções auxiliares de análise ---
def limpar_texto(texto):
    return texto.translate(str.maketrans('', '', string.punctuation))

def contar_palavras(texto):
    return len(texto.split())

def contar_caracteres(texto):
    return len(texto), len(texto.replace(" ", ""))

def contar_vogais(texto):
    vogais = "aeiou"
    return {v: texto.lower().count(v) for v in vogais}

def palavras_mais_longas(palavras, n=3):
    return sorted(palavras, key=len, reverse=True)[:n]

def tem_numeros(texto):
    return any(char.isdigit() for char in texto)

def exibir_transformacoes(texto):
    print("Texto em maiúsculas:", texto.upper())
    print("Texto em minúsculas:", texto.lower())
    print("Texto capitalizado:", texto.capitalize())

def exibir_analise(texto_original):
    texto_limpo = limpar_texto(texto_original)
    palavras = texto_limpo.split()

    num_palavras = contar_palavras(texto_limpo)
    num_com_espaco, num_sem_espaco = contar_caracteres(texto_original)
    frequencias = contar_vogais(texto_original)
    maiores_palavras = palavras_mais_longas(palavras)

    # Condicional para "Texto muito curto"
    if num_palavras < 10:
        print("** Texto muito curto **")

    # Condicional para "Texto contém dados mistos"
    if tem_numeros(texto_original):
        print("** Texto contém dados mistos **")

    # Exibir apenas os dados pertinentes
    if texto_original:
        print("Texto em maiúsculas:", texto_original.upper())
        print("Texto em minúsculas:", texto_original.lower())
        print("Texto capitalizado:", texto_original.capitalize())

    print("Número de palavras:", num_palavras)
    print("Número de caracteres (com espaços):", num_com_espaco)
    print("Número de caracteres (sem espaços):", num_sem_espaco)

    print("Frequência das vogais:")
    for vogal in "aeiou":
        print(f"  {vogal}: {frequencias[vogal]}")

    if maiores_palavras:
        print("3 palavras mais longas:", ", ".join(maiores_palavras))

# --- Interface do usuário ---
def exibir_menu():
    print("\nMenu:")
    print("1 - Analisar novo texto")
    print("2 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            texto = input("\nDigite o texto a ser analisado:\n")
            print("\n--- Estatísticas do Texto ---")
            exibir_analise(texto)
        elif opcao == '2':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início da execução
if __name__ == "__main__":
    main()


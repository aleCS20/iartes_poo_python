# analisador_texto.py
# Autor: ALESSANDRO BARBOSA DE OLIVEIRA

import string

## ================ fazer limpeza da frase (sem pontuação) ========================== ##
def limpar_frase(frase):
    return frase.translate(str.maketrans('', '', string.punctuation))

## =================== contar as vogais da frase ==================================== ##
def contar_vogais_frase(frase):
    frequencia = {}
    vogais = "aeiou"

    frase = frase.lower()

    for vogal in vogais:
        frequencia[vogal] = frase.count(vogal)

    return frequencia

## =================== trecho de transformação da frase ============================= ##
def transformar_frase_em_maiusculas(frase):
    print("Texto em maiúsculas: ", frase.upper())

def transformar_frase_em_minusculas(frase):
    print("Texto em minúsculas: ", frase.lower())

def transformar_frase_em_capitalizado(frase):
    print("Texto em capitalizado: ", frase.capitalize())

## ==================== trecho de tratativas de palavras da frase ====================== ##
def contar_palavras_frase(frase):
    frase_so_palavras = limpar_frase(frase)
    palavras = frase_so_palavras.split()
    return len(palavras), palavras

def contar_caracteres_frase_com_espaco(frase):
    total_caracteres_com_espaco = frase
    return len(total_caracteres_com_espaco)

def contar_caracteres_frase_sem_espaco(frase):
    total_caracteres_sem_espaco = frase
    return len(total_caracteres_sem_espaco.replace(" ", ""))

def contar_maiores_palavras(lista_palavras, top=3):
    if not lista_palavras:
        return []
    palavras_em_ordem = sorted(lista_palavras, key=len, reverse=True)
    maiores_palavras = palavras_em_ordem[:top]
    return maiores_palavras

def contar_numeros_frase(frase):
    for char in frase:
        if char.isdigit():
            return True
    return False

## ==================== analisar frase digitada =================================== ##
def analisar_frase(frase):
    numero_palavras, lista_palavras = contar_palavras_frase(frase)
    numero_caracteres_com_espacos = contar_caracteres_frase_com_espaco(frase)
    numero_caracteres_sem_espacos = contar_caracteres_frase_sem_espaco(frase)
    frequencia_vogais = contar_vogais_frase(frase)
    palavras_maiores = contar_maiores_palavras(lista_palavras)

    exibir_resultados_frase(frase, numero_palavras, numero_caracteres_com_espacos, 
                            numero_caracteres_sem_espacos, frequencia_vogais, palavras_maiores)
    
    if numero_palavras < 10:
        print("Aviso: Texto muito curto")

    if contar_numeros_frase(frase):
        print("Aviso: Texto contém dados mistos")
    
## ==================== exibir resultados da frase =================================== ##
def exibir_resultados_frase(frase, numero_palavras, numero_caracteres, numero_caracteres_sem_espaco, 
                            frequencia_vogais, palavras_maiores):
    transformar_frase_em_maiusculas(frase)
    transformar_frase_em_minusculas(frase)
    transformar_frase_em_capitalizado(frase)

    print("Número de palavras: ", numero_palavras)
    print("Número total de caracteres (com espaços): ", numero_caracteres)
    print("Número total de caracteres (sem espaços): ", numero_caracteres_sem_espaco)

    freq_formatada = ", ".join([f"{vogal}={frequencia_vogais[vogal]}" for vogal in 'aeiou'])
    print("Frequência das vogais: ", freq_formatada)
    print("As 3 palavras maiores são: ", ", ".join(palavras_maiores))

## ==================== Menu de controle do usuário ================================= ##
def exibir_menu():
    print("\n ****************** MENU ******************* ")
    print("1 - Deseja analisar um novo texto? ")
    print("2 - Sair")

## ======================== Programa principal ===================================== ##
def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha um opção conforme acima: "))
        if opcao == 1:
            frase = input("Digite sua frase: ")
            print("\n *********************** Resultados *********************** ")
            analisar_frase(frase)
            print("\n *************************** Fim ************************** ")
        elif opcao == 2:
            print("O programa será encerrado ... ")
            break
        else:
            print("Opção inválida! Digite novamente ")

if __name__ == "__main__":
    main()

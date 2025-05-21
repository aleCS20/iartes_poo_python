# analisador_texto.py
# Autor: ALESSANDRO BARBOSA DE OLIVEIRA

import string

## ==================== fazer limpeza da frase (sem pontuação) ========================== ##
## método para remover a pontuação do texto
def limpar_frase(frase):
    return frase.translate(str.maketrans('', '', string.punctuation))

## ===================== contar as vogais da frase ===================================== ##
## método para contaa a frequência de cada vogal na frase
def contar_vogais_frase(frase):
    ## dicionário para armazenar a vogal encontrada na frase
    frequencia = {}
    vogais = "aeiou"

    frase = frase.lower()

    ##fazendo varredura no dicionário e armazendo as vogais e sua frequência
    for vogal in vogais:
        frequencia[vogal] = frase.count(vogal)

    return frequencia

## ===================== trecho de transformação da frase ============================== ##
## método para transformar a frase em maiúsculas
def transformar_frase_em_maiusculas(frase):
    print("Texto em maiúsculas: ", frase.upper())

## método para transformar a frase em minúsculas
def transformar_frase_em_minusculas(frase):
    print("Texto em minúsculas: ", frase.lower())

## método para transformar a primeira palavra em capitular
def transformar_frase_em_capitalizado(frase):
    print("Texto em capitalizado: ", frase.capitalize())

## ==================== trecho de tratativas de palavras da frase ====================== ##
## método para contar o total de palavras da frase
def contar_palavras_frase(frase):
    frase_so_palavras = limpar_frase(frase)
    palavras = frase_so_palavras.split()
    return len(palavras), palavras

## método para contar o total de caracteres da frase - incluíndo os espaços
def contar_caracteres_frase_com_espaco(frase):
    total_caracteres_com_espaco = frase
    return len(total_caracteres_com_espaco)

## método para contar o total de caracteres da frase - sem incluir os espaços
def contar_caracteres_frase_sem_espaco(frase):
    total_caracteres_sem_espaco = frase
    return len(total_caracteres_sem_espaco.replace(" ", ""))

## método para mostrar e retornar as três palavras mais longas da frase 
def contar_maiores_palavras(lista_palavras, top=3):
    if not lista_palavras:
        return []
    palavras_em_ordem = sorted(lista_palavras, key=len, reverse=True)
    maiores_palavras = palavras_em_ordem[:top]
    return maiores_palavras

## método para verificar a existência de numéros na frase
def contar_numeros_frase(frase):
    for char in frase:
        if char.isdigit():
            return True
    return False

## ==================== analisar frase digitada =================================== ##
## método completo com chamadas para os métodos para analisar a frase digitada
def analisar_frase(frase):
    numero_palavras, lista_palavras = contar_palavras_frase(frase)
    numero_caracteres_com_espacos = contar_caracteres_frase_com_espaco(frase)
    numero_caracteres_sem_espacos = contar_caracteres_frase_sem_espaco(frase)
    frequencia_vogais = contar_vogais_frase(frase)
    palavras_maiores = contar_maiores_palavras(lista_palavras)

    ## chamada do método para exibir os resultados das analises e tratamentos
    exibir_resultados_frase(frase, numero_palavras, numero_caracteres_com_espacos, 
                            numero_caracteres_sem_espacos, frequencia_vogais, palavras_maiores)
    
    # Estrutura de decisão if para mensagem com quantitativo de palavras < 10
    if numero_palavras < 10:
        print("Aviso: Texto muito curto")

    # Estrutura de decisão if para mensagem cuja frase contém palavras e números
    if contar_numeros_frase(frase):
        print("Aviso: Texto contém dados mistos")
    
## ==================== exibir resultados da frase =================================== ##
## método para fins de exibição dos resultados
def exibir_resultados_frase(frase, numero_palavras, numero_caracteres, numero_caracteres_sem_espaco, 
                            frequencia_vogais, palavras_maiores):
    ## chamada de métodos para transformação das palavras da frase e mostra-los
    transformar_frase_em_maiusculas(frase)
    transformar_frase_em_minusculas(frase)
    transformar_frase_em_capitalizado(frase)

    ## impressão dos resultados da frase - tratamentos (quantitativos e caracteres)
    print("Número de palavras: ", numero_palavras)
    print("Número total de caracteres (com espaços): ", numero_caracteres)
    print("Número total de caracteres (sem espaços): ", numero_caracteres_sem_espaco)

    ## impressão dos resultados da frase - vogais e maiores palavras
    freq_formatada = ", ".join([f"{vogal}={frequencia_vogais[vogal]}" for vogal in 'aeiou'])
    print("Frequência das vogais: ", freq_formatada)
    print("As 3 palavras maiores são: ", ", ".join(palavras_maiores))

## ==================== Menu de controle do usuário ================================= ##
## método apenas para exibir o menu de controle ao usuário
def exibir_menu():
    print("\n ****************** MENU ******************* ")
    print("1 - Deseja analisar um novo texto? ")
    print("2 - Sair")

## ======================== Programa principal ===================================== ##
def main():
    while True:
        exibir_menu()
        ## escolha uma das opções conforme o menu mostra
        opcao = int(input("Escolha um opção conforme acima: "))
        if opcao == 1:
            ## entrada da frase pelo usuário
            frase = input("Digite sua frase: ")
            print("\n *********************** Resultados *********************** ")
            ## chamada do método principal que irá analisar e tratar a frase
            analisar_frase(frase)
            print("\n *************************** Fim ************************** ")
        elif opcao == 2:
            print("O programa será encerrado ... \n")
            break
        else:
            print("Opção inválida! Digite novamente ! \n")

if __name__ == "__main__":
    main()

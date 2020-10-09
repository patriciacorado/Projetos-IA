from fuzzywuzzy import process

def identificaCorrespondencia():
    #faz uma lista de frases
    dicionario = ["UMA COISA É UMA COISA", "OUTRA COISA É OUTRA COISA", "e ASSIM a vida seguE"]
    #verifica a frase inserida de acordo com a lista e define a sua correspondencia e o nivel de correspondencia
    r = process.extract("não é nada nada", dicionario, limit=2)
    #imprime a frase correspondente e o nível de correspondencia
    print (r)
identificaCorrespondencia()
import nltk
def lerArquivo(): 
    #cria uma string
    s = "I am so confuse with this library"
    #faz o reconhecimento da string e divide cada simbolos(tokens)
    tokens = nltk.word_tokenize(s)
    #exibe os simbolos
    print (tokens)
    #etiqueta os tokens de acordo sua classe gramatical
    tagged = nltk.pos_tag(tokens)
    #imprime os tokens etiquetados
    print (tagged[0:6])
lerArquivo()

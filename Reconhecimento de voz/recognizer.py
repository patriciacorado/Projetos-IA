import speech_recognition as sr

def reconhecedor():
    rec = sr.Recognizer()
    condicao = False;
    #trata a funcao Microphone da biblioteca como o recurso de áudio
    with sr.Microphone() as mic:
        #adapta-se para distinguir o barulho do ambiente da fala em 2 segundos
        rec.adjust_for_ambient_noise(mic, duration=2)
    
        while(condicao == False):
            print("Poderia falar algo?")    
            #captura a entrada do microfone, pode esperar até 5 segundos para a entrada de audio
            microfone = rec.listen(mic, timeout=5) 
            try :
                #faz o reconhecimento da fala usando a entrada do microfone e procurando no dicionário em pt-br
                transcricao = rec.recognize_google(microfone, language="pt-br") 
                condicao = True
                print("Reconheci sua voz, você falou: " + transcricao)
            except :
                print("Não entendi")
reconhecedor()
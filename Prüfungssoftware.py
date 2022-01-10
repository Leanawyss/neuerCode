i=0
frage=input("Wer ist der Präsident von der USA?")
while i<4: #Wiederholt das Programm bis zu drei mal.
    
    if frage == "Joe Biden": #Sorgt dafür, wenn die Frage richtig beantwortet wird, dass es aufhört.
        print ("Gratulation!")
        i=i+10
#        break
    else: #Wenn die Frage nicht richtig beantwortet wird, wird die Frage noch einmal gestellt und es steht wie viele Versuche man noch hat.
        print ("Noch " + str(3-i) +" Versuche") 
        i=i+1
        frage=input("Wer ist der Präsident von der USA?")
        print("Prüfung leider nicht bestanden")


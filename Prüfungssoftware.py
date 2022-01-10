i=0
frage=input("Wer ist der Präsident von der USA?")
while i<4:
    
    if frage == "Joe Biden":
        print ("Gratulation!")
        i=i+10
#        break
    else:
        print ("Noch " + str(3-i) +" Versuche") 
        i=i+1
        frage=input("Wer ist der Präsident von der USA?")
        print("Prüfung leider nicht bestanden")


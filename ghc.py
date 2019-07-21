import os
import speech_recognition as sr
d={12:["happy",0],23:["coffee",0],34:["bike",0]}
party={"Neha":0,"Navya":0}
vote=[0]*10
while(True):
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            os.system("espeak 'Say your identity number'")
            print("Say your identity number")
            audio1=r.listen(source)
        print(r.recognize_google(audio1))
        for k in d.keys():
            if(str(k)==r.recognize_google(audio1)):
                if(d[k][1]==1):
                    print("Voted already!")
                    os.system("espeak 'Voted already'")
                    break
                p=sr.Recognizer()
                with sr.Microphone() as source:
                    os.system("espeak 'Say your secret code'")
                    print("Say your secret code")
                    audio2=p.listen(source)
                print(p.recognize_google(audio2))
                if(d[k][0]==p.recognize_google(audio2)):	
                    s=sr.Recognizer()
                    with sr.Microphone() as source:
                        os.system("espeak 'Say your party name'")
                        print("Say your party name")
                        audio3=r.listen(source)
                    print(s.recognize_google(audio3))
                    for i in party:
                        if(i==s.recognize_google(audio3)):
                            party[i]=party[i]+1
                            print("Voted Successfully")
                            print(party)
                            os.system("espeak 'Voted Successfully'")
                            d[k][1]=1
                            break
                    break
                else:
                    count=0
                    while(count<=1):
                        print("Secret code mismatch")
                        os.system("espeak 'Secret code mismatch'")
                        os.system("espeak 'Try Again'")
                        print("Try Again")
                        l=sr.Recognizer()
                        with sr.Microphone() as source:
                            audio6=l.listen(source)
                        print(l.recognize_google(audio6))
                        if(d[k][0]!=l.recognize_google(audio6)):
                            count=count+1
                            continue
                        else:
                            q=sr.Recognizer()
                            with sr.Microphone() as source:
                                os.system("espeak 'Say your party name'")
                                print("Say your party name")
                                audio4=q.listen(source)
                            print(q.recognize_google(audio4))
                            for i in party:
                                if(i==q.recognize_google(audio4)):
                                    party[i]=party[i]+1
                                    print("Voted Successfully")
                                    os.system("espeak 'Voted Successfully'")
                                    print(party)
                                    d[k][1]=1
                                    break
                            break
                    if(count==2):
                        os.system("espeak 'Alert Invalid Voter'")
                        print("Invalid voter")
                    break
        else:
            print("Voter doesn't exist!!")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
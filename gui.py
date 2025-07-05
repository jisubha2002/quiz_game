'''import tkinter
import speedtest
def speed():

  Sp= speedtest.Speedtest()
  Sp.get_servers()
  down=str(round(Sp.download()/(10**6),3))+"mbps"
  up =str(round(Sp.download()/(10**6),3))+"mbps"

  lab_down.config(text=down)
  lab_up.config(text=up)

m = tkinter.Tk()
m.title("internet speed test")
m.geometry("500x500")
m.config(bg="Blue")
lab =tkinter.Label(m,text ="internet speed test",font=("Arial",30,"bold"),bg="Blue")
lab.place(x=60,y=40,height=50,width=380)

lab =tkinter.Label(m,text ="download speed",font=("Arial",30,"bold"))
lab.place(x=60,y=120,height=50,width=380)

lab_down =tkinter.Label(m,text ="00",font=("Arial",30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab =tkinter.Label(m,text ="Uploading speed",font=("Arial",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up=tkinter.Label(m,text ="00",font=("Arial",30,"bold"))
lab_up.place(x=60,y=350,height=50,width=380)

button =tkinter.Button(m,text="cheak speed",font=("Arial",30,"bold"),relief="raised",command = speed)
button.place(x=60,y=440,height=50,width=380)





m.mainloop()
'''

'''import random
import string
n=int(input("put the length of password:"))
s=string.ascii_lowercase + string.ascii_uppercase +string.digits 
print(s)
passwd ="".join(random.choice(s) for i in range(n))
print("password is ", passwd)
'''
'''import speech_recognition as sr
r= sr.Recognizer()
with  sr.Microphone() as  s:
    print("speeaking")
    audio = r.listen(s)
    t=r.recognize_google(audio)
    print("you said ",t)

    '''
import tkinter
import speedtest

def speed():
    Sp = speedtest.Speedtest()
    Sp.get_servers()
    down = str(round(Sp.download() / (10**6), 3)) + " mbps"
    up = str(round(Sp.upload() / (10**6), 3)) + " mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

m = tkinter.Tk()
m.title("internet speed test")
m.geometry("500x500")
m.config(bg="Blue")

lab_title = tkinter.Label(m, text="internet speed test", font=("Arial", 30, "bold"), bg="Blue")
lab_title.place(x=60, y=40, height=50, width=380)

lab_down_text = tkinter.Label(m, text="download speed", font=("Arial", 30, "bold"))
lab_down_text.place(x=60, y=120, height=50, width=380)

lab_down = tkinter.Label(m, text="00", font=("Arial", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab_up_text = tkinter.Label(m, text="Uploading speed", font=("Arial", 30, "bold"))
lab_up_text.place(x=60, y=290, height=50, width=380)

lab_up = tkinter.Label(m, text="00", font=("Arial", 30, "bold"))
lab_up.place(x=60, y=350, height=50, width=380)

button = tkinter.Button(m, text="cheak speed", font=("Arial", 30, "bold"), relief="raised", command=speed)
button.place(x=60, y=440, height=50, width=380)

m.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def lisa():
    hulk.add(hulk1.get())
    print(hulk)

def järgmine():
    global hulk
    hulgad.append(hulk)
    hulk = set()
    print(hulgad)
    global harv
    harv += 1

def kuvaarvutus():
    evalsõne = ""
    for sümbol in arvut.get():
        try:
            int(sümbol)
        except:
            evalsõne += sümbol
            continue
        else:
            evalsõne += "hulgad[" + str(int(sümbol)-1) + "]"
            continue
    vastus = eval(evalsõne)
    messagebox.showinfo(message="Vastus on " + str(vastus))

def minuhulgad():
    minuraam = Tk()
    minuraam.title("Hulga leidmine")
    minuraam.geometry("300x100")
    mitu = ttk.Label(minuraam, text="Sul on " + str(harv) + " hulka")
    mitu.place(x=75, y=10)
    global mitmes
    mitmes = ttk.Entry(minuraam)
    mitmes.place(x=200, y=35, width=25)
    küsimus = ttk.Label(minuraam, text="Mitmendat hulka soovid näha?")
    küsimus.place(x=10, y = 35)
    global vaatahulk
    vaatahulk = ttk.Button(minuraam, text="Vaata", command=vaatahulk)
    vaatahulk.place(x=150, y=60, width=100)
    
def vaatahulk():
    näehulk = hulgad[int(mitmes.get()) - 1]
    messagebox.showinfo(message=str(näehulk))

def arvutama():   #Kustutab akna ja kuvab uue akna. Kõik uue akna tegevused on funktsiooni sees
    arvutaraam = Tk()
    arvutaraam.title("Lausearvutused")
    arvutaraam.geometry("500x600")
    raam.destroy()
    arvuinfo = ttk.Label(arvutaraam, text="Lausearvutuste kirjutamisel kujuta hulgad numbritega\nalustades 1-st. (Näiteks 1&2)\n")
    arvuinfo.place(x=20,y=5)
    väli = ttk.Label(arvutaraam, text="Sisesta hulgatehe")
    väli.place(x=20, y=55)
    info = ttk.Label(arvutaraam, text=""" KASUTA JÄRGMISEID SÜMBOLEID:
•in on hulga element
• not in ei ole hulga element
• == on võrdne
• != mittevõrdne
• < on range alamhulk
• <= on alamhulk
• > on range ülemhulk
• >= on ülemhulk
• & ühisosa
• | ühend
• - hulkade vahe
• ^ sümmeetriline vahe""")
    info.place(x=10,y=150)
    global arvut
    arvut = ttk.Entry(arvutaraam)
    arvut.place(x=200, y=55, width=150)
    lausearvutus = ttk.Button(arvutaraam, text="Arvuta", command=kuvaarvutus)
    lausearvutus.place(x=150, y=100, width=100)
    global minuhulgad
    minuhulgad = ttk.Button(arvutaraam, text="Minu hulgad", command=minuhulgad)
    minuhulgad.place(x= 30, y=100, width=100)
   
hulk = set()
raam = Tk()
raam.title("Hulkade sisestamine")
raam.geometry("275x125")

harv = 0
silt = ttk.Label(raam, text="Sisesta hulga element")
silt.place(x=5, y=5)

hulk1 = ttk.Entry(raam)
hulk1.place(x=200, y=5, width=50)

hulgad = []
nupp = ttk.Button(raam, text="Lisa", command=lisa)
nupp.place(x=75, y=40, width=50)

jarg = ttk.Button(raam, text="Uus hulk", command=järgmine)
jarg.place(x=125, y=40, width=100)

arvuta = ttk.Button(raam, text="Arvutama", command=arvutama)
arvuta.place(x=100, y=75, width=100)

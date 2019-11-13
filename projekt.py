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

def arvutama():   #Kustutab akna ja kuvab uue akna. Kõik uue akna tegevused on funktsiooni sees
    arvutaraam = Tk()
    arvutaraam.title("Lausearvutused")
    arvutaraam.geometry("400x400")
    raam.destroy()
    väli = ttk.Label(arvutaraam, text="Sisesta hulga element")
    väli.place(x=5, y=5)
    arvut = ttk.Entry(arvutaraam)
    arvut.place(x=70, y=5, width=150)
    evalsõne = ""
    '''    #Kood mis tekitab sõne mida hiljem evaluate'ib. On vaja veel nupuga kutsuda. Ehk sobib paremini eraldi funktsioonina
    for sümbol in arvut:
        try:
            int(sümbol)
        except:
            evalsõne += sümbol
            continue
        else:
            evalsõne = "hulgad[" + str(sümbol-1) + "]"
    vastus = eval(evalsõne)
    print(evalsõne)
    print(vastus)
    '''

hulk = set()
raam = Tk()
raam.title("Hulkade sisestamine")
raam.geometry("300x100")

silt = ttk.Label(raam, text="Sisesta hulga element")
silt.place(x=5, y=5)

hulk1 = ttk.Entry(raam)
hulk1.place(x=70, y=5, width=150)

hulgad = []
nupp = ttk.Button(raam, text="Lisa", command=lisa)
nupp.place(x=70, y=40, width=50)

jarg = ttk.Button(raam, text="Järgmine", command=järgmine)
jarg.place(x=150, y=40, width=100)

arvuta = ttk.Button(raam, text="Arvutama", command=arvutama)
arvuta.place(x=100, y=75, width=75)
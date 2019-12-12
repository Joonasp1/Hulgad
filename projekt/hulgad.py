from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def joonista_venn():
    if not (len(vhulgad)==2 or len(vhulgad)==3):
        messagebox.showinfo(message="Sisesta kaks või kolm hulka")
        return
    if len(vhulgad) == 2:
        venn = venn2([vhulgad[0],vhulgad[1]], ('Esimene hulk', 'Teine hulk'))
        try:
            venn.get_label_by_id('100').set_text('\n'.join(vhulgad[0]-vhulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(vhulgad[0]&vhulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(vhulgad[1]-vhulgad[0]))
        except:
            pass
        
    else:    
        venn=venn3([vhulgad[0], vhulgad[1], vhulgad[2]], ('Esimene hulk', 'Teine hulk', 'Kolmas hulk'))
        try:
            venn.get_label_by_id('111').set_text('\n'.join(vhulgad[0]&vhulgad[1]&vhulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('100').set_text('\n'.join(vhulgad[0]-vhulgad[1]-vhulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(vhulgad[0]&vhulgad[1]-vhulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(vhulgad[1]-vhulgad[2]-vhulgad[0]))
        except:
            pass
        try:
            venn.get_label_by_id('101').set_text('\n'.join(vhulgad[0]&vhulgad[2]-vhulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('011').set_text('\n'.join(vhulgad[1]&vhulgad[2]-vhulgad[0]))
        except:
            pass
        try:
            venn.get_label_by_id('001').set_text('\n'.join(vhulgad[2]-vhulgad[1]-vhulgad[0]))
        except:
            pass
    
    plt.show()

def vlisa():
    vhulk.add(vhulk1.get())
    print(vhulk)
    hetkevhulk["text"]="Praegune hulk on " + str(vhulk)

def vjärgmine():
    if len(vhulgad) == 3:
        messagebox.showinfo(message="See programm ei toeta üle 3 hulga Venni diagramme")
        Venn()
        return
    else:
        global vhulk
        vhulgad.append(vhulk)
        sinuvhulgad["text"] += "\n" + str(len(vhulgad)) + ". " + str(vhulk)
        vhulk = set()
        print(vhulgad)
        hetkevhulk["text"]="Praegune hulk on tühi" 

def Venn():
    kraam.destroy()
    global vhulk
    vhulk = set()
    vraam = Tk()
    vraam.title("Hulkade sisestamine")
    vraam.geometry("300x200")

    vsilt = ttk.Label(vraam, text="Sisesta hulga element")
    vsilt.place(x=5, y=5)

    global vhulk1
    vhulk1 = ttk.Entry(vraam)
    vhulk1.place(x=200, y=5, width=50)

    global vhulgad
    vhulgad = []
    nupp = ttk.Button(vraam, text="Lisa element", command=vlisa)
    nupp.place(x=25, y=40, width=125)

    jarg = ttk.Button(vraam, text="Salvesta hulk", command=vjärgmine)
    jarg.place(x=150, y=40, width=125)

    kuva = ttk.Button(vraam, text="Kuva diagramm", command=joonista_venn)
    kuva.place(x=100, y=75, width=150)
    
    global hetkevhulk
    hetkevhulk = ttk.Label(vraam, text="Praegune hulk on tühi")
    hetkevhulk.place(x=30,y=100)
    
    global sinuvhulgad
    sinuvhulgad = ttk.Label(vraam, text="Sinu hulgad on: ")
    sinuvhulgad.place(x=50, y=125)
    
def lisa():
    hulk.add(hulk1.get())
    print(hulk)
    hetkehulk["text"]="Praegune hulk on " + str(hulk)
    
def järgmine():
    global hulk
    global harv
    harv += 1
    sinuhulgad["text"] += "\n" + str(harv) + ". " + str(hulk)
    hulgad.append(hulk)
    hulk = set()
    print(hulgad)
    hetkehulk["text"]="Praegune hulk on tühi" 

def kuvaarvutus():
    evalsõne = ""
    arvutused["text"] += "\n" + str(arvut.get())
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
    arvutused["text"] += " = " + str(vastus)
    
def minuhulgad():
    minuraam = Tk()
    minuraam.title("Minu hulgad")
    minuraam.geometry("100x150")
    hulgalist = ttk.Label(minuraam, text="Sinu hulgad on:")
    hulgalist.place(x=20,y=10)
    for i in range(len(hulgad)):
        hulgalist["text"]+="\n" + str(i+1) + ". " + str(hulgad[i])
    

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
    minuhulgad.place(x= 30, y=100, width=115)
    
    global arvutused
    arvutused = ttk.Label(arvutaraam, text="Arvutused: ")
    arvutused.place(x = 275, y = 100)
    
def kustutahulgad():
    hulgad = []
    hulk = set()
    harv = 0
    messagebox.showinfo(message="Hulgad on kustutatud. Saad alustada nullist")

def lausearvutus():
    kraam.destroy()
    global raam
    raam = Tk()
    raam.title("Hulkade sisestamine")
    raam.geometry("300x250")
    global hulk
    hulk = set()
    silt = ttk.Label(raam, text="Sisesta hulga element")
    silt.place(x=5, y=5)
    global harv
    harv = 0

    global hulk1
    hulk1 = ttk.Entry(raam)
    hulk1.place(x=200, y=5, width=50)

    global hulgad
    hulgad = []
    nupp = ttk.Button(raam, text="Lisa element", command=lisa)
    nupp.place(x=25, y=40, width=125)

    jarg = ttk.Button(raam, text="Salvesta hulk", command=järgmine)
    jarg.place(x=150, y=40, width=125)
    
    arvuta = ttk.Button(raam, text="Arvutama", command=arvutama)
    arvuta.place(x=100, y=75, width=100)
    
    global hetkehulk
    hetkehulk = ttk.Label(raam, text="Praegune hulk on tühi")
    hetkehulk.place(x=30,y=100)
    
    global sinuhulgad
    sinuhulgad = ttk.Label(raam, text="Sinu hulgad on: ")
    sinuhulgad.place(x=50, y=125)


global kraam
kraam = Tk()
kraam.title("Valik")
kraam.geometry("400x200")

vali = ttk.Label(kraam, text="Vali alamprogramm")
vali.config(font=("Times new roman",18))
vali.place(x=60,y=10)

lausevalik = ttk.Button(kraam, text="Lausearvutused", width=15, command=lausearvutus)
lausevalik.place(x=125,y=75)

vennvalik = ttk.Button(kraam, text="Venni diagramm", width= 15, command=Venn)
vennvalik.place(x=125,y=125)

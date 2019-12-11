from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def joonista_venn():
    if len(vhulgad) < 2:
        messagebox.showinfo(message="Sisesta vähemalt 2 hulka")
        return
    if len(vhulgad) == 2:
        venn = venn2([vhulgad[0],vhulgad[1]], ('Esimene hulk', 'Teine hulk'))
        venn.get_label_by_id('100').set_text('\n'.join(vhulgad[0]-vhulgad[1]))
        venn.get_label_by_id('110').set_text('\n'.join(vhulgad[0]&vhulgad[1]))
        venn.get_label_by_id('010').set_text('\n'.join(vhulgad[1]-vhulgad[0]))
        
    else:    
        venn=venn3([vhulgad[0], vhulgad[1], vhulgad[2]], ('Esimene hulk', 'Teine hulk', 'Kolmas hulk'))
        venn.get_label_by_id('111').set_text('\n'.join(vhulgad[0]&vhulgad[1]&vhulgad[2]))
        venn.get_label_by_id('100').set_text('\n'.join(vhulgad[0]-vhulgad[1]-vhulgad[2]))
        venn.get_label_by_id('110').set_text('\n'.join(vhulgad[0]&vhulgad[1]-vhulgad[2]))
        venn.get_label_by_id('010').set_text('\n'.join(vhulgad[1]-vhulgad[2]-vhulgad[0]))
        venn.get_label_by_id('101').set_text('\n'.join(vhulgad[0]&vhulgad[2]-vhulgad[1]))
        venn.get_label_by_id('011').set_text('\n'.join(vhulgad[1]&vhulgad[2]-vhulgad[0]))
        venn.get_label_by_id('001').set_text('\n'.join(vhulgad[2]-vhulgad[1]-vhulgad[0]))
    
    plt.show()

def vlisa():
    vhulk.add(vhulk1.get())
    print(vhulk)

def vjärgmine():
    if len(vhulgad) == 3:
        messagebox.showinfo(message="See programm ei toeta üle 3 hulga Venni diagramme")
        Venn()
        return
    else:
        global vhulk
        messagebox.showinfo(message="Lisasid hulga " + str(vhulk))
        vhulgad.append(vhulk)
        vhulk = set()
        print(vhulgad)

def Venn():
    kraam.destroy()
    global vhulk
    vhulk = set()
    vraam = Tk()
    vraam.title("Hulkade sisestamine")
    vraam.geometry("275x125")

    vsilt = ttk.Label(vraam, text="Sisesta hulga element")
    vsilt.place(x=5, y=5)

    global vhulk1
    vhulk1 = ttk.Entry(vraam)
    vhulk1.place(x=200, y=5, width=50)

    global vhulgad
    vhulgad = []
    nupp = ttk.Button(vraam, text="Lisa", command=vlisa)
    nupp.place(x=75, y=40, width=50)

    jarg = ttk.Button(vraam, text="Uus hulk", command=vjärgmine)
    jarg.place(x=125, y=40, width=100)

    kuva = ttk.Button(vraam, text="Kuva diagramm", command=joonista_venn)
    kuva.place(x=100, y=75, width=100)
    
def lisa():
    hulk.add(hulk1.get())
    print(hulk)

def järgmine():
    global hulk
    global harv
    harv += 1
    messagebox.showinfo(message="Lisasid hulga nr." + str(harv) + " : " + str(hulk))
    hulgad.append(hulk)
    hulk = set()
    print(hulgad)

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

def lausearvutus():
    kraam.destroy()
    global raam
    raam = Tk()
    raam.title("Hulkade sisestamine")
    raam.geometry("275x125")
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
    nupp = ttk.Button(raam, text="Lisa", command=lisa)
    nupp.place(x=75, y=40, width=50)

    jarg = ttk.Button(raam, text="Uus hulk", command=järgmine)
    jarg.place(x=125, y=40, width=100)

    arvuta = ttk.Button(raam, text="Arvutama", command=arvutama)
    arvuta.place(x=100, y=75, width=100)


global kraam
kraam = Tk()
kraam.title("Valik")
kraam.geometry("300x200")

vali = ttk.Label(kraam, text="Vali alamprogramm")
vali.config(font=("Times new roman",18))
vali.place(x=60,y=10)

lausevalik = ttk.Button(kraam, text="Lausearvutused", width=15, command=lausearvutus)
lausevalik.place(x=100,y=75)

vennvalik = ttk.Button(kraam, text="Venni diagramm", width= 15, command=Venn)
vennvalik.place(x=100,y=125)

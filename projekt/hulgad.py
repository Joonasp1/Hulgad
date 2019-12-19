from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def joonista_venn():
    if len(hulgad) < 2 :
        messagebox.showinfo(message="Sisesta kaks või kolm hulka")
        return
    elif len(hulgad) > 3:
        messagebox.showinfo(message="See programm ei toeta üle kolme hulga diagramme")
    if len(hulgad) == 2:
        venn = venn2([hulgad[0],hulgad[1]], ('Esimene hulk', 'Teine hulk'))
        try:
            venn.get_label_by_id('100').set_text('\n'.join(hulgad[0]-hulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(hulgad[0]&hulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(hulgad[1]-hulgad[0]))
        except:
            pass
        
    else:    
        venn=venn3([hulgad[0], hulgad[1], hulgad[2]], ('Esimene hulk', 'Teine hulk', 'Kolmas hulk'))
        try:
            venn.get_label_by_id('111').set_text('\n'.join(hulgad[0]&hulgad[1]&hulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('100').set_text('\n'.join(hulgad[0]-hulgad[1]-hulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(hulgad[0]&hulgad[1]-hulgad[2]))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(hulgad[1]-hulgad[2]-hulgad[0]))
        except:
            pass
        try:
            venn.get_label_by_id('101').set_text('\n'.join(hulgad[0]&hulgad[2]-hulgad[1]))
        except:
            pass
        try:
            venn.get_label_by_id('011').set_text('\n'.join(hulgad[1]&hulgad[2]-hulgad[0]))
        except:
            pass
        try:
            venn.get_label_by_id('001').set_text('\n'.join(hulgad[2]-hulgad[1]-hulgad[0]))
        except:
            pass
    
    plt.show()


    
def lisa():
    hulk.add(hulk1.get())
    print(hulk)
    hetkehulk["text"]="Praegune hulk on " + str(hulk)
    hulk1.delete(0, END)
    
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
    minuraam.geometry("200x200")
    hulgalist = ttk.Label(minuraam, text="Sinu hulgad on:")
    hulgalist.place(x=20,y=10)
    for i in range(len(hulgad)):
        hulgalist["text"]+="\n" + str(i+1) + ". " + str(hulgad[i])
    

def arvutama():   #Kustutab akna ja kuvab uue akna. Kõik uue akna tegevused on funktsiooni sees
    global arvutaraam
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
    
    tagasinupp = ttk.Button(arvutaraam, text="Tagasi (kustutab hulgad)", command=tagasi)
    tagasinupp.place(x=350,y=10)

    global arvutused
    arvutused = ttk.Label(arvutaraam, text="Arvutused: ")
    arvutused.place(x = 275, y = 100, width=150)
    
def kustutahulgad():
    global hulgad
    hulgad = []
    global hulk
    hulk = set()
    global harv
    harv = 0
    global hetkehulk
    hetkehulk["text"] = "Praegune hulk on tühi"
    global sinuhulgad
    sinuhulgad["text"] = "Sinu hulgad on:"
    messagebox.showinfo(message="Hulgad on kustutatud. Saad alustada nullist")

def tagasi():
    arvutaraam.destroy()
    global hulgad
    hulgad = []
    global hulk
    hulk = set()
    global harv
    harv = 0
    main()

def main():
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
    arvuta.place(x=25, y=75, width=100)

    vdiag = ttk.Button(raam, text="Venni diagramm", command=joonista_venn)
    vdiag.place(x=150, y=75, width=100)

    kustuta = ttk.Button(raam, text="Kustuta hulgad", command=kustutahulgad)
    kustuta.place(x=100, y=110)

    global hetkehulk
    hetkehulk = ttk.Label(raam, text="Praegune hulk on tühi")
    hetkehulk.place(x=30,y=150)

    global sinuhulgad
    sinuhulgad = ttk.Label(raam, text="Sinu hulgad on: ")
    sinuhulgad.place(x=50, y=177)

if __name__ == '__main__':
    main()
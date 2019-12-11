from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

def joonista_venn(järjend):
    try:
        Hulk3=järjend[2]
        Hulk2=järjend[1]
        Hulk1=järjend[0]
    except:
        Hulk2=järjend[1]
        Hulk1=järjend[0]
        Hulk3={""}
    if Hulk3=={""} and Hulk2!="" and Hulk1!="":
        venn = venn2([Hulk1,Hulk2], ('Esimene hulk', 'Teine hulk'))
        try:
            venn.get_label_by_id('100').set_text('\n'.join(Hulk1-Hulk2))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(Hulk1&Hulk2))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(Hulk2-Hulk1))
        except:
            pass
        
    else:    
        venn=venn3([Hulk1, Hulk2, Hulk3], ('Esimene hulk', 'Teine hulk', 'Kolmas hulk'))
        try:
            venn.get_label_by_id('111').set_text('\n'.join(Hulk1&Hulk2&Hulk3))
        except:
            pass
        try:
            venn.get_label_by_id('100').set_text('\n'.join(Hulk1-Hulk2-Hulk3))
        except:
            pass
        try:
            venn.get_label_by_id('110').set_text('\n'.join(Hulk1&Hulk2-Hulk3))
        except:
            pass
        try:
            venn.get_label_by_id('010').set_text('\n'.join(Hulk2-Hulk3-Hulk1))
        except:
            pass
        try:
            venn.get_label_by_id('101').set_text('\n'.join(Hulk1&Hulk3-Hulk2))
        except:
            pass
        try:
            venn.get_label_by_id('011').set_text('\n'.join(Hulk2&Hulk3-Hulk1))
        except:
            pass
        try:
            venn.get_label_by_id('001').set_text('\n'.join(Hulk3-Hulk2-Hulk1))
        except:
            pass
    
    plt.show()

#Testimiseks
from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

def joonista_venn(Hulk1,Hulk2,Hulk3={""}):
    if Hulk3=={""} and Hulk2!="" and Hulk1!="":
        venn = venn2([Hulk1,Hulk2], ('Esimene hulk', 'Teine hulk'))
        venn.get_label_by_id('100').set_text('\n'.join(Hulk1-Hulk2))
        venn.get_label_by_id('110').set_text('\n'.join(Hulk1&Hulk2))
        venn.get_label_by_id('010').set_text('\n'.join(Hulk2-Hulk1))
        
    else:    
        venn=venn3([Hulk1, Hulk2, Hulk3], ('Esimene hulk', 'Teine hulk', 'Kolmas hulk'))
        venn.get_label_by_id('111').set_text('\n'.join(Hulk1&Hulk2&Hulk3))
        venn.get_label_by_id('100').set_text('\n'.join(Hulk1-Hulk2-Hulk3))
        venn.get_label_by_id('110').set_text('\n'.join(Hulk1&Hulk2-Hulk3))
        venn.get_label_by_id('010').set_text('\n'.join(Hulk2-Hulk3-Hulk1))
        venn.get_label_by_id('101').set_text('\n'.join(Hulk1&Hulk3-Hulk2))
        venn.get_label_by_id('011').set_text('\n'.join(Hulk2&Hulk3-Hulk1))
        venn.get_label_by_id('001').set_text('\n'.join(Hulk3-Hulk2-Hulk1))
    
    plt.show()

#Testimiseks
"""A = {"1","2","3","4","5"}
B = {"4","5","6","7"}
C = {"1","7","9","5"}
joonista_venn(A,B,C)"""

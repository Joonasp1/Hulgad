def ühisosa(Hulkade_List):
    ühisosa=list(Hulkade_List)[0] #Võtab esimes hulga
    for h in range(len(Hulkade_List)-1): #Käib kõik ülejäänud hulgad läbi
        ühisosa=ühisosa & list(Hulkade_List)[h+1] #Teeb vastava tehte ja lisab vastuse tulemusse
    return ühisosa
def ühend(Hulkade_List):
    ühend=list(Hulkade_List)[0]
    for h in range(len(Hulkade_List)-1):
        ühend=ühend | list(Hulkade_List)[h+1]
    return ühend
def vahe(Hulkade_List):
    vahe=list(Hulkade_List)[0]
    for h in range(len(Hulkade_List)-1):
        vahe=vahe - list(Hulkade_List)[h+1]
    return vahe
def sümmeetriline_vahe(Hulkade_List):
    if Hulkade_List==[{}]:
        return {}
    return ühend(Hulkade_List)-ühisosa(Hulkade_List)
"""D=set(["a","b","c","F",10]) 
B=set(["c","F","a",10,9,"wau"])
C=set([10,"c","g","F"])
Hulkade_List=[]
print(ühend(Hulkade_List))
print(ühisosa(Hulkade_List))
print(vahe(Hulkade_List))
print(sümmeetriline_vahe(Hulkade_List))"""
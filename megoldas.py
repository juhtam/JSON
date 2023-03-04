# 1. feladat: Az átlagéletkor 15.60
# 2. feladat: A legidősebb diák neve: Tóth Géza
# 3. feladat: A kolisok nevei:
#         Nagy Zoé
#         Tóth Géza
#         Horvát Éva
# 4. feladat: A kolisok lista:
# [{'vnev': 'Nagy', 'knev': 'Zoé', 'kor': 15, 'email': 'null', 'kolis_e': True}, {'vnev': 'Tóth', 'knev': 'Géza', 'kor': 17, 'email': 'gezu@gmail.com', 'kolis_e': True}, {'vnev': 'Horvát', 'knev': 'Éva', 'kor': 15, 'email': 'horeva@moriczref.hu', 'kolis_e': True}]
"""
vnevek = []
knevek = []
korok = []
emailek = []
kolisok_e = []

with open("./adatok/diakok_adatai.txt","r",encoding="utf-8") as fm:
    fm.readline()
    for sor in fm:
        seged_lista = sor.strip().split()
        vnevek.append(seged_lista[0])
        knevek.append(seged_lista[1])
        korok.append(int(seged_lista[2]))
        emailek.append(seged_lista[3])
        kolisok_e.append(seged_lista[4]=="1")

print(vnevek)
print(knevek)
print(korok)
print(emailek)
print(kolisok_e)
"""

diakok = []
diak = {}
with open("./adatok/diakok_adatai.txt", "r", encoding="utf-8") as fm:
    fm.readline()
    for sor in fm:
        seged_lista = sor.strip().split()
        diak["vnev"] = seged_lista[0]
        diak["knev"] = seged_lista[1]
        diak["kor"] = int(seged_lista[2])
        diak["email"] = seged_lista[3]
        diak["kolis_e"] = seged_lista[4] == "1"
        diakok.append(diak)
        diak = {}
print(diakok)

# 1. feladat: Az átlagéletkor 15.60
def osszegzes(lista):
    osszeg = 0
    for diak in lista:
        osszeg += diak["kor"]
    return osszeg

osszeg = osszegzes(diakok)
darab = len(diakok)

print(f"Az átlagéletkor: {osszeg/darab:0.2f} ")

# 2. feladat: A legidősebb diák neve: Tóth Géza
def maximum_kivalasztas(lista):
    max_index = 0
    for index in range(1,len(lista)):
        if lista[max_index]["kor"] < lista[index]["kor"]:
            max_index = index
    return max_index

mi=maximum_kivalasztas(diakok)  

print(f"A legidősebb diák neve: {diakok[mi]['vnev']} {diakok[mi]['knev']}")
# 3. feladat: A kolisok nevei:
#         Nagy Zoé
#         Tóth Géza
#         Horvát Éva

print("3. feladat: A Kolisok nevei")
for diak in diakok:
    if diak['kolis_e']:
        print(f"\t{diak['vnev']} {diak['knev']}")

# 4. feladat: A kolisok lista:
# [{'vnev': 'Nagy', 'knev': 'Zoé', 'kor': 15, 'email': 'null', 'kolis_e': True}, {'vnev': 'Tóth', 'knev': 'Géza', 'kor': 17, 'email': 'gezu@gmail.com', 'kolis_e': True}, {'vnev': 'Horvát', 'knev': 'Éva', 'kor': 15, 'email': 'horeva@moriczref.hu', 'kolis_e': True}]
# kolisok=[]
# for diak in diakok:
#     if diak['kolis_e']:
#         kolisok.append(diak)
#Leképezés
kolisok=[diak for diak in diakok if diak['kolis_e']]

print("4. feladat: A kolisok listája: ")
print(kolisok)

"""
LEKÉPEZÉS
import random
szamok=[]
for _ in range(100):
    szamok.append(random.randint(1,100))
print(szamok)
paros_szamok=[szam for szam in szamok if szam%2==0 ] # Leképezés
print(paros_szamok)
"""
#5. feladat
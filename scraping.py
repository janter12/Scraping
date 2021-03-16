import requests
from bs4 import BeautifulSoup
import csv

url_page = 'https://www.lamoncloa.gob.es/gobierno/composiciondelgobierno/Paginas/index.aspx'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

# Separamos los nombres de los politicos
politicos = soup.find_all(class_="politician-name")

listanombres=[]
for valor in politicos:
    listanombres.append(valor.string)

for nombres in listanombres:
    nombres = print(nombres)
#print(nombres)

# Separamos los cargosde cada politico
puesto = soup.find_all(class_="politician-charge")

listapuesto=[]
for valor in puesto:
    listapuesto.append(valor.string)

for puestos in listapuesto:
    puestos = print(puestos)
#print(puestos)

# FECHA NACIMIENTO PRESI
url_fechanac = 'https://www.lamoncloa.gob.es/presidente/biografia/Paginas/index.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

presi = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
presi = presi.replace('\n', "")
#print(presi)


# FECHA NACIMIENTO VICEPRESI (CARMEN CALVO)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-carmencalvo.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

vicep1 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
vi1 = vicep1.replace('\n', "")
#print(vi1)

# FECHA NACIMIENTO VICEPRESI (Pablo Iglesias Turrión)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/13012020_pabloiglesias.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

vicep2 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
vi2 = vicep2.replace('\n', "")
#print(vi2)

# FECHA NACIMIENTO VICEPRESI (Nadia Calviño Santamaría)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-nadiacalvino.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

vicep3 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
vi3 = vicep3.replace('\n', "")
#print(vi3)

# FECHA NACIMIENTO VICEPRESI (Teresa Ribera Rodríguez)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-teresariberarodrig.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

vicep4 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
vi4 = vicep4.replace('\n', "")
#print(vi4)

# FECHA NACIMIENTO MINISTROS (María Aránzazu González Laya)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-aranzazugonzalez.aspx'

page2 = requests.get(url_fechanac).text
soup = BeautifulSoup(page2, "lxml")

minis1 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m1 = minis1.replace('\n', "")
#print(m1)

# FECHA NACIMIENTO MINISTROS (Juan Carlos Campo Moreno)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-juancarloscampo.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis2 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m2 = minis2.replace('\n', "")
#print(m2)


# FECHA NACIMIENTO MINISTROS (Margarita Robles Fernández)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-margaritarobles.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis3 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m3 = minis3.replace('\n', "")
#print(m3)



# FECHA NACIMIENTO MINISTROS (María Jesús Montero Cuadrado)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-mariajesusmontero.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis4 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m4 = minis4.replace('\n', "")
#print(m4)


# FECHA NACIMIENTO MINISTROS (Fernando Grande-Marlaska Gómez)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-fernandogrande.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis5 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m5 = minis5.replace('\n', "")
#print(m5)


# FECHA NACIMIENTO MINISTROS (José Luis Ábalos Meco)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-joseluisabalos.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis6 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m6 = minis6.replace('\n', "")
#print(m6)

# FECHA NACIMIENTO MINISTROS (Isabel Celaá Diéguez)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-isabelcelaadieguez.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis7 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m7 = minis7.replace('\n', "")
#print(m7)

# FECHA NACIMIENTO MINISTROS (Yolanda Díaz Pérez)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-yolandadiazperez.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis8 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m8 = minis8.replace('\n', "")
#print(m8)

# FECHA NACIMIENTO MINISTROS (Reyes Maroto Illera)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-reyesmarotoillera.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis9 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m9 = minis9.replace('\n', "")
#print(m9)

# FECHA NACIMIENTO MINISTROS (Luis Planas Puchades)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-luisplanaspuchades.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis10 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m10 = minis10.replace('\n', "")
#print(m10)

# FECHA NACIMIENTO MINISTROS (Miquel Iceta i Llorens)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/27012021-miqueliceta.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis11 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m11 = minis11.replace('\n', "")
#print(m11)

# FECHA NACIMIENTO MINISTROS (José Manuel Rodríguez Uribes)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-josemanuelrodrigue.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis12 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m12 = minis12.replace('\n', "")
#print(m12)

# FECHA NACIMIENTO MINISTROS (Carolina Darias San Sebastián)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/27012021-carolinadarias.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis13 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m13 = minis13.replace('\n', "")
#print(m13)

# FECHA NACIMIENTO MINISTROS (Pedro Duque Duque)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-pedrofranciscoduqu.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis14 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m14 = minis14.replace('\n', "")
#print(m14)

# FECHA NACIMIENTO MINISTROS (Irene Montero Gil)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-irenemariamonterog.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis15 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m15 = minis15.replace('\n', "")
#print(m15)

# FECHA NACIMIENTO MINISTROS (Alberto Garzón Espinosa)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-albertocarlosgarzo.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis16 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m16 = minis16.replace('\n', "")
#print(m16)

# FECHA NACIMIENTO MINISTROS (José Luis Escrivá Belmonte)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-joseluisescrivabel.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis17 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m17 = minis17.replace('\n', "")
#print(m17)

# FECHA NACIMIENTO MINISTROS (Manuel Castells Oliván)
url_fechanac = 'https://www.lamoncloa.gob.es/gobierno/Paginas/130120-manuelcastellsoliv.aspx'

page2 = requests.get(url_fechanac).text 
soup = BeautifulSoup(page2, "lxml")

minis18 = soup.find('div', attrs={'id': 'ctl00_PlaceHolderMain_DisplayMode_noticia_divSummary'}).getText()
m18 = minis18.replace('\n', "")
#print(m18)

# Creamos un array donde metemos las fechas y lugar de nacimiento de cada uno de ellos
listafechas = [presi, vi1, vi2, vi3, vi4, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18]
for fechas in listafechas:
    fechas = print(fechas)
#fechas



with open('politicos.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for valor in range(len(nombres)):
        writer.writerow([nombres, puestos, fechas])


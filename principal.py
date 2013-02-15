import urllib2
from xml.dom.minidom import parse

APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"

url = urllib2.urlopen("http://www.resultados-futbol.com/scripts/api/api.php?key="+APIKEY+"&format=xml&req=tables&league=1")
lista= url.read()
equipos=open("equipos","w")
equipos.write(lista)
equipos.close()

dom = parse('equipos')

nodo_equipos = dom.firstChild

equipos =[]
puntos =[]
for nodo_equipo in nodo_equipos.getElementsByTagName('table'):
    equipo= nodo_equipo.getElementsByTagName('team')[0].firstChild.data
    punto= nodo_equipo.getElementsByTagName('points')[0].firstChild.data
    equipos.append(equipo)
    puntos.append(punto)

equipos2 =[]
for i in equipos:
    sin_saltos = i.replace('\n','')
    equipos2.append(sin_saltos)

puntos2 =[]
for i in puntos:
    sin_saltos = i.replace('\n','')
    puntos2.append(sin_saltos)



for i in range(20):
    print equipos2[i], puntos2[i]



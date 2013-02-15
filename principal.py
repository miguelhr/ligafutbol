# -*- coding: utf-8 -*- 
#Modulos
import urllib2
from xml.dom.minidom import parse

#objetos
APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"
raiz = "http://www.resultados-futbol.com/scripts/api/api.php?key="+APIKEY+"&format=xml"

#peticiones al usuario
liga =(raw_input("Que liga quieres ver: "))

#Ligas
if liga=="primera españa":
    liga=1
elif liga=="segunda españa":
    liga=2

url = urllib2.urlopen(""+raiz+"&req=tables&league=%s" % liga)

#Reemplazos de palabras
lista= url.read()
lista=lista.replace("Real","R.")
lista=lista.replace("Rayo ","R.")
lista=lista.replace("Lugo","C.D Lugo")
equipos=open("equipos","w")
equipos.write(lista)
equipos.close()

#Leyendo XML
dom = parse('equipos')
nodo_equipos = dom.firstChild

equipos =[]
puntos =[]
ganados =[]
for nodo_equipo in nodo_equipos.getElementsByTagName('table'):
    equipo= nodo_equipo.getElementsByTagName('team')[0].firstChild.data.replace('\n','')
    punto= nodo_equipo.getElementsByTagName('points')[0].firstChild.data.replace('\n','')
    ganado= nodo_equipo.getElementsByTagName('wins')[0].firstChild.data.replace('\n','')
    equipos.append(equipo)
    puntos.append(punto)
    ganados.append(ganado)

#Mostrar en pantalla clasificacion
if liga==1:
    print "Pos.     Equipos       Puntos  Ganados"
    print "--------------------------------------"
    for i in range(20):
            print "%s\t%s   \t %s   \t %s" % (i+1,equipos[i],puntos[i],ganados[i])

elif liga==2:
    print "Pos.     Equipos       Puntos  Ganados"
    print "--------------------------------------"
    for i in range(22):
            print "%s\t%s   \t %s   \t %s" % (i+1,equipos[i],puntos[i],ganados[i])

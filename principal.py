# -*- coding: utf-8 -*- 
import urllib2
from xml.dom.minidom import parse

APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"

liga =(raw_input("Que liga quieres ver: "))
if liga=="primera españa":
    liga=1
if liga=="segunda españa":
    liga=2


url = urllib2.urlopen("http://www.resultados-futbol.com/scripts/api/api.php?key="+APIKEY+"&format=xml&req=tables&league=%s" % liga)
lista= url.read()
lista=lista.replace("Real","R.")
lista=lista.replace("Rayo ","R.")
lista=lista.replace("Lugo","C.D Lugo")
equipos=open("equipos","w")
equipos.write(lista)
equipos.close()

dom = parse('equipos')

nodo_equipos = dom.firstChild

equipos =[]
puntos =[]
ganados =[]
for nodo_equipo in nodo_equipos.getElementsByTagName('table'):
    equipo= nodo_equipo.getElementsByTagName('team')[0].firstChild.data
    punto= nodo_equipo.getElementsByTagName('points')[0].firstChild.data
    ganado= nodo_equipo.getElementsByTagName('wins')[0].firstChild.data
    equipos.append(equipo)
    puntos.append(punto)
    ganados.append(ganado)

equipos2 =[]
for i in equipos:
    sin_saltos = i.replace('\n','')
    equipos2.append(sin_saltos)

puntos2 =[]
for i in puntos:
    sin_saltos = i.replace('\n','')
    puntos2.append(sin_saltos)

ganados2 =[]
for i in ganados:
    sin_saltos = i.replace('\n','')
    ganados2.append(sin_saltos)

if liga==1:
    print "Pos      Equipos       Puntos  Ganados"
    print "-------------------------------------"
    for i in range(20):
            print "%s\t%s   \t %s   \t %s" % (i+1,equipos2[i],puntos2[i],ganados2[i])

if liga==2:
    print "Pos      Equipos       Puntos  Ganados"
    print "-------------------------------------"
    for i in range(22):
            print "%s\t%s   \t %s   \t %s" % (i+1,equipos2[i],puntos2[i],ganados2[i])



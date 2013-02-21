#!/usr/bin/python
# -*- coding: utf-8 -*- 
import cgi
import urllib2
from xml.dom.minidom import parse

#objetos
APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"
raiz = "http://www.resultados-futbol.com/scripts/api/api.php?key="+APIKEY+"&format=xml"

print "Content-Type: text/html\n"
form = cgi.FieldStorage()
name = form.getvalue("primera","NN")

print 

if name=="primera":
    name=1
if name=="segunda":
    name=2
elif name=="premier":
    name=10
elif name=="superliga":
    name=19

url = urllib2.urlopen(""+raiz+"&req=tables&league=%s" % name)

#Reemplazos de palabras
lista= url.read()
lista=lista.replace("Atlético","Atletico")
lista=lista.replace("Málaga","Malaga")
lista=lista.replace("Almería","Almeria")
lista=lista.replace("Alcorcón","Alcorcon")
lista=lista.replace("Córdoba","Cordoba")
lista=lista.replace("Mirandés","Mirandes")
lista=lista.replace("Hércules","Hercules")
lista=lista.replace("Paços","Pazos")
lista=lista.replace("Río","Rio")
lista=lista.replace("Marítimo","Maritimo")
lista=lista.replace("Guimarães","Guimaraes")
lista=lista.replace("Académica","Academica")
lista=lista.replace("Setúbal","Setubal")
equipos=open("fichero","w")
equipos.write(lista)
equipos.close()

#Leyendo XML
dom = parse('fichero')
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

    #Cuenta el número de equipos
Numeroequipos = len(equipos)

    #Mostrar en pantalla clasificación
print("<html><head><title>Clasificacion liga BBVA</title></head>")
print "<body><h5>Pos.     Equipos       Puntos  Ganados</h5>"
for i in range(Numeroequipos):
    print "<p>%s  %s  %s  %s</p></body></html>" % (i+1,equipos[i],puntos[i],ganados[i])

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
name = form.getvalue("liga")
name2 = form.getvalue("jornada")


url = urllib2.urlopen(""+raiz+"&req=matchs&league="+"%s"%name+"&round="+"%s" % name2)
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
result=open("fichero","w")
result.write(lista)
result.close()


#Leyendo XML
dom = parse('fichero')
nodo_result = dom.firstChild

locales =[]
visitantes =[]
gollocales =[]
golvisitantes =[]
for nodo_resul in nodo_result.getElementsByTagName('match'):
    local= nodo_resul.getElementsByTagName('local')[0].firstChild.data.replace('\n','')
    visitante= nodo_resul.getElementsByTagName('visitor')[0].firstChild.data.replace('\n','')
    gollocal= nodo_resul.getElementsByTagName('local_goals')[0].firstChild.data.replace('\n','')
    golvisitante= nodo_resul.getElementsByTagName('visitor_goals')[0].firstChild.data.replace('\n','')
    locales.append(local)
    visitantes.append(visitante)
    gollocales.append(gollocal)
    golvisitantes.append(golvisitante)

#Cuenta el número de equipos
Numeroequipos = len(locales)

#Muestra en pantalla resultados
print("<html><head><title>Resultados</title></head>")
print "<body><h5>Local                   visitante</h5>"
for i in range(Numeroequipos):
    print "<p>%s  \t%s-%s\t%s</p></body></html>" % (locales[i],gollocales[i],golvisitantes[i],visitantes[i])





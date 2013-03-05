#!/usr/bin/python
# -*- coding: utf-8 -*- 
import cgi
from lxml import etree
import requests

#objetos
APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"

#Obtenemos valores
print "Content-Type: text/html\n"
form = cgi.FieldStorage()
name = form.getvalue("quini")
#Obtenemos XML
payload = {'round': '%s'%name, 'req': 'quiniela', 'format': 'xml', 'key': APIKEY}
r = requests.get('http://www.resultados-futbol.com/scripts/api/api.php?', params=payload)
url= r.text
#Leyendo XML
resp_xml = etree.fromstring(url)

local = resp_xml.xpath("/quiniela/quiniela/lines/team1_name/text()")
visitante = resp_xml.xpath("/quiniela/quiniela/lines/team2_name/text()")
resultado = resp_xml.xpath("/quiniela/quiniela/lines/result/text()")


#Cuenta el número de equipos
Numeroequipos = len(local)

#Mostrar en pantalla clasificación
print("<html><head><title>Resultado</title></head>")
print "<body><h5>Resultado</h5><table><tr><th></th><th></th><th></th></tr>"
for i in range(Numeroequipos):
    print "<tr><td>%s</td><td>%s</td><td>%s</td>" % (local[i].encode('utf-8'),visitante[i].encode('utf-8'),resultado[i].encode('utf-8'))  
print "</table><p> <a href=../>Volver al indice</a></p></body></html>"


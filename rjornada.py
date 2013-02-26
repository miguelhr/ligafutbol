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
name = form.getvalue("liga")
name2 = form.getvalue("jornada")

#Obtenemos XML
payload = {'req': 'matchs', 'league': '%s' % name, 'format': 'xml', 'key': APIKEY, 'round': '%s' % name2}
r = requests.get('http://www.resultados-futbol.com/scripts/api/api.php?', params=payload)
url= r.text

#Leyendo XML
resp_xml = etree.fromstring(url)

locales = resp_xml.xpath("/matchs/match/local/text()")
visitantes = resp_xml.xpath("/matchs/match/visitor/text()")
gollocales = resp_xml.xpath("/matchs/match/local_goals/text()")
golvisitantes = resp_xml.xpath("/matchs/match/visitor_goals/text()")

#Cuenta el número de equipos
Numeroequipos = len(locales)

#Muestra en pantalla resultados
print("<html><head><title>Resultados</title></head>")
print "<body><h5>Local                   visitante</h5>"
for i in range(Numeroequipos):
    print "<p>%s  \t%s-%s\t%s</p></body></html>" % (locales[i].encode('utf-8'),gollocales[i],golvisitantes[i],visitantes[i].encode('utf-8'))





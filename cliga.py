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
name = form.getvalue("clasi")

#Obtenemos XML
payload = {'league': '%s'%name, 'req': 'tables', 'format': 'xml', 'key': APIKEY}
r = requests.get('http://www.resultados-futbol.com/scripts/api/api.php?', params=payload)
url= r.text

#Leyendo XML
resp_xml = etree.fromstring(url)

equipos = resp_xml.xpath("/tables/table/team/text()")
puntos = resp_xml.xpath("/tables/table/points/text()")
jugados = resp_xml.xpath("/tables/table/round/text()")
ganados = resp_xml.xpath("/tables/table/wins/text()")
empatados = resp_xml.xpath("/tables/table/draws/text()")
perdidos = resp_xml.xpath("/tables/table/losses/text()")
gfavor = resp_xml.xpath("/tables/table/gf/text()")
gcontra = resp_xml.xpath("/tables/table/ga/text()")
gaverage = resp_xml.xpath("/tables/table/avg/text()")

#Cuenta el número de equipos
Numeroequipos = len(equipos)

#Mostrar en pantalla clasificación
print("<html><head><title>Clasificacion</title></head>")
print "<body><h5>Pos.     Equipos       Puntos  Ganados</h5>"
for i in range(Numeroequipos):
    print "<p>%s  %s  %s  %s  %s  %s  %s  %s  %s  %s</p></body></html>" % (i+1,equipos[i].encode('utf-8'),puntos[i],jugados[i],ganados[i],empatados[i],perdidos[i],gfavor[i],gcontra[i],gaverage[i])


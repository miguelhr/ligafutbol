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
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
bodyElt = etree.SubElement(page, "body")
title = etree.SubElement(headElt, "title")
title.text = "Clasificacion"
tableElt = etree.SubElement(bodyElt, "table")
trElt = etree.SubElement(tableElt, "tr")

datos = ["Pos.","Equipos","P","J","G","E","P","GF","GC","GV"]
for i in datos:
    thElt = etree.SubElement(trElt, "th")
    thElt.text = "%s" % i

for i in range(Numeroequipos):
    trElt2 = etree.SubElement(tableElt, "tr")
    tdElt = etree.SubElement(trElt2, "td")
    tdElt.text = "%s" % (i+1)
    tdElt2 = etree.SubElement(trElt2, "td")
    tdElt2.text = "%s" % (equipos[i])
    tdElt3 = etree.SubElement(trElt2, "td")
    tdElt3.text = "%s" % (puntos[i])
    tdElt4 = etree.SubElement(trElt2, "td")
    tdElt4.text = "%s" % (jugados[i])
    tdElt5 = etree.SubElement(trElt2, "td")
    tdElt5.text = "%s" % (ganados[i])
    tdElt6 = etree.SubElement(trElt2, "td")
    tdElt6.text = "%s" % (empatados[i])
    tdElt7 = etree.SubElement(trElt2, "td")
    tdElt7.text = "%s" % (perdidos[i])
    tdElt8 = etree.SubElement(trElt2, "td")
    tdElt8.text = "%s" % (gfavor[i])
    tdElt9 = etree.SubElement(trElt2, "td")
    tdElt9.text = "%s" % (gcontra[i])
    tdElt10 = etree.SubElement(trElt2, "td")
    tdElt10.text = "%s" % (gaverage[i])

pElt = etree.SubElement(bodyElt, "p")
aElt2 = etree.SubElement(pElt, "a", href="..")
aElt2.text = "Volver al indice"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')




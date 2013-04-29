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
resp_xml = etree.fromstring(url.encode('utf-8'))

local = resp_xml.xpath("/quiniela/quiniela/lines/team1_name/text()")
visitante = resp_xml.xpath("/quiniela/quiniela/lines/team2_name/text()")
resultado = resp_xml.xpath("/quiniela/quiniela/lines/result/text()")


#Cuenta el número de equipos
Numeroequipos = len(local)

#Mostrar en pantalla clasificación
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
bodyElt = etree.SubElement(page, "body")
title = etree.SubElement(headElt, "title")
title.text = "Resultados De Quiniela"
h4Elt = etree.SubElement(bodyElt, "h4")
h4Elt.text = "Resultados"
tableElt = etree.SubElement(bodyElt, "table")
trElt = etree.SubElement(tableElt, "tr")

datos = ["","",""]
for i in datos:
    thElt = etree.SubElement(trElt, "th")
    thElt.text = "%s" % i

for i in range(Numeroequipos):
    trElt2 = etree.SubElement(tableElt, "tr")
    tdElt = etree.SubElement(trElt2, "td")
    tdElt.text = "%s" % (local[i])
    tdElt = etree.SubElement(trElt2, "td")
    tdElt.text = "%s" % (visitante[i])
    tdElt = etree.SubElement(trElt2, "td")
    tdElt.text = "%s" % (resultado[i])

pElt = etree.SubElement(bodyElt, "p")
aElt2 = etree.SubElement(pElt, "a", href="..")
aElt2.text = "Volver al indice"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')




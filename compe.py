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
name = form.getvalue("compe")

#Obtenemos XML
payload = {'country': '%s'%name, 'req': 'leagues', 'format': 'xml', 'key': APIKEY}
r = requests.get('http://www.resultados-futbol.com/scripts/api/api.php?', params=payload)
url= r.text

#Leyendo XML
resp_xml = etree.fromstring(url)

compe = resp_xml.xpath("/leagues/league/name/text()")

#Cuenta el número de equipos
Numeroequipos = len(compe)

#Mostrar en pantalla clasificación
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
bodyElt = etree.SubElement(page, "body")
title = etree.SubElement(headElt, "title")
title.text = "Competiciones"
tableElt = etree.SubElement(bodyElt, "table")
trElt = etree.SubElement(tableElt, "tr")
thElt = etree.SubElement(trElt, "th")
thElt.text = "Competiciones"
for i in range(Numeroequipos):
    trElt2 = etree.SubElement(tableElt, "tr")
    tdElt = etree.SubElement(trElt2, "td")
    tdElt.text = "%s" % (compe[i])

pElt = etree.SubElement(bodyElt, "p")
aElt2 = etree.SubElement(pElt, "a", href="..")
aElt2.text = "Volver al indice"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')



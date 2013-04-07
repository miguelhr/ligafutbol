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
fotolocal = resp_xml.xpath("/matchs/match/local_shield/text()")
fotovisi = resp_xml.xpath("/matchs/match/visitor_shield/text()")
fecha = resp_xml.xpath("/matchs/match/schedule/text()")
canal = resp_xml.xpath("/matchs/match/channels/image/text()")

#Cuenta el número de equipos
Numeroequipos = len(locales)

#Muestra en pantalla resultados
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
bodyElt = etree.SubElement(page, "body")
title = etree.SubElement(headElt, "title")
title.text = "Resultados De Jornada"
tableElt = etree.SubElement(bodyElt, "table")
trElt = etree.SubElement(tableElt, "tr")

datos = ["","Local","Resultado","Visitante",""]
for i in datos:
    thElt = etree.SubElement(trElt, "th")
    thElt.text = "%s" % i

for i in range(Numeroequipos):
    trElt2 = etree.SubElement(tableElt, "tr")
    tdElt = etree.SubElement(trElt2, "td")
    imgElt = etree.SubElement(tdElt, "img", src="%s" % (fotolocal[i]), alt="local")
    tdElt2 = etree.SubElement(trElt2, "td", align="center")
    tdElt2.text = "%s" % (locales[i])
    tdElt3 = etree.SubElement(trElt2, "td", align="center")
    tdElt3.text = "%s - %s" % (gollocales[i],golvisitantes[i])
    tdElt4 = etree.SubElement(trElt2, "td", align="center")
    tdElt4.text = "%s" % (visitantes[i])
    tdElt5 = etree.SubElement(trElt2, "td", align="center")
    imgElt2 = etree.SubElement(tdElt5, "img", src="%s" % (fotovisi[i]), alt="local")

    trElt3 = etree.SubElement(tableElt, "tr")
    tdElt6 = etree.SubElement(trElt3, "td")
    tdElt6.text = ""
    tdElt7 = etree.SubElement(trElt3, "td")
    tdElt7.text = ""
    tdElt8 = etree.SubElement(trElt3, "td")
    tdElt8.text = "%s" % (fecha[i])
    tdElt9 = etree.SubElement(trElt3, "td")
    tdElt9.text = ""
    tdElt10 = etree.SubElement(trElt3, "td")
    tdElt10.text = "" 

pElt = etree.SubElement(bodyElt, "p")
aElt2 = etree.SubElement(pElt, "a", href="..")
aElt2.text = "Volver al indice"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')



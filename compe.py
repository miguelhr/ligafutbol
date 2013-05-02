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
resp_xml = etree.fromstring(url.encode('utf-8'))

compe = resp_xml.xpath("/leagues/league/name/text()")
codigo = resp_xml.xpath("/leagues/league/id/text()")

#Cuenta el número de equipos
Numeroequipos = len(compe)
Numerocompe = len(codigo)

#Mostrar en pantalla clasificación
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Competiciones"

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
#meta = etree.SubElement(headElt, "meta",http-equiv='Content-Type', content='text/html; charset=utf-8')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estilocomp.css")

bodyElt = etree.SubElement(page, "body")
div = etree.SubElement(bodyElt, "div", id="container")
div2 = etree.SubElement(div, "div", id="header")
h1Elt = etree.SubElement(div2, "h1")
h1Elt.text = "Competiciones"
div3 = etree.SubElement(div, "div", id="content")

tableElt = etree.SubElement(div3, "table")
trElt = etree.SubElement(tableElt, "tr")
thElt = etree.SubElement(trElt, "th")
thElt.text = "Competiciones"
for i in range(Numeroequipos):
    for i in range(Numerocompe):
        trElt2 = etree.SubElement(tableElt, "tr")
        tdElt = etree.SubElement(trElt2, "td")
        pElt2 = etree.SubElement(tdElt, "p")
        aElt3 = etree.SubElement(pElt2, "a", href="http://localhost/cgi-bin/cliga.py?clasi=%s"% codigo[i])
        aElt3.text = "%s"% (compe[i])
    break

pElt = etree.SubElement(bodyElt, "p")
aElt2 = etree.SubElement(pElt, "a", href="..")
aElt2.text = "Volver al indice"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')



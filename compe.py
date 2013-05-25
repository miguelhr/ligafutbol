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

#Contadores
Numeroequipos = len(compe)
Numerocompe = len(codigo)

#Mostrar en pantalla clasificación
#Cabecera
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Competiciones"

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estilocomp.css")

bodyElt = etree.SubElement(page, "body")
div = etree.SubElement(bodyElt, "div", id="container")
div2 = etree.SubElement(div, "div", id="header")
ulElt1 = etree.SubElement(div2, "ul")
liElt1 = etree.SubElement(ulElt1, "li")
aElt1 = etree.SubElement(liElt1, "a", href="http://localhost/clasificacion.html")
aElt1.text = "Clasificaciones de Ligas"
liElt2 = etree.SubElement(ulElt1, "li")
aElt2 = etree.SubElement(liElt2, "a", href="http://localhost/resultados.html")
aElt2.text = "Resultados de Ligas"
liElt3 = etree.SubElement(ulElt1, "li")
aElt3 = etree.SubElement(liElt3, "a", href="http://localhost/quiniela.html")
aElt3.text = "Quiniela Liga Espanola"
liElt4 = etree.SubElement(ulElt1, "li")
aElt4 = etree.SubElement(liElt4, "a", href="http://localhost/compe.html")
aElt4.text = "Competiciones"
liElt5 = etree.SubElement(ulElt1, "li")
aElt5 = etree.SubElement(liElt5, "a", href="http://localhost/noticias.html")
aElt5.text = "Noticias"

#contenido
div3 = etree.SubElement(div, "div", id="content")
h1Elt = etree.SubElement(div3, "h1")
h1Elt.text = "Competiciones"
ulElt = etree.SubElement(div3, "ul")
for i in range(Numeroequipos):
    for i in range(Numerocompe):
        liElt2 = etree.SubElement(ulElt, "li")
        aElt3 = etree.SubElement(liElt2, "a", href="http://localhost/cgi-bin/cliga.py?clasi=%s"% codigo[i])
        aElt3.text = "%s"% (compe[i])
    break

#pie de pagina
div4 = etree.SubElement(div, "div", id="pie")
pElt = etree.SubElement(div4, "p")
pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')


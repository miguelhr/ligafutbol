#!/usr/bin/python
# -*- coding: utf-8 -*- 
import cgi
import feedparser
from lxml import etree
import requests

#Obtenemos valores
print "Content-Type: text/html\n"
form = cgi.FieldStorage()
name = form.getvalue("noti")

#Obtenemos XML
tesdementa = feedparser.parse("http://espndeportes-assets.espn.go.com/rss/news?section=section.%s&name=%s"% (name,name))

#Muestra en pantalla resultados
#Cabecera
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Noticias de %s" % name

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estilorss.css")

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
h1Elt.text = "Noticias de %s" % name
div4 = etree.SubElement(div3, "div", id="fondo")

for entry in tesdementa.entries:
    h4Elt2 = etree.SubElement(div3, "h4")
    h4Elt2.text = "%s" % (entry.title)
    pElt2 = etree.SubElement(div3, "p")
    pElt2.text = "%s" % (entry.date)
    pElt = etree.SubElement(div3, "p",id="contenido")
    pElt.text = "%s" % (entry.summary)
    aElt = etree.SubElement(pElt, "a", href=entry.link)
    aElt.text = "Leer mas"

#Pie de pagina
div4 = etree.SubElement(div, "div", id="pie")
pElt = etree.SubElement(div4, "p")
pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')

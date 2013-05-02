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
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Noticias de %s" % name

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
#meta = etree.SubElement(headElt, "meta",http-equiv='Content-Type', content='text/html; charset=utf-8')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estilorss.css")

bodyElt = etree.SubElement(page, "body")
div = etree.SubElement(bodyElt, "div", id="container")
div2 = etree.SubElement(div, "div", id="header")
h1Elt = etree.SubElement(div2, "h1")
h1Elt.text = "Noticias de %s" % name
div3 = etree.SubElement(div, "div", id="content") 

for entry in tesdementa.entries:
    h4Elt2 = etree.SubElement(bodyElt, "h4")
    h4Elt2.text = "%s" % (entry.title)
    pElt2 = etree.SubElement(bodyElt, "p")
    pElt2.text = "%s" % (entry.date)
    pElt = etree.SubElement(bodyElt, "p")
    pElt.text = "%s" % (entry.summary)
    aElt = etree.SubElement(pElt, "a", href=entry.link)
    aElt.text = "Leer mas"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')

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
resp_xml = etree.fromstring(url.encode('utf-8'))

locales = resp_xml.xpath("/matchs/match/local/text()")
visitantes = resp_xml.xpath("/matchs/match/visitor/text()")
gollocales = resp_xml.xpath("/matchs/match/local_goals/text()")
golvisitantes = resp_xml.xpath("/matchs/match/visitor_goals/text()")
fotolocal = resp_xml.xpath("/matchs/match/local_shield/text()")
fotovisi = resp_xml.xpath("/matchs/match/visitor_shield/text()")
fecha = resp_xml.xpath("/matchs/match/schedule/text()")
canal = resp_xml.xpath("/matchs/match/channels/image/text()")
codigo = resp_xml.xpath("/matchs/match/id/text()")

#Contadores
Numeroequipos = len(locales)

#Muestra en pantalla resultados
#Cabecera
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Resultados De Jornada"

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estiloresult.css")

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
h1Elt.text = "Resultados Jornada %s" % name2

tableElt = etree.SubElement(div3, "table",align="center")
trElt = etree.SubElement(tableElt, "tr")

datos = ["Hora","","Local","Resultado","Visitante",""]
for i in datos:
    thElt = etree.SubElement(trElt, "th")
    thElt.text = "%s" % i

for i in range(Numeroequipos):
    trElt2 = etree.SubElement(tableElt, "tr")
    tdElt8 = etree.SubElement(trElt2, "td")
    tdElt8.text = "%s" % (fecha[i][:-3])
    tdElt = etree.SubElement(trElt2, "td")
    imgElt = etree.SubElement(tdElt, "img", src="%s" % (fotolocal[i]), alt="local")
    tdElt2 = etree.SubElement(trElt2, "td")
    tdElt2.text = "%s" % (locales[i])
    tdElt3 = etree.SubElement(trElt2, "td")
    aElt3 = etree.SubElement(tdElt3, "a", href="http://localhost/cgi-bin/detalle.py?id=%s"% codigo[i])
    aElt3.text = "%s - %s" % (gollocales[i],golvisitantes[i])
    tdElt4 = etree.SubElement(trElt2, "td")
    tdElt4.text = "%s" % (visitantes[i])
    tdElt5 = etree.SubElement(trElt2, "td")
    imgElt2 = etree.SubElement(tdElt5, "img", src="%s" % (fotovisi[i]), alt="local")

#Pie de pagina
div4 = etree.SubElement(div, "div", id="pie")
pElt = etree.SubElement(div4, "p")
pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')



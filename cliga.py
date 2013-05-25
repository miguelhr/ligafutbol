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
try:
    resp_xml = etree.fromstring(url.encode('utf-8'))

    equipos = resp_xml.xpath("/tables/table/team/text()")
    puntos = resp_xml.xpath("/tables/table/points/text()")
    jugados = resp_xml.xpath("/tables/table/round/text()")
    ganados = resp_xml.xpath("/tables/table/wins/text()")
    empatados = resp_xml.xpath("/tables/table/draws/text()")
    perdidos = resp_xml.xpath("/tables/table/losses/text()")
    gfavor = resp_xml.xpath("/tables/table/gf/text()")
    gcontra = resp_xml.xpath("/tables/table/ga/text()")
    gaverage = resp_xml.xpath("/tables/table/avg/text()")

    #Cuenta el numero de equipos
    Numeroequipos = len(equipos)

#Si ocurre cualquier error, nos muestra esta pagina de error
except:
    page = etree.Element("html")
    doc=etree.ElementTree(page)
    headElt = etree.SubElement(page, "head")
    title = etree.SubElement(headElt, "title")
    title.text = "ERROR"
    link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
    link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/error.css")

    bodyElt = etree.SubElement(page, "body")
    div = etree.SubElement(bodyElt, "div", id="container")
    div2 = etree.SubElement(div, "div", id="header")
    div3 = etree.SubElement(div, "div", id="content")
    h1Elt = etree.SubElement(div2, "h1")
    h1Elt.text = "Pagina en Construccion"
    pElt = etree.SubElement(div3, "p")
    pElt.text = "Lo sentimos mucho, pero este contenido esta en construccion y estamos solucionando el problema. Para cualquier consulta mande un correo al administrador."

    div4 = etree.SubElement(div, "div", id="pie")
    pElt = etree.SubElement(div4, "p")
    pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

    print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')

#Si el numero de equipos es 0 nos muestra la pagina de error
if Numeroequipos==0:
    page = etree.Element("html")
    doc=etree.ElementTree(page)
    headElt = etree.SubElement(page, "head")
    title = etree.SubElement(headElt, "title")
    title.text = "ERROR"
    link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
    link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/error.css")

    bodyElt = etree.SubElement(page, "body")
    div = etree.SubElement(bodyElt, "div", id="container")
    div2 = etree.SubElement(div, "div", id="header")
    div3 = etree.SubElement(div, "div", id="content")
    h1Elt = etree.SubElement(div2, "h1")
    h1Elt.text = "Pagina en Construccion"
    pElt = etree.SubElement(div3, "p")
    pElt.text = "Lo sentimos mucho, pero este contenido esta en construccion y estamos solucionando el problema. Para cualquier consulta mande un correo al administrador."

    div4 = etree.SubElement(div, "div", id="pie")
    pElt = etree.SubElement(div4, "p")
    pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

    print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')

#Si es mayor que 0 seguira
else:
    #Mostrar en pantalla clasificacion
    #Cabecera
    page = etree.Element("html")
    doc=etree.ElementTree(page)
    headElt = etree.SubElement(page, "head")
    title = etree.SubElement(headElt, "title")
    title.text = "Clasificacion"

    link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
    link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estiloclaa.css")

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

    #Contenido
    div3 = etree.SubElement(div, "div", id="content")
    h1Elt = etree.SubElement(div3, "h1")
    h1Elt.text = "Clasificiacion"

    tableElt = etree.SubElement(div3, "table",align="center")
    trElt = etree.SubElement(tableElt, "tr")

    datos = ["Pos","Equipos","P","J","G","E","P","GF","GC","GV"]
    for i in datos:
        thElt = etree.SubElement(trElt, "th")
        thElt.text = "%s" % i

    for i in range(Numeroequipos):
        trElt2 = etree.SubElement(tableElt, "tr")
        tdElt = etree.SubElement(trElt2, "td")
        tdElt.text = "%s" % (i+1)
        tdElt2 = etree.SubElement(trElt2, "td",id="espacio")
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

    #pie de pagina
    div4 = etree.SubElement(div, "div", id="pie")
    pElt = etree.SubElement(div4, "p")
    pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"
    print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')


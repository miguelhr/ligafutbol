#!/usr/bin/python
# -*- coding: utf-8 -*- 
import cgi
from lxml import etree
import requests
import re
#objetos
APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"

#Obtenemos valores
print "Content-Type: text/html\n"
form = cgi.FieldStorage()
name = form.getvalue("id")

#Obtenemos XML
payload = {'req': 'match', 'format': 'xml', 'key': APIKEY, 'id': '%s' % name}
r = requests.get('http://www.resultados-futbol.com/scripts/api/api.php?', params=payload)
url= r.text

#Eliminamos la etiqueta erronea para poder obtener el xml
x=re.search("<progression>.*?</progression>", url, re.DOTALL)
span = x.span()
stripped_content = url[:span[0]] + url[span[1]:]
x=re.search("<progression>.*?</progression>", stripped_content, re.DOTALL)
span = x.span()
stripped_content1 = stripped_content[:span[0]] + stripped_content[span[1]:]

#Leyendo XML
resp_xml = etree.fromstring(stripped_content1.encode('utf-8'),etree.XMLParser(ns_clean=True, recover=True))

locales = resp_xml.xpath("/match/local/text()")
visitantes = resp_xml.xpath("/match/visitor/text()")
estadio = resp_xml.xpath("/match/stadium/text()")
liga = resp_xml.xpath("/match/league/text()")
#twitterlocal = resp_xml.xpath("/match/team1_twitter/text()")
#twittervisi = resp_xml.xpath("/match/team2_twitter/text()")
resultado = resp_xml.xpath("/match/result/text()")
jornada = resp_xml.xpath("/match/round/text()")
escudolocal = resp_xml.xpath("/match/local_shield/text()")
escudovisitante = resp_xml.xpath("/match/visitor_shield/text()")
arbitro = resp_xml.xpath("/match/referee/text()")
minutotarje = resp_xml.xpath("/match/events/cards/minute/text()")
equipotarje = resp_xml.xpath("/match/events/cards/team/text()")
jugadortarje = resp_xml.xpath("/match/events/cards/player/text()")
iconotarje = resp_xml.xpath("/match/events/cards/action_icon/text()")
minutogol = resp_xml.xpath("/match/events/goals/minute/text()")
equipogol = resp_xml.xpath("/match/events/goals/team/text()")
jugadorgol = resp_xml.xpath("/match/events/goals/player/text()")
iconogol = resp_xml.xpath("/match/events/goals/action_icon/text()")
numerojugadorvisi = resp_xml.xpath("/match/lineups/visitor/num/text()")
apellidojugavisi = resp_xml.xpath("/match/lineups/visitor/last_name/text()")
nombrejugavisi = resp_xml.xpath("/match/lineups/visitor/name/text()")
fotojugavisi = resp_xml.xpath("/match/lineups/visitor/image/text()")
numerojugadorlocal = resp_xml.xpath("/match/lineups/local/num/text()")
apellidojugalocal = resp_xml.xpath("/match/lineups/local/last_name/text()")
nombrejugalocal = resp_xml.xpath("/match/lineups/local/name/text()")
fotojugalocal = resp_xml.xpath("/match/lineups/local/image/text()")

#Contadores
numerojugadoresvisi = len(fotojugavisi)
numerojugadoreslocal = len(fotojugalocal)
contador = len(locales)
contador2 = len(minutotarje)
contador3 = len(minutogol)

#Muestra en pantalla resultados
#Cabecera
page = etree.Element("html")
doc=etree.ElementTree(page)
headElt = etree.SubElement(page, "head")
title = etree.SubElement(headElt, "title")
title.text = "Detalles de la Jornada %s de %s" % (jornada[0],liga[0])

link = etree.SubElement(headElt, "link",href='http://fonts.googleapis.com/css?family=PT+Sans', rel='stylesheet', type='text/css')
link2 = etree.SubElement(headElt, "link",rel="stylesheet", type="text/css", href="http://localhost/css/estilodetalle.css")

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

div3 = etree.SubElement(div, "div", id="content")
h1Elt = etree.SubElement(div3, "h1")
h1Elt.text = "Detalles de la Jornada %s de %s" % (jornada[0],liga[0])

#Tabla local
div4 = etree.SubElement(div3, "div", id="tablas")

div5 = etree.SubElement(div4, "div", id="tablalocal")
tableElt1 = etree.SubElement(div5, "table")
trElt1 = etree.SubElement(tableElt1, "tr")
thElt1 = etree.SubElement(trElt1, "th",colspan="4")
thElt1.text = "%s" % locales[0]

trElt2 = etree.SubElement(tableElt1, "tr")
datos1 = ["Foto","Nombre","Apellido","Numero"]
for i in datos1:
    thElt2 = etree.SubElement(trElt2, "th")
    thElt2.text = "%s" % i

for i in range(numerojugadoreslocal):
    trElt3 = etree.SubElement(tableElt1, "tr")
    tdElt1 = etree.SubElement(trElt3, "td")
    imgElt1 = etree.SubElement(tdElt1, "img", src="%s" % (fotojugalocal[i]), alt="local")
    tdElt2 = etree.SubElement(trElt3, "td")
    tdElt2.text = "%s" % (nombrejugalocal[i])
    tdElt3 = etree.SubElement(trElt3, "td")
    tdElt3.text = "%s" % (apellidojugalocal[i])
    tdElt4 = etree.SubElement(trElt3, "td")
    tdElt4.text = "%s" % (numerojugadorlocal[i])

#Tabla datos del partido
div6 = etree.SubElement(div4, "div", id="tabladatos")
tableElt20 = etree.SubElement(div6, "table")
trElt20 = etree.SubElement(tableElt20, "tr")
thElt20 = etree.SubElement(trElt20, "th",colspan="6")
thElt20.text = "Datos de Partido" 

trElt21 = etree.SubElement(tableElt20, "tr")
datos3 = ["Local","","Resultado","","Visitante","Estadio"]
for i in datos3:
    thElt21 = etree.SubElement(trElt21, "th")
    thElt21.text = "%s" % i

for i in range(contador):
    trElt22 = etree.SubElement(tableElt20, "tr")
    tdElt22 = etree.SubElement(trElt22, "td")
    tdElt22.text = "%s" % (locales[i])
    tdElt23 = etree.SubElement(trElt22, "td")
    imgElt20 = etree.SubElement(tdElt23, "img", src="%s" % (escudolocal[i]), alt="fotolocal")
    tdElt24 = etree.SubElement(trElt22, "td")
    tdElt24.text = "%s" % (resultado[i])
    tdElt25 = etree.SubElement(trElt22, "td")
    imgElt21 = etree.SubElement(tdElt25, "img", src="%s" % (escudovisitante[i]), alt="fotovisi")
    tdElt26 = etree.SubElement(trElt22, "td")
    tdElt26.text = "%s" % (visitantes[i])
    tdElt27 = etree.SubElement(trElt22, "td")
    tdElt27.text = "%s" % (estadio[i])

#Tabla visitante
div9 = etree.SubElement(div4, "div", id="tablavisi")
tableElt10 = etree.SubElement(div9, "table")
trElt10 = etree.SubElement(tableElt10, "tr")
thElt10 = etree.SubElement(trElt10, "th",colspan="4")
thElt10.text = "%s" % visitantes[0] 

trElt11 = etree.SubElement(tableElt10, "tr")
datos2 = ["Foto","Nombre","Apellido","Numero"]
for i in datos2:
    thElt11 = etree.SubElement(trElt11, "th")
    thElt11.text = "%s" % i

for i in range(numerojugadoresvisi):
    trElt12 = etree.SubElement(tableElt10, "tr")
    tdElt10 = etree.SubElement(trElt12, "td")
    imgElt10 = etree.SubElement(tdElt10, "img", src="%s" % (fotojugavisi[i]), alt="visitante")
    tdElt11 = etree.SubElement(trElt12, "td")
    tdElt11.text = "%s" % (nombrejugavisi[i])
    tdElt12 = etree.SubElement(trElt12, "td")
    tdElt12.text = "%s" % (apellidojugavisi[i])
    tdElt13 = etree.SubElement(trElt12, "td")
    tdElt13.text = "%s" % (numerojugadorvisi[i])

#Tabla datos goles
contador10 = len(minutogol)
if contador10>0:
    div7 = etree.SubElement(div4, "div", id="tablagol")
    tableElt40 = etree.SubElement(div7, "table")
    trElt40 = etree.SubElement(tableElt40, "tr")
    thElt40 = etree.SubElement(trElt40, "th",colspan="4")
    thElt40.text = "Detalles de Goles" 

    trElt41 = etree.SubElement(tableElt40, "tr")
    datos5 = ["Minuto","Equipo","Jugador",""]
    for i in datos5:
        thElt41 = etree.SubElement(trElt41, "th")
        thElt41.text = "%s" % i

    for i in range(contador3):
        trElt42 = etree.SubElement(tableElt40, "tr")
        tdElt42 = etree.SubElement(trElt42, "td")
        tdElt42.text = "%s" % (minutogol[i])
        tdElt43 = etree.SubElement(trElt42, "td")
        tdElt43.text = "%s" % (equipogol[i])
        tdElt44 = etree.SubElement(trElt42, "td")
        tdElt44.text = "%s" % (jugadorgol[i])
        tdElt45 = etree.SubElement(trElt42, "td")
        imgElt41 = etree.SubElement(tdElt45, "img", src="%s" % (iconogol[i]), alt="iconogol")

#Tabla datos tarjetas
contador11 = len(minutotarje)
if contador11>0:
    div8 = etree.SubElement(div4, "div", id="tablatarje")
    tableElt30 = etree.SubElement(div8, "table")
    trElt30 = etree.SubElement(tableElt30, "tr")
    thElt30 = etree.SubElement(trElt30, "th",colspan="4")
    thElt30.text = "Detalles de Tarjetas" 

    trElt31 = etree.SubElement(tableElt30, "tr")
    datos4 = ["Minuto","Equipo","Jugador",""]
    for i in datos4:
        thElt31 = etree.SubElement(trElt31, "th")
        thElt31.text = "%s" % i

    for i in range(contador2):
        trElt32 = etree.SubElement(tableElt30, "tr")
        tdElt32 = etree.SubElement(trElt32, "td")
        tdElt32.text = "%s" % (minutotarje[i])
        tdElt33 = etree.SubElement(trElt32, "td")
        tdElt33.text = "%s" % (equipotarje[i])
        tdElt34 = etree.SubElement(trElt32, "td")
        tdElt34.text = "%s" % (jugadortarje[i])
        tdElt35 = etree.SubElement(trElt32, "td")
        imgElt31 = etree.SubElement(tdElt35, "img", src="%s" % (iconotarje[i]), alt="iconotarje")

#Pie de pagina
div4 = etree.SubElement(div, "div", id="pie")
pElt = etree.SubElement(div4, "p")
pElt.text = "Copyright 2013 miguelhr - API de www.resuldos-futbol.com"

print etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')


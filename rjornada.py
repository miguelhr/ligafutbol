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
print("<html><head><title>Resultados</title></head>")
print "<body><table><tr><th></th><th>Local</th><th>Resultado</th><th>Visitante</th><th></th></tr>"
for i in range(Numeroequipos):
    print "<tr><td><img src=%s alt=local/></td><td align=center>%s</td><td align=center>%s -%s</td><td align=center>%s</td><td><img src=%s alt=visitante/></td></tr>" % (fotolocal[i],locales[i].encode('utf-8'),gollocales[i],golvisitantes[i],visitantes[i].encode('utf-8'),fotovisi[i])
    if len(canal)>0:    
        print "<tr><td></td><td><img src=%s alt=canal/></td><td align=center>%s</td></tr>" % (canal[i],fecha[i])
print "</table><p> <a href=../>Volver al indice</a></p></body></html>"



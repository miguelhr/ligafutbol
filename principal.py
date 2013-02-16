# -*- coding: utf-8 -*- 
#Módulos
import urllib2
from xml.dom.minidom import parse

#objetos
APIKEY = "3102fc908ca426bc06c8cb1c48dcedd4"
raiz = "http://www.resultados-futbol.com/scripts/api/api.php?key="+APIKEY+"&format=xml"

#peticiones al usuario
print "competiciones \nclasificacion"
opcion =(raw_input("Que opcion quieres: "))

#Apartado clasificación
if opcion=="clasificacion":
    liga =(raw_input("Que liga quieres ver: "))
    #Ligas
    if liga=="primera españa":
        liga=1
    elif liga=="segunda españa":
        liga=2
    elif liga=="premier league":
        liga=10
    elif liga=="primera portugal":
        liga=19

    url = urllib2.urlopen(""+raiz+"&req=tables&league=%s" % liga)

    #Reemplazos de palabras
    lista= url.read()
    lista=lista.replace("Real","R.")
    lista=lista.replace("Rayo ","R.")
    lista=lista.replace("Lugo","C.D Lugo")
    lista=lista.replace(" FC","")
    lista=lista.replace(" Clube","")
    lista=lista.replace(" Braga","B.")
    lista=lista.replace("Paços de ","P. ")
    equipos=open("equipos","w")
    equipos.write(lista)
    equipos.close()

    #Leyendo XML
    dom = parse('equipos')
    nodo_equipos = dom.firstChild

    equipos =[]
    puntos =[]
    ganados =[]
    for nodo_equipo in nodo_equipos.getElementsByTagName('table'):
        equipo= nodo_equipo.getElementsByTagName('team')[0].firstChild.data.replace('\n','')
        punto= nodo_equipo.getElementsByTagName('points')[0].firstChild.data.replace('\n','')
        ganado= nodo_equipo.getElementsByTagName('wins')[0].firstChild.data.replace('\n','')
        equipos.append(equipo)
        puntos.append(punto)
        ganados.append(ganado)

    #Mostrar en pantalla clasificación
    #Clasificación para ligas de 16 equipos
    if liga==19:
        print "Pos.     Equipos       Puntos  Ganados"
        print "--------------------------------------"
        for i in range(16):
                print "%s\t%s   \t %s   \t %s" % (i+1,equipos[i],puntos[i],ganados[i])

    #Clasificación para ligas de 20 equipos
    elif liga==1 or 10:
        print "Pos.     Equipos       Puntos  Ganados"
        print "--------------------------------------"
        for i in range(20):
                print "%s\t%s   \t %s   \t %s" % (i+1,equipos[i],puntos[i],ganados[i])

    #Clasificación para ligas de 22 equipos
    elif liga==2:
        print "Pos.     Equipos       Puntos  Ganados"
        print "--------------------------------------"
        for i in range(22):
                print "%s\t%s   \t %s   \t %s" % (i+1,equipos[i],puntos[i],ganados[i])

#Apartado competiciones
elif opcion=="competiciones":
    opcion =(raw_input("Localización de la liga: "))

    #Competiciones
    if opcion=="españa":
        opcion="es"

    elif opcion=="francia":
        opcion="fr"

    elif opcion=="inglaterra":
        opcion="gb"

    elif opcion=="portugal":
        opcion="pt"

    url = urllib2.urlopen(""+raiz+"&req=leagues&country=%s" % opcion)
    lista= url.read()
    competis=open("competis","w")
    competis.write(lista)
    competis.close()

    #Leyendo XML
    dom = parse('competis')
    nodo_competis = dom.firstChild

    competis =[]
    for nodo_competi in nodo_competis.getElementsByTagName('league'):
        competi= nodo_competi.getElementsByTagName('name')[0].firstChild.data.replace('\n','')
        competis.append(competi)
    #Mostrar en pantalla competicones
    for i in competis:
        print i



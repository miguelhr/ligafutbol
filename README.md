ligafutbol
==========

Proyecto para Lenguaje de Marcas
--------------------------------

El proyecto se basara en realizar una aplicacion web donde podremos consultar resultados y la clasificacion de futbol de diferentes ligas. Utilizaremos la API resultados-futbol de la cual obtendremos los datos que necesitemos.


Para poder utilizar esta api, tenemos que tener Apache2 instalado y los modulos urllib2, cgi y xml (este viene por defecto instalado)

Los ubicacion de los archivos sera la siguiente:
-En /usr/lib/cgi-bin/ tendremos el archivo cLiga.py
-En /var/www/ tendremos el index.html

Los dos ficheros con permisos 777

en el navegador introducimos localhost y ya estara funcionando


aptitude install libapache2-mod-python


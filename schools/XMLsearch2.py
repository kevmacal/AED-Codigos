f = open("tempo.xml", "r")
fWrite = open("escuelas.csv", "a")

total = 0
busqueda = 0
busqValue = "span class=\"geo-dec\" title=\"Maps, aerial photos, and other data for this location\">"
headHTML = ""
cadena = headHTML
#print busqValue[3]
while True:
    letra = f.read(1)
    if not letra or total == 1:
        print ("End of file")
        break
    else:
        if(busqueda < len(busqValue)):
            if(busqValue[busqueda] == letra):
                busqueda = busqueda + 1
                #print letra
            else:
                busqueda = 0
        else:
            if(letra == '<'):
                total = 1
                busqueda = 0
                fWrite.write(cadena + "")
                print (cadena)
                cadena = headHTML
            else:
                cadena = cadena + letra
f.close()
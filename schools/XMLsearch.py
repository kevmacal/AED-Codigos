f = open("tempo.xml", "r")
fWrite = open("escuelas.csv", "a")

busqueda = 0
busqValue = "<h1 id=\"firstHeading\" class=\"firstHeading\" lang=\"en\">"
headHTML = ""
cadena = headHTML
#print busqValue[3]
while True:
    letra = f.read(1)
    if not letra:
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
                busqueda = 0
                fWrite.write("\n" + cadena + ";")
                print (cadena)
                cadena = headHTML
            else:
                cadena = cadena + letra
f.close()
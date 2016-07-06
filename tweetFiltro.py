# -*- coding: utf-8 -*-
import json
import os
from pprint import pprint
from os import listdir

archivos = []
for archDir in listdir("./data"):
    archivos.append(str(archDir))
    print ((str(archDir)))

#print archivos[0]

dictionary = []
for line in open('dictionary', 'r'):
    dictionary.append(line.upper())

#print tweets[0]["created_at"]
#print ((dictionary[20][0:len(dictionary[20]) - 1]))
#print ((tweets[0]['text'].upper().find(dictionary[20][0:len(dictionary[20]) - 1])))

for numArch in range(len(archivos)):
    #print archivos[numArch]
    fileOutput = open('./filter/filtrado_' + archivos[numArch], 'a')
    tweets = []
    pureTweets = []
    archi = open('./data/' + archivos[numArch], 'r')
    linea = archi.readline()
    numero = 0
    while linea != "":
        pureTweets.append(linea)
        linea = archi.readline()
    for line in open('./data/' + archivos[numArch], 'r'):
        try:
            tweets.append(json.loads(line))
            numero = numero + 1
            #A cazar errores
        except ValueError as error:
            print ((str(archivos[numArch]) + str(numero + 1)))
            print (error)
    for i in range(len(tweets)):
        found = -1
        for j in range(len(dictionary)):
            if found == -1:
                found = tweets[i]['text'].upper().find(dictionary[j][0:len(dictionary[j]) - 1])
            if found != -1:
    #            print ((pureTweets[i]))
                fileOutput.write(pureTweets[i])
    #            with open('./filter/pruebaFiltrado.json', 'a') as f:
    #                json.dump(pureTweets[i], f)
                break

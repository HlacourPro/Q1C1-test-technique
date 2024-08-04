import os
from afficher import afficher
from chercher import chercher
from class_file import ImmeubleClass

def parse_content(content, immeuble_list) :
    for line in content :
        line = line.replace(',', '')
        line_split = line.split('"')
        line_split = [line for line in line_split if line.strip()]
        if (len(line_split) != 9) :
            continue
        else :
            immeuble_list.append(ImmeubleClass(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4], line_split[5], line_split[6], line_split[7], line_split[8]))
    return immeuble_list

def read_file(immeuble_list) :
    for filename in os.listdir("data"):
        path = "data\\" + filename
        file = open(path, 'r')
        content = file.readlines()[1:]
        immeuble_list = parse_content(content, immeuble_list)
    immeuble_list.sort()
    return immeuble_list

def start() :
    immeuble_list = []
    immeuble_list = read_file(immeuble_list)
    while(1) :
        val = input("1: afficher,  2: rechercher, 3: exit\n")
        if(val != "1" and val != "2" and val != "3") :
            print("une valeur incorrecte à été saisie.")
            print("les valeurs correctes sont 1, 2 et 3\n")
        elif(val == "1") :
            afficher(immeuble_list)
        elif(val == "2") :
            chercher(immeuble_list)
        else :
            return

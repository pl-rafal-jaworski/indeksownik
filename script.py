import csv
import sys

def buildDatabase(databaseFileName):
    database = []
    with open(databaseFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line = 0
        for row in csv_reader:
            if line == 0:
                line += 1
            else:
                database.append(row)
        return database

def buildCheckFile(checkFileName):
    list = []
    with open (checkFileName) as file:
        for row in file:
            list.append(row.rstrip())
        return list

def startup():
    if len(sys.argv) !=3 :
        print("Błąd!\nPrawidłowa składnia to: python3 script.py baza plik_z_indeksami")
        #return False
    else:
        global databaseFileName
        global checkFileName
        databaseFileName = sys.argv[1]
        checkFileName = sys.argv[2]
        #return True
        mainCont()
def mainCont():
    global database
    global list
    database = buildDatabase(databaseFileName)
    list = buildCheckFile(checkFileName)
    #print (list)
    findInDatabase()
    saveAsCSV()

def findInDatabase():
    global referenceTable
    referenceTable = []
    global savedIndexes
    savedIndexes = []
    for index in list:
        for row in database:
            if index == row[1]:
                person = ""
                person += row[1] + ";"
                person += row[2] + ";"
                person += row[3] + ";"
                person += row[4] + ";"
                person += row[5] + ";"
                person += row[6] + ";"
                person += row[7] + ";"
                person += row[8]
                referenceTable.append(person)
                savedIndexes.append(index)
                #print(referenceTable)
    #print(database[0][1])
def notFoundIndexes():
    global notFound
    notFound = []
    for person in list:
        if person not in savedIndexes:
            notFound.append(person)
    if len(notFound) > 0:
        return True
    else:
        return False


def saveAsCSV():
    with open("wynik.csv", 'w') as file:
        file.write('Indeks;Imię;Imię 2;Nazwisko;Kierunek 1;Specjalność 1;Kierunek 2;Specjalność 2\n')
        for person in referenceTable:
            file.write(person)
            file.write('\n')
        if notFoundIndexes() :
            file.write("\n\nBrak danych o indeksach\n")
            for p in notFound:
                file.write(p+"\n")







startup()

# Klasse der indeholder atributter og metoder til håndtering af database.
# Jeg har ikke kigget nærmere på typisk design mønster for impementering af databaser, men denne klasse lader til at
# virke som den skal og gøre min kode genbrugelig
# Dens eneste formål er at lære sqlite3. Funktionaliteten i klassen laver en backup af mine test materialer i en
# databasefil der hedder 'examen.db'. Der er ligeledes funktioner der kan lave objekter af typen Bog, Film, CD og
# DRMLicens fra data i databasen. Hver gang mit program starter dumpes alle tabeller i databasen, oprettes på ny og
# data fra listMaterialer kopieres ind igen.
# Imports
import sqlite3
from klasser import Bog, Film, CD, DRMLicens


class dbHandler:
    # constructor der laver en database hvis den ikke findes i forvejen og initiliserer en cursor.
    def __init__(self, dbNavn):
        self.dbNavn = dbNavn
        # Skaber forbindelse til databasen. Hvis den ikke eksisterer, bliver den oprettet
        self.conn = sqlite3.connect(self.dbNavn)
        self.cursor = self.conn.cursor()
        # Sletter tabeller i databasen så jeg har en tom database at arbejde med til testdataen
        self.cleanDB()

    # metode der laver database strukturen. Tabellerne afspejler mine klasser i klasser.py
    def makeStructure(self):
        # opretter tabel BOG
        self.cursor.execute('''CREATE TABLE BOG
                            (ID INTEGER PRIMARY KEY NOT NULL,
                            TITEL TEXT NOT NULL,
                            ANTAL TEXT NOT NULL,
                            N_UDLAAN TEXT NOT NULL,
                            RESERVEREDE TEXT NOT NULL,
                            AARSTAL TEXT NOT NULL,
                            N_SIDER TEXT NOT NULL,
                            FORFATTER TEXT NOT NULL)''')
        # opretter tabel FILM
        self.cursor.execute('''CREATE TABLE FILM
                            (ID INTEGER PRIMARY KEY NOT NULL,
                            TITEL TEXT NOT NULL,
                            ANTAL TEXT NOT NULL,
                            N_UDLAAN TEXT NOT NULL,
                            RESERVEREDE TEXT NOT NULL,
                            AARSTAL TEXT NOT NULL,
                            INSTRUKTOER TEXT NOT NULL,
                            VARIGHED TEXT NOT NULL)''')
        # opretter tabel CD
        self.cursor.execute('''CREATE TABLE CD
                            (ID INTEGER PRIMARY KEY NOT NULL,
                            TITEL TEXT NOT NULL,
                            ANTAL TEXT NOT NULL,
                            N_UDLAAN TEXT NOT NULL,
                            RESERVEREDE TEXT NOT NULL,
                            AARSTAL TEXT NOT NULL,
                            KUNSTNER TEXT NOT NULL,
                            TRACKS TEXT NOT NULL,
                            TOTAL_VARIGHED TEXT NOT NULL)''')
        # opretter tabel DRMLICENS
        self.cursor.execute('''CREATE TABLE DRMLICENS
                            (ID INTEGER PRIMARY KEY NOT NULL,
                            TITEL TEXT NOT NULL,
                            ANTAL TEXT NOT NULL,
                            N_UDLAAN TEXT NOT NULL,
                            RESERVEREDE TEXT NOT NULL,
                            AARSTAL TEXT NOT NULL,
                            SKABER TEXT NOT NULL,
                            FORMATTYPE TEXT NOT NULL,
                            TIDSBEGRAENSNING TEXT NOT NULL)''')
        self.statusEcho('Tabellerne Materialer, Bog, Film, CD og DRMLicens er oprettet')
        # commit SQL i databasen
        self.conn.commit()

    # metode sender SQL kode til databasen
    def runSQL(self, sqlInjection):
        # self.statusEcho(sqlInjection)
        self.cursor.execute(sqlInjection)
        self.conn.commit()

    # metode der returnerer en liste af objekter af typen Bog hvor attributterne er taget fra databasen
    # - medtaget for at teste min database.
    def makeAllBooks(self):
        bogliste = []
        # append bøger til bogliste
        for row in self.conn.execute(f'SELECT * FROM BOG'):
            bogliste.append(Bog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]).toString())
        return bogliste

    # metode der returnerer en liste af objekter af typen Film hvor attributterne er taget fra databasen
    # - medtaget for at teste min database.
    def makeAllFilms(self):
        filmliste = []
        # append film til filmliste
        for row in self.conn.execute(f'SELECT * FROM FILM'):
            filmliste.append(Film(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]).toString())
        return filmliste

    # metode der returnerer en liste af objekter af typen CD hvor attributterne er taget fra databasen
    # - medtaget for at teste min database.
    def makeAllCDs(self):
        cdliste = []
        # append bøger til bogliste
        for row in self.conn.execute(f'SELECT * FROM CD'):
            cdliste.append(CD(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]).toString())
        return cdliste

    # metode der returnerer en liste af objekter af typen DRMLicens hvor attributterne er taget fra databasen
    # - medtaget for at teste min database.
    def makeAllDRMs(self):
        drmliste = []
        # append bøger til bogliste
        for row in self.conn.execute(f'SELECT * FROM DRMLICENS'):
            drmliste.append(DRMLicens(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]).toString())
        return drmliste
    # metode der nulstiller databasen, dvs dropper alle tables. Da denne klasse kun er en lille test, er det
    # lidt nemmere for mig at droppe alle tabeller i databasen inden jeg gemmer mine testdata hver gang jeg starter mit
    # program.

    def cleanDB(self):
        # dropper følgende tabeller
        self.cursor.execute('DROP TABLE IF EXISTS BOG')
        self.cursor.execute('DROP TABLE IF EXISTS FILM')
        self.cursor.execute('DROP TABLE IF EXISTS CD')
        self.cursor.execute('DROP TABLE IF EXISTS DRMLICENS')
        # udfører
        self.conn.commit()
        self.statusEcho('Databasen er ren')

    # metode der lukker forbindelsen til databasen
    def closeDB(self):
        self.conn.close()
        self.statusEcho('forbindelsen til databasen er lukket')

    # Metode der printer en besked
    def statusEcho(self, msgString):
        print(msgString)

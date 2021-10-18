# Parent klasse. Indeholder de atributter der er fælles for alle klasser samt metoder der håndterer disse.
# Jeg har tilføjet metoder til at lave SQL kode som jeg kan bruge i min dbHandler - klasse.
# TODO tilføj funktionalitet til fuldt database baseret program
class Materiale:
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede

    # Metode der returnerer en boolean hvorvidt materialet er ledigt for udlån. Den ligger her fordi den er ens
    # for alle children af Materiale
    def isAvailable(self):
        if self.antal > self.n_udlaan + self.reserverede:
            return True
        else:
            return False


# Child klasse. Arver fra Materiale de atributter og metoder der er fælles for alle klasser
class Bog(Materiale):
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal, n_sider, forfatter):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede
        self.n_sider = n_sider
        self.forfatter = forfatter

    # funktion der returnerer en streng med alle klassens attributter
    def toString(self):
        return f'ID:{self.idnr} (Bog) {self.titel}({self.aarstal}), {self.forfatter}, ({self.n_sider} sider), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'

    # funktion der laver en SQL der indsætter attributter i den korrekte tabel i min database
    def toSQL(self, sqltype):
        if sqltype == 'insert':
                return f"INSERT INTO BOG (ID,TITEL,ANTAL,N_UDLAAN,RESERVEREDE,AARSTAL,N_SIDER,FORFATTER) " \
                   f"VALUES ({self.idnr}, '{self.titel}', '{self.antal}', '{self.n_udlaan}', '{self.reserverede}', " \
                   f"'{self.aarstal}', '{self.n_sider}', '{self.forfatter}')"
        if sqltype == 'selectall':
            return 'SELECT * FROM BOG'

# Child klasse. Arver fra Materiale de attributter og metoder der er fælles for alle klasser
class Film(Materiale):
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal, instruktoer, varighed):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede
        self.instruktoer = instruktoer
        self.varighed = varighed

    # funktion der returnerer en streng med alle klassens attributter
    def toString(self):
        return f'ID:{self.idnr} (Film) {self.titel}({self.aarstal}), {self.instruktoer}, ({self.varighed} minutter), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'

    # funktion der laver en SQL alt efter hvilken type ønsker
    def toSQL(self, sqltype):
        if sqltype == 'insert':
            return f"INSERT INTO FILM (ID,TITEL,ANTAL,N_UDLAAN,RESERVEREDE,AARSTAL,INSTRUKTOER,VARIGHED) " \
                   f"VALUES ({self.idnr}, '{self.titel}', '{self.antal}', '{self.n_udlaan}', '{self.reserverede}', " \
                   f"'{self.aarstal}', '{self.instruktoer}', '{self.varighed}')"
        if sqltype == 'selectall':
            return 'SELECT * FROM FILM'
# Child klasse. Arver fra Materiale de atributter og metoder der er fælles for alle klasser
class CD(Materiale):
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal, kunstner, tracks, total_varighed):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede
        self.kunstner = kunstner
        self.tracks = tracks
        self.total_varighed = total_varighed

    # funktion der returnerer en streng med alle klassens atributter
    def toString(self):
        return f'ID:{self.idnr} (CD) {self.titel}({self.aarstal}), {self.kunstner}, Tracks {self.tracks}({self.total_varighed} minutter), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'

    # funktion der laver en SQL der indsætter attributter i den korrekte tabel i min database
    def toSQL(self, sqltype):
        if sqltype == 'insert':
            return f"INSERT INTO CD (ID,TITEL,ANTAL,N_UDLAAN,RESERVEREDE,AARSTAL,KUNSTNER,TRACKS,TOTAL_VARIGHED) " \
                   f"VALUES ({self.idnr}, '{self.titel}', '{self.antal}', '{self.n_udlaan}', '{self.reserverede}', " \
                   f"'{self.aarstal}', '{self.kunstner}', '{self.tracks}', '{self.total_varighed}')"
        if sqltype == 'selectall':
            return 'SELECT * FROM CD'

# Child klasse. Arver fra Materiale de atributter og metoder der er fælles for alle materialer
class DRMLicens(Materiale):
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal, skaber, formattype, tidsbegraensning):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede
        self.skaber = skaber
        self.formattype = formattype
        self.tidsbegraensning = tidsbegraensning

    # funktion der returnerer en streng med alle klassens atributter
    def toString(self):
        return f'ID:{self.idnr} ({self.formattype}) {self.titel}({self.aarstal}), {self.skaber}, ({self.tidsbegraensning}' \
               f' dage), Tilgængelighed {self.n_udlaan}/{self.antal}'

    # funktion der laver en SQL der indsætter attributter i den korrekte tabel i min database
    def toSQL(self, sqltype):
        if sqltype == 'insert':
            return f"INSERT INTO DRMLICENS (ID,TITEL,ANTAL,N_UDLAAN,RESERVEREDE,AARSTAL,SKABER,FORMATTYPE,TIDSBEGRAENSNING) " \
                   f"VALUES ({self.idnr}, '{self.titel}', '{self.antal}', '{self.n_udlaan}', '{self.reserverede}', " \
                   f"'{self.aarstal}', '{self.skaber}', '{self.formattype}', '{self.tidsbegraensning}')"
        if sqltype == 'selectall':
            return 'SELECT * FROM DRMLICENS'

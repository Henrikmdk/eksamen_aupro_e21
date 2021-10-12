# Parent klasse. Indeholder de atributter der er fælles for alle klasser samt metoder der håndterer disse
import self as self
class Materiale:
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, aarstal):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede

    # Funktion der returnerer en boolean hvorvidt materialet er ledigt for udlån
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


    def toString(self):
        return f'ID:{self.idnr} (Bog) {self.titel}({self.aarstal}), {self.forfatter}, ({self.n_sider} sider), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'
# Child klasse. Arver fra Materiale de atributter og metoder der er fælles for alle klasser
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


    def toString(self):
        return f'ID:{self.idnr} (Film) {self.titel}({self.aarstal}), {self.instruktoer}, ({self.varighed} minutter), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'



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


    def toString(self):
        return f'ID:{self.idnr} (CD) {self.titel}({self.aarstal}), {self.kunstner}, Tracks {self.tracks}({self.total_varighed} minutter), ' \
               f' Tilgængelighed {self.n_udlaan}/{self.antal}, Reserverede: {self.reserverede}'


# Child klasse. Arver fra Materiale de atributter og metoder der er fælles for alle materialer
class DRMLicens(Materiale):
    def __init__(self, idnr, titel, antal, n_udlaan, reserverede, skaber, aarstal, formattype, tidsbegraensning):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.n_udlaan = n_udlaan
        self.aarstal = aarstal
        self.reserverede = reserverede
        self.skaber = skaber
        self.formattype = formattype
        self.tidsbegraensning = tidsbegraensning


    def toString(self):
        return f'ID:{self.idnr} ({self.formattype}) {self.titel}({self.aarstal}), {self.skaber}, ({self.tidsbegraensning}' \
               f' dage), Tilgængelighed {self.n_udlaan}/{self.antal}'

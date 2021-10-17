# Import af moduler
import calendar
import datetime
import time
import tkinter
from tkinter import *
from tkinter.messagebox import askyesno, showinfo, showwarning
# Import af mine egne moduler
from klasser import Bog, Film, CD, DRMLicens
from dbHandler import dbHandler

# Testdata - objekter instansieret direkte i en liste
listMaterialer = [Bog(1, 'The Silver Spoon', 10, 3, 0, 2011, 1505, 'Il Cucchiaio d’Argento'),
                  Bog(2, 'The Fat Duck Cookbook', 2, 2, 12, 2009, 532, 'Heston Blumenthal'),
                  Bog(3, 'Joy of Cooking, 1st edition', 1, 1, 5, 1931, None, 'Irma S. Rombauer'),
                  Film(4, 'Dune', 5, 0, 0, 1984, 'David Lynch', 137),
                  Film(5, '12 Angry Men', 2, 0, 0, 1957, 'Sidney Lumet', 96),
                  Film(6, 'Apocalypse Now', 5, 2, 0, 1979, 'Francis Ford Coppola', 147),
                  CD(7, 'The Number of the Beast', 3, 2, 0, 1982, 'Iron Maiden', 8, 39),
                  CD(8, 'A Night at the Opera', 2, 2, 4, 1975, 'Queen', 12, 43),
                  CD(9, 'Back in Black', 12, 12, 9, 1980, 'AC/DC', 10, 42),
                  DRMLicens(10, 'Alle mine morgener på jorden: Mit autodidakte liv', 5, 3, 0, 2017, 'Troels Kløvedal',
                            'Lydbog', 14),
                  DRMLicens(11, 'Gør det selv nr 10', 5, 2, 0, 'Bonniers', 2021, 'Online Magasin', 14),
                  DRMLicens(12, 'The Third man', 5, 5, 2, 1949, 'Orson Welles', 'Online Film', 1)
                  ]
# Backup af Testdata
# Initialiserer db
handler = dbHandler('examen.db')
# Laver databasestruktur
handler.makeStructure()
# Opret test-data i db ved at itterere igennem vores listMaterialer
for materiale in listMaterialer:
    handler.runSQL(materiale.toSQL('insert'))

# denne klasse er blevet meget omfattende, så
    # todo til næste update: lav en MAIN.py og flyt funktionalitet
    #  der ikke er gui relateret over i denne og importer gui (eksamen_aupro_e21 omdøbes til gui_.py), klasser,
    #  dbHandler moduler derfra og læg ligeledes testdata der. Giver bedre kode...
class Application(Frame):
    # lille funktion der sætter dato og klokkeslæt ind i GUI listen så vi kan se alderen på den viste data. Nyttigt ved
    # flerbruger applikationer der ikke har reservationshåndtering på data der bliver tilgået.
    # Dvs at brugeren selv må vurdere om det materiale han eller hun har kigget på i 2 timer stadig er ledigt for
    # udlån...
    def timestamp(self):
        timestamp = calendar.timegm(time.gmtime())
        human_readable = datetime.datetime.fromtimestamp(timestamp).isoformat()
        self.listGui.insert(INSERT, human_readable + '\n' + '\n')

    #  funktion der håndterer udlån af materialer
    def udlaan(self):
        # Fanger brugerens input fra tekstfeltet
        idnr = self.id_entry.get()
        # Flag der sættes til True hvis materialet bliver fundet
        found = False
        print("id der skal lånes: " + idnr)
        # Her udlånes det korrekte materiale
        # Iteration igennem alle materialer
        # hvis det rigtige materiale findes
        # - og hvis der er ledige eksemplarer på hylden - opskrives n_udlaan med 1
        # ellers får brugeren en prompt for reservation
        # hvis ja - reserveres materialet - reservationer opskrives med 1
        # Opdaterer tekst listen med nye data
        # Hvis brugeren prøver at udlåne et materiale på et ugyldigt eller ikke eksiterende id, promptes en fejlmedd.

        for materiale in listMaterialer:
            if materiale.idnr == int(idnr):
                # Flag der sættes til True hvis materialet bliver fundet
                found = True
                if materiale.isAvailable():
                    materiale.n_udlaan += 1
                    self.vis_hele_listen("test_data")
                else:
                    answer = askyesno('Hovsa', 'Alle eksemplarer er desværre udlånt - vil du reservere ?')
                    if answer:
                        materiale.reserverede += 1
                        print(f'Du har reserveret {materiale.toString()}')
                    print('Alle eksemplarer er udlånte')
        if not found:
            tkinter.messagebox.showwarning('Udlån', 'Materiale eksisterer ikke - indtast korrekt id eller'
                                                    ' kontakt en bibliotekar')

    # Funktion der håndterer aflevering af materialer
    def aflever(self):
        # Fanger brugerens input fra tekstfeltet
        idnr = self.aflever_entry.get()
        print("id der skal afleveres: " + idnr)
        # Her afleveres det korrekte materiale
        # Iteration igennem alle materialer
        # hvis det rigtige materiale findes
        # - og hvis det er udlånt mere end 0 gange
        # afleveres materialet og n_udlaan nedskrives med 1
        # ellers får brugeren en promt hvis materialet ikke er registreret som udlånt
        # Opdaterer tekstlisten med nye data
        for materiale in listMaterialer:
            if materiale.idnr == int(idnr):
                if materiale.n_udlaan > 0:
                    materiale.n_udlaan -= 1
                    print('Din aflevering er registreret')
                    self.vis_hele_listen("test_data")
                else:
                    print('Materialet kan ikke afleveres - kontakt venligst en bibliotekar')
                    tkinter.messagebox.showwarning('Materiale ikke udlånt!', 'Kontakt venligst en bibliotekar')

    # Funktion der håndterer søgning i listMaterialer
    def sog_i_listen(self):
        search_text = self.entry.get()
        print("søge tekst: " + search_text)

        # Flag der sættes til True hvis materialet bliver fundet
        found = False

        # linjen nedenunder sletter hele listen i GUI'en
        self.listGui.delete('1.0', END)

        # Iteration igennem toString() metoden for alle elementer i listMaterialer. Jeg søger på enhver forekomst af
        # søgetesktsten i lowcase returværdien af funktionen.
        if search_text:
            for materiale in listMaterialer:
                if search_text.lower() in materiale.toString().lower():
                    found = True
                    self.listGui.insert(INSERT, materiale.toString() + '\n')

            # Hvis der ikke er match, prompt!
            if not found:
                self.listGui.insert(INSERT, 'Ingen resultater fundet, prøv igen!\n')
                tkinter.messagebox.showinfo('Søg materiale', 'Ingen resultater fundet!')
                # opdater listen igen
                self.vis_hele_listen("test_data")
        else:
           tkinter.messagebox.showinfo('Søg i materialer', 'Du skal indtaste i søgefeltet, din søgning er tom!')

    # Funktion der håndterer opdatering af tekstfeltet listGui. Kaldes fra to knapper i GUI og sender 'souce' som
    # parameter så jeg i funktionen kan afgøre hvor den viste data skal komme fra: listMaterialer eller den embeddede
    # database 'examen.db'
    def vis_hele_listen(self, source):
        if source == 'test_data':
            # linjen nedenunder sletter hele listen i GUI'en
            self.listGui.delete('1.0', END)
            # Timestamp og kilde indsættes øverst i listen
            self.timestamp()
            self.listGui.insert(INSERT, source.upper() + '\n' + '\n')
            # Indsæt alt materiale i listen fra listMaterialer
            for materiale in listMaterialer:
                self.listGui.insert(INSERT, materiale.toString() + '\n')
        elif source == 'database':
            # linjen nedenunder sletter hele listen i GUI'en
            self.listGui.delete('1.0', END)
            # Timestamp og kilde indsættes øverst i listen
            self.timestamp()
            self.listGui.insert(INSERT, source.upper() + '\n' + '\n')
            # Indsæt alt materiale i listen fra databasen - lidt kluntet lavet, men det virker!
            for item in handler.makeAllBooks():
                self.listGui.insert(INSERT, f'{item}\n')
            for item in handler.makeAllFilms():
                self.listGui.insert(INSERT, f'{item}\n')
            for item in handler.makeAllCDs():
                self.listGui.insert(INSERT, f'{item}\n')
            for item in handler.makeAllDRMs():
                self.listGui.insert(INSERT, f'{item}\n')

    # funktion der håndterer sletning af materiale
    def slet_materiale(self):
        input_int = int(self.slet_entry.get())
        print(f"Materiale ID for sletning: {input_int}")

        # Flag der sættes til True hvis materialet bliver fundet
        found = False

        # Iteration igennem alle elementer i listMaterialer. Jeg søger på forekomst af
        # søgetesktsten på positionen i listen der indeholder materialets ID
        for entry in listMaterialer:
            if input_int == entry.idnr:
                found = True
                if askyesno("Sletning af materiale", f"Bekræft sletning af: {input_int}"):
                    listMaterialer.remove(entry)
                    self.vis_hele_listen('test_data')

        # Hvis der ikke er match, prompt!
        if not found:
            self.listGui.insert(INSERT, 'Ingen resultater fundet, prøv igen!\n')
            self.tkinter.messagebox.showinfo('Slet materiale', 'Ingen resultater fundet!')

    # Her initialiseres alle elementer i GUI
    def create_widgets(self):
        frame = Frame(self)
        frame2 = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="Afslut")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen. Jeg har ændret knappen så jeg kan kalde funktioner med
        # parametre og udkommenteret den oprindelige "command" -tildeling
        self.visListe = Button(frame, text="Vis hele listen", command=lambda: self.vis_hele_listen("test_data"))
        # self.visListe["command"] = self.vis_hele_listen('test_data')
        self.visListe.pack({"side": "left"})

        # definition af input søge feltet.
        self.L1 = Label(frame, text="Søge Streng")
        self.L1.pack(side=LEFT)
        self.entry = Entry(frame, bd=5)
        self.entry.pack(side=LEFT)

        # definition og mapping af søgeknappen.
        self.sogKnap = Button(frame, text="Søg i listen")
        self.sogKnap["command"] = self.sog_i_listen
        self.sogKnap.pack({"side": "left"})

        # definition af ID input feltet til udlån
        self.L1 = Label(frame, text="ID for udlån")
        self.L1.pack(side=LEFT)
        self.id_entry = Entry(frame, bd=5)
        self.id_entry.pack(side=LEFT)

        # definition af udlåns knappen og mapping til
        # en funktion.
        self.udlaanKnap = Button(frame, text="Udlån")
        self.udlaanKnap["command"] = self.udlaan
        self.udlaanKnap.pack({"side": "left"})

        # input felt til aflevering.
        self.L1 = Label(frame, text="ID for aflevering:")
        self.L1.pack(side=LEFT)
        self.aflever_entry = Entry(frame, bd=5)
        self.aflever_entry.pack(side=LEFT)

        # definition og mapping af afleveringsknap
        self.afleverKnap = Button(frame, text="Aflever")
        self.afleverKnap["command"] = self.aflever
        self.afleverKnap.pack({"side": "left"})

        # tilføjelse til udleveret GUI: et tekstfelt med tilhørende label og en knap med en slet funktion
        # definition af input feltet til slet, samt en knap til at teste min database ved at opdatere Text() listen
        # med data fra DB
        self.L1 = Label(frame2, text="ID for slet")
        self.L1.pack(side=LEFT)
        self.slet_entry = Entry(frame2, bd=5)
        self.slet_entry.pack(side=LEFT)

        # definition og mapping af slet knap
        self.sletKnap = Button(frame2, text="Slet materiale")
        self.sletKnap["command"] = self.slet_materiale
        self.sletKnap.pack(side=LEFT)

        # definition og mapping af test db knap. Jeg har ændret knappen så jeg kan kalde funktioner med
        # parametre og udkommenteret den oprindelige "command" -tildeling
        self.dbKnap = Button(frame2, text="Backup til DB", command=lambda: self.vis_hele_listen("database"))
        # self.dbKnap["command"] = self.vis_hele_listen('database')
        self.dbKnap.pack(side=LEFT)

        # Her definerer vi en Text widget - dvs
        # den kan indeholde multiple linjer
        # ideen er så at hver linje indeholde et styk materiale
        # Nedenunder kan du se hvordan listen af materiale løbes
        # igennem og toString metoden bliver kaldt og så bliver
        # der indsat en ny linje i Text widgeten
        self.listGui = Text(self, width=140)
        # Timestamp der sætter etn dato og tid over den viste data
        self.timestamp()
        # Opdaterer listGUI med testdata ved at iterere gennem listMaterialer
        self.vis_hele_listen("test_data")

        frame.pack()
        frame2.pack()
        self.listGui.pack()

    # Denne constructor køres når programmet starter
    # og sørger for at alle vores widgets bliver lavet.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()

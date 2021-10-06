from tkinter import *


# TODO - du skal have initialiseret nogle bogobjekter og nogle filmobjekter
# og sat ind i listen - Lav minimum 3 af hver type -
# og husk at give dem alle et forskelligt ID - som skal bruges til
# at udlåne det.
listMaterialer = []


class Application(Frame):

    def udlaan(self):
        idnr = self.id_entry.get()
        print("id der skal lånes: " + idnr)
        # TODO - her skal du have udlånt det korrekte materiale.
        # med det korrekte id og opdater objektet.

    def aflever(self):
        idnr = self.aflever_entry.get()
        print("id der skal afleveres: " + idnr)
        # TODO - her skal du have afleveret det korrekte materiale
        # med det korrekte id og så opdater det objekt.

    def sog_i_listen(self):
        search_text = self.entry.get()
        print("søge tekst: "+search_text)
        # TODO Nu skal listen af materiale søges igennem og
        # de materialer som matcher (dvs. hvor søgestrengen indgår som
        # en delstring) skal nu vises i listen og altså IKKE alle
        # materialer. Så du kan få brug for at slette det som
        # allerede står i vinduet og så tilføje de materialer
        # som matcher.

    def vis_hele_listen(self):
        print("Vis hele listen")
        # linjen nedenunder sletter hele listen i GUI'en
        # Den være være nyttig andre steder.....
        self.listGui.delete('1.0', END)
        # TODO - nu skal du vise HELE listen af materialer igen

    def create_widgets(self):
        frame = Frame(self)
        self.winfo_toplevel().title("Biblioteks databasen")

        # definition af quit knap
        self.QUIT = Button(frame, text="QUIT")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

        # definition og mapping af vis hele listen knappen
        self.visListe = Button(frame,text="Vis hele listen")
        self.visListe["command"] = self.vis_hele_listen
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

        # Her definerer vi en Text widget - dvs
        # den kan indeholde multiple linjer
        # ideen er så at hver linje indeholde et styk materiale
        # Nedenunder kan du se hvordan listen af materiale løbes
        # igennem og toString metoden bliver kaldt og så bliver
        # der indsat en ny linje i Text widgeten
        self.listGui = Text(self, width=140)
        for materiale in listMaterialer:
            self.listGui.insert(INSERT, materiale.toString()+"\n")
        frame.pack()
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
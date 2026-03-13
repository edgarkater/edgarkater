import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class NotenberechnungApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notenberechnung")

        # Datenmodell
        self.daten = {"klassen": []}

        # Aktuelle Klasse
        self.aktuelle_klasse = None

        # GUI erstellen
        self.create_widgets()

    def create_widgets(self):
        # Notebook für Tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        # Tab 1: Klassen verwalten
        tab_klassen = ttk.Frame(notebook)
        notebook.add(tab_klassen, text="Klassen verwalten")

        tk.Label(tab_klassen, text="Name der Klasse:").pack()
        self.klasse_name_entry = tk.Entry(tab_klassen)
        self.klasse_name_entry.pack()

        tk.Button(tab_klassen, text="Klasse hinzufügen", command=self.klasse_hinzufuegen).pack()
        tk.Button(tab_klassen, text="Klasse auswählen", command=self.klasse_auswaehlen).pack()

        self.klasse_listbox = tk.Listbox(tab_klassen)
        self.klasse_listbox.pack(fill="both", expand=True)

        # Tab 2: Schüler verwalten
        tab_schueler = ttk.Frame(notebook)
        notebook.add(tab_schueler, text="Schüler verwalten")

        tk.Label(tab_schueler, text="Name des Schülers:").pack()
        self.schueler_name_entry = tk.Entry(tab_schueler)
        self.schueler_name_entry.pack()

        tk.Button(tab_schueler, text="Schüler hinzufügen", command=self.schueler_hinzufuegen).pack()

        self.schueler_listbox = tk.Listbox(tab_schueler)
        self.schueler_listbox.pack(fill="both", expand=True)

        # Tab 3: Fächer und Kategorien verwalten
        tab_faecher = ttk.Frame(notebook)
        notebook.add(tab_faecher, text="Fächer/Kategorien verwalten")

        tk.Label(tab_faecher, text="Fach:").pack()
        self.fach_name_entry = tk.Entry(tab_faecher)
        self.fach_name_entry.pack()

        tk.Button(tab_faecher, text="Fach hinzufügen", command=self.fach_hinzufuegen).pack()

        tk.Label(tab_faecher, text="Kategorie:").pack()
        self.kategorie_name_entry = tk.Entry(tab_faecher)
        self.kategorie_name_entry.pack()

        tk.Label(tab_faecher, text="Gewicht:").pack()
        self.kategorie_gewicht_entry = tk.Entry(tab_faecher)
        self.kategorie_gewicht_entry.pack()

        tk.Button(tab_faecher, text="Kategorie hinzufügen", command=self.kategorie_hinzufuegen).pack()

        self.fach_listbox = tk.Listbox(tab_faecher)
        self.fach_listbox.pack(fill="both", expand=True)

        self.kategorie_listbox = tk.Listbox(tab_faecher)
        self.kategorie_listbox.pack(fill="both", expand=True)

        # Tab 4: Noten eingeben
        tab_noten = ttk.Frame(notebook)
        notebook.add(tab_noten, text="Noten eingeben")

        tk.Label(tab_noten, text="Schüler:").pack()
        self.note_schueler_combobox = ttk.Combobox(tab_noten)
        self.note_schueler_combobox.pack()

        tk.Label(tab_noten, text="Fach:").pack()
        self.note_fach_combobox = ttk.Combobox(tab_noten)
        self.note_fach_combobox.pack()

        tk.Label(tab_noten, text="Kategorie:").pack()
        self.note_kategorie_combobox = ttk.Combobox(tab_noten)
        self.note_kategorie_combobox.pack()

        tk.Label(tab_noten, text="Note (1-15):").pack()
        self.note_wert_entry = tk.Entry(tab_noten)
        self.note_wert_entry.pack()

        tk.Button(tab_noten, text="Note eintragen", command=self.note_eintragen).pack()

        # Tab 5: Gesamtnote berechnen
        tab_ergebnis = ttk.Frame(notebook)
        notebook.add(tab_ergebnis, text="Gesamtnote berechnen")

        tk.Button(tab_ergebnis, text="Gesamtnote berechnen", command=self.gesamtnote_berechnen).pack()

        self.ergebnis_text = tk.Text(tab_ergebnis)
        self.ergebnis_text.pack(fill="both", expand=True)

        # Tab 6: Daten speichern/exportieren
        tab_daten = ttk.Frame(notebook)
        notebook.add(tab_daten, text="Daten speichern/exportieren")

        tk.Button(tab_daten, text="Daten speichern", command=self.daten_speichern).pack()
        tk.Button(tab_daten, text="Daten laden", command=self.daten_laden).pack()
        tk.Button(tab_daten, text="Als PDF exportieren", command=self.als_pdf_exportieren).pack()

    # Funktionen
    def klasse_hinzufuegen(self):
        name = self.klasse_name_entry.get()
        if name:
            self.daten["klassen"].append({"name": name, "schueler": [], "faecher": []})
            self.klasse_listbox.insert(tk.END, name)
            self.klasse_name_entry.delete(0, tk.END)

    def klasse_auswaehlen(self):
        selection = self.klasse_listbox.curselection()
        if selection:
            index = selection[0]
            self.aktuelle_klasse = self.daten["klassen"][index]
            self.aktualisiere_listen()

    def schueler_hinzufuegen(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        name = self.schueler_name_entry.get()
        if name:
            self.aktuelle_klasse["schueler"].append({"name": name, "noten": {}})
            self.schueler_listbox.insert(tk.END, name)
            self.note_schueler_combobox["values"] = [s["name"] for s in self.aktuelle_klasse["schueler"]]
            self.schueler_name_entry.delete(0, tk.END)

    def fach_hinzufuegen(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        name = self.fach_name_entry.get()
        if name:
            self.aktuelle_klasse["faecher"].append({"name": name, "noten_kategorien": []})
            self.fach_listbox.insert(tk.END, name)
            self.note_fach_combobox["values"] = [fach["name"] for fach in self.aktuelle_klasse["faecher"]]
            self.fach_name_entry.delete(0, tk.END)

    def kategorie_hinzufuegen(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        fach_selection = self.fach_listbox.curselection()
        if not fach_selection:
            messagebox.showerror("Fehler", "Bitte zuerst ein Fach auswählen!")
            return

        fach_index = fach_selection[0]
        fach = self.aktuelle_klasse["faecher"][fach_index]

        name = self.kategorie_name_entry.get()
        gewicht_text = self.kategorie_gewicht_entry.get()

        if name and gewicht_text:
            try:
                gewicht = float(gewicht_text)
                fach["noten_kategorien"].append({"name": name, "gewicht": gewicht})
                self.kategorie_listbox.insert(tk.END, f"{name} (Gewicht: {gewicht})")
                self.note_kategorie_combobox["values"] = [k["name"] for k in fach["noten_kategorien"]]
                self.kategorie_name_entry.delete(0, tk.END)
                self.kategorie_gewicht_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Fehler", "Gewicht muss eine Zahl sein!")

    def note_eintragen(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        schueler_name = self.note_schueler_combobox.get()
        fach_name = self.note_fach_combobox.get()
        kategorie_name = self.note_kategorie_combobox.get()
        note_text = self.note_wert_entry.get()

        if schueler_name and fach_name and kategorie_name and note_text:
            try:
                note = float(note_text)
                if 1 <= note <= 15:
                    # Suche den Schüler
                    schueler = None
                    for s in self.aktuelle_klasse["schueler"]:
                        if s["name"] == schueler_name:
                            schueler = s
                            break

                    if not schueler:
                        messagebox.showerror("Fehler", "Schüler nicht gefunden!")
                        return

                    # Suche das Fach
                    fach = None
                    for f in self.aktuelle_klasse["faecher"]:
                        if f["name"] == fach_name:
                            fach = f
                            break

                    if not fach:
                        messagebox.showerror("Fehler", "Fach nicht gefunden!")
                        return

                    # Suche die Kategorie
                    kategorie = None
                    for k in fach["noten_kategorien"]:
                        if k["name"] == kategorie_name:
                            kategorie = k
                            break

                    if not kategorie:
                        messagebox.showerror("Fehler", "Kategorie nicht gefunden!")
                        return

                    # Note eintragen
                    if fach_name not in schueler["noten"]:
                        schueler["noten"][fach_name] = {}

                    schueler["noten"][fach_name][kategorie_name] = note
                    messagebox.showinfo("Erfolg", "Note erfolgreich eingetragen!")
                    self.note_wert_entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Fehler", "Note muss zwischen 1 und 15 liegen!")
            except ValueError:
                messagebox.showerror("Fehler", "Note muss eine Zahl sein!")

    def gesamtnote_berechnen(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        self.ergebnis_text.delete(1.0, tk.END)
        for schueler in self.aktuelle_klasse["schueler"]:
            gesamt_note = 0
            gesamt_gewicht = 0

            for fach_name, noten in schueler["noten"].items():
                # Suche das Fach in der Klasse
                fach = None
                for f in self.aktuelle_klasse["faecher"]:
                    if f["name"] == fach_name:
                        fach = f
                        break

                if fach:
                    for kategorie_name, note in noten.items():
                        # Suche die Kategorie im Fach
                        for k in fach["noten_kategorien"]:
                            if k["name"] == kategorie_name:
                                gesamt_note += note * k["gewicht"]
                                gesamt_gewicht += k["gewicht"]
                                break

            if gesamt_gewicht > 0:
                gesamt_note /= gesamt_gewicht
                self.ergebnis_text.insert(tk.END, f"{schueler['name']}: {gesamt_note:.2f}\n")
            else:
                self.ergebnis_text.insert(tk.END, f"{schueler['name']}: Keine Noten eingetragen\n")

    def daten_speichern(self):
        datei = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON-Dateien", "*.json")])
        if datei:
            with open(datei, "w") as f:
                json.dump(self.daten, f, indent=4)
            messagebox.showinfo("Erfolg", "Daten erfolgreich gespeichert!")

    def daten_laden(self):
        datei = filedialog.askopenfilename(filetypes=[("JSON-Dateien", "*.json")])
        if datei:
            with open(datei, "r") as f:
                self.daten = json.load(f)
            self.aktualisiere_listen()
            messagebox.showinfo("Erfolg", "Daten erfolgreich geladen!")

    def als_pdf_exportieren(self):
        if not self.aktuelle_klasse:
            messagebox.showerror("Fehler", "Bitte zuerst eine Klasse auswählen!")
            return

        datei = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF-Dateien", "*.pdf")])
        if datei:
            c = canvas.Canvas(datei, pagesize=A4)
            c.setFont("Helvetica", 16)
            c.drawString(50, 800, f"Notenübersicht: {self.aktuelle_klasse['name']}")

            y = 780
            for schueler in self.aktuelle_klasse["schueler"]:
                gesamt_note = 0
                gesamt_gewicht = 0

                for fach_name, noten in schueler["noten"].items():
                    # Suche das Fach in der Klasse
                    fach = None
                    for f in self.aktuelle_klasse["faecher"]:
                        if f["name"] == fach_name:
                            fach = f
                            break

                    if fach:
                        for kategorie_name, note in noten.items():
                            # Suche die Kategorie im Fach
                            for k in fach["noten_kategorien"]:
                                if k["name"] == kategorie_name:
                                    gesamt_note += note * k["gewicht"]
                                    gesamt_gewicht += k["gewicht"]
                                    break

                if gesamt_gewicht > 0:
                    gesamt_note /= gesamt_gewicht
                    c.setFont("Helvetica", 12)
                    c.drawString(50, y, f"{schueler['name']}: {gesamt_note:.2f}")
                    y -= 20
                else:
                    c.setFont("Helvetica", 12)
                    c.drawString(50, y, f"{schueler['name']}: Keine Noten eingetragen")
                    y -= 20

            c.save()
            messagebox.showinfo("Erfolg", "PDF erfolgreich exportiert!")

    def aktualisiere_listen(self):
        # Klassen
        self.klasse_listbox.delete(0, tk.END)
        for klasse in self.daten["klassen"]:
            self.klasse_listbox.insert(tk.END, klasse["name"])

        if not self.aktuelle_klasse:
            return

        # Schüler
        self.schueler_listbox.delete(0, tk.END)
        for schueler in self.aktuelle_klasse["schueler"]:
            self.schueler_listbox.insert(tk.END, schueler["name"])
        self.note_schueler_combobox["values"] = [s["name"] for s in self.aktuelle_klasse["schueler"]]

        # Fächer
        self.fach_listbox.delete(0, tk.END)
        for fach in self.aktuelle_klasse["faecher"]:
            self.fach_listbox.insert(tk.END, fach["name"])
        self.note_fach_combobox["values"] = [fach["name"] for fach in self.aktuelle_klasse["faecher"]]

        # Kategorien (leer, da fachabhängig)
        self.kategorie_listbox.delete(0, tk.END)
        self.note_kategorie_combobox["values"] = []

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = NotenberechnungApp(root)
    root.mainloop()

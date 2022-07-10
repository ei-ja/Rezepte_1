from tkinter import*
from tkinter import messagebox, simpledialog, Text
import sqlite3

connection = sqlite3.connect("rezepte.db")
cursor = connection.cursor()
try:
    sql = "CREATE TABLE rezepte(" \
                  "überschrift TEXT PRIMARY KEY, "\
                  "zutaten TEXT, " \
                  "zubereitung TEXT)"
    cursor.execute(sql)
except:
    pass

def root_neu_rezept():
    def add_neu_rezept():
        sql = "INSERT INTO rezepte VALUES('"+überschrift.get()+"', '"+zutaten.get("1.0", "end")+"','"+zubereitung.get("1.0", "end")+"')"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("", "Hinzugefügt")
    root2 = Tk()
    root2.title("Neues Rezept")
    root2.iconbitmap("icon.ico")
    früberschrift = Frame(root2)
    früberschrift.pack(side="left",padx=20,pady=20)
    frzutaten = Frame(root2)
    frzutaten.pack(side="left",padx=20,pady=20)
    frzubereitung = Frame(root2)
    frzubereitung.pack(side="left",padx=20,pady=20)
    lbüberschrift = Label(früberschrift, text="Überschrift: ")
    lbüberschrift.pack()
    überschrift = Entry(früberschrift, width=30)
    überschrift.pack()
    lbzutaten = Label(frzutaten, text="Zutaten (jede in einer Zeile):")
    lbzutaten.pack()
    zutaten = Text(frzutaten, width=30, height=30)
    zutaten.pack()
    lbzubereitung = Label(frzubereitung, text="Arbeitsanweisung (Jeder Satz in einer Zeile):")
    lbzubereitung.pack()
    zubereitung = Text(frzubereitung, width=60, height=25)
    zubereitung.pack()
    button = Button(root2, text="Absenden", command=add_neu_rezept)
    button.pack(side="right",padx=20,pady=20)

def root_anzeigen_rezept():
    connection = sqlite3.connect("rezepte.db")
    cursor = connection.cursor()
    begriff = simpledialog.askstring(" ", "Suchbegriff eingeben:")
    sql = "SELECT * FROM rezepte"
    text = ""
    cursor.execute(sql)
    for dsatz in cursor:
        if begriff.lower() in dsatz[0].lower():
            text += dsatz[0] + "\nZutaten:\n" + dsatz[1] + "\nZubereitung:\n"+ dsatz[2] + "\n \n"
    root3 = Tk()
    root3.title("Rezepte")
    t = Label(root3)
    t["text"] = text
    t.pack()

def rezept_löschen():
    name = simpledialog.askstring(" ", "Name des Rezeptes:")
    sql = "DELETE FROM rezepte WHERE überschrift = '"+name+"'"
    cursor.execute(sql)
    connection.commit()
    messagebox.showinfo("","Gelöscht")

def zutaten_bearbeiten():
    def zutaten_ändern():
        sql = "UPDATE rezepte SET zutaten = '"+zutaten.get("1.0", "end")+"' WHERE überschrift = '"+name+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("","Bearbeitet")
    name = simpledialog.askstring(" ", "Name des Rezeptes:")
    root4 = Tk()
    root4.title("Zutaten bearbeiten")
    root4.iconbitmap("icon.ico")
    zutaten = Text(root4, width=30, height=30)
    sql = "SELECT * FROM rezepte WHERE überschrift = '"+name+"'"
    cursor.execute(sql)
    for dsatz in cursor:
        zutaten.insert("1.0", dsatz[1])
    zutaten.pack(padx=20,pady=20)
    button = Button(root4, text="Ändern", command=zutaten_ändern)
    button.pack(padx=20,pady=20)

def zubereitung_bearbeiten():
    def zubereitung_ändern():
        sql = "UPDATE rezepte SET zubereitung = '"+zubereitung.get("1.0", "end")+"' WHERE überschrift = '"+name+"'"
        cursor.execute(sql)
        connection.commit()
        messagebox.showinfo("","Bearbeitet")
    name = simpledialog.askstring(" ", "Name des Rezeptes:")
    root5 = Tk()
    root5.title("Zubereitung bearbeiten")
    root5.iconbitmap("icon.ico")
    zubereitung = Text(root5, width=60, height=25)
    sql = "SELECT * FROM rezepte WHERE überschrift = '"+name+"'"
    cursor.execute(sql)
    for dsatz in cursor:
        zubereitung.insert("1.0", dsatz[2])
    zubereitung.pack(padx=20,pady=20)
    button = Button(root5, text="Ändern", command=zubereitung_ändern)
    button.pack(padx=20,pady=20)
    
root = Tk()
root.title("Rezepte")
root.iconbitmap("icon.ico")

b1 = Button(root, text="Neues Rezept", width=30, height=10, command=root_neu_rezept)
b1.pack(side="left", padx=30, pady=30)

b2 = Button(root, text="Rezepte anschauen", width=30, height=10, command=root_anzeigen_rezept)
b2.pack(side="left", padx=30, pady=30)

b3 = Button(root, text="Zutaten bearbeiten", width=30, height=10, command=zutaten_bearbeiten)
b3.pack(side="left", padx=30, pady=30)

b4 = Button(root, text="Zubereitung bearbeiten", width=30, height=10, command=zubereitung_bearbeiten)
b4.pack(side="left", padx=30, pady=30)

b5 = Button(root, text="Rezept löschen", width=30, height=10, command=rezept_löschen)
b5.pack(side="left", padx=30, pady=30)

root.mainloop()

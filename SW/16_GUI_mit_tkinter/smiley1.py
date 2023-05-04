# Drei Smileys untereinander darstellen

# Modul für die GUI-Erstellung importieren
import tkinter as tk

# Konstruktor für das Fenster aufrufen
root = tk.Tk()

# Bildausgabe erzeugen
bild1 = tk.PhotoImage(file="slightly_smiling_face.png")
label1 = tk.Label(root, image=bild1)

# in GUI Elemente einbetten
label1.pack()

# Bildausgabe erzeugen
bild2 = tk.PhotoImage(file="neutral_face.png")
label2 = tk.Label(root, image=bild2)

# in GUI Elemente einbetten
label2.pack()

# Bildausgabe erzeugen
bild3 = tk.PhotoImage(file="slightly_frowning_face.png")
label3 = tk.Label(root, image=bild3)

# in GUI Elemente einbetten
label3.pack()

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()

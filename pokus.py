import tkinter as tk

stav = {
    "seznam": [],
    "soucet": 0,
}

def pocitej_cisla():
    cislo_text = vstup.get().strip()
    
    try:
        cislo = int(cislo_text)
    except ValueError:
        chyba.config(text="Zadej celé číslo")
        vstup.select.range(0, tk.END)
        vstup.focus()
        return
    
    if operace.get() == "minus":
        cislo =- cislo
    
    stav["seznam"].append(str(cislo))
    stav["soucet"] += cislo
    
    if uloz_do_soubor.get():
        with open("cisla.txt", "a", encoding="utf-8") as f:
            f.write(f"{cislo}\n")
    
    lb_vystup.config(text=str(stav["soucet"]))
    novy_vypis = ",".join(stav["seznam"])
    
    entry_seznam.config(state="normal")
    entry_seznam.delete(0, tk.END)
    entry_seznam.insert(0, novy_vypis)
    entry_seznam.config(state="readonly")
    
    chyba.config(text="")
    
    vstup.select_range(0, tk.END)
    vstup.focus()
    
def resetuj():
    stav["seznam"] = []
    stav["soucet"] = 0
    lb_vystup.config(text="0")
    entry_seznam.config(state="normal")
    entry_seznam.delete(0, tk.END)
    entry_seznam.config(state="readonly")
    vstup.delete(0, tk.END)
    vstup.config(text="")
    vstup.focus()
    
okno = tk.Tk()
okno.title("Moje GUI okno")
okno.geometry("300x300")

lb_vstup = tk.Label(okno, text="Nové číslo")
lb_vstup.pack()

vstup = tk.Entry(okno)
vstup.pack()
vstup.bind("<Return>", lambda event: pocitej_cisla())

chyba = tk.Label(okno, text="", fg="red")
chyba.pack()

operace = tk.StringVar(value="plus")
tk.Radiobutton(okno, text="Přičíst", variable= operace, value="plus").pack()
tk.Radiobutton(okno, text="Odečíst", variable= operace, value="minus").pack()

uloz_do_soubor = tk.BooleanVar(value=True)
tk.Checkbutton(okno, text="Ukládání do souborů", variable=uloz_do_soubor).pack()

tlacitko = tk.Button(okno, text="Přidej číslo", command=pocitej_cisla)
tlacitko.pack()

tlacitko_resetuj = tk.Button(okno, text="Resetuj tlačítko", command=resetuj)
tlacitko_resetuj.pack()

lb_vystup_popis = tk.Label(okno, text="Součet čísel")
lb_vystup_popis.pack()

lb_vystup = tk.Label(okno, text="Seznam čísel")
lb_vystup.pack()

entry_seznam = tk.Entry(okno, state="readonly")
entry_seznam.pack()

vstup.focus()

okno.mainloop()
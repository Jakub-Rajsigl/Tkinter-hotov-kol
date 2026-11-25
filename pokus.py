import tkinter as tk

stav = {
    "seznam": [],
    "soucet": 0,
}

def pridej_cislo():
    cele_cislo = vstup.get().strip()

    try:
        cislo = int(cele_cislo)
    except ValueError:
        chyba.config(text="Zadej celé číslo")
        vstup.select.range(0, tk.END)
        vstup.focus()
        return
    
    stav["seznam"].append(str(cislo))
    stav["soucet"] += cislo
    
    lb_vystup.config(text=str(stav["soucet"]))
    novy_vypis = ",".join(stav["seznam"])
    
    entry_seznam.config(state="normal")
    entry_seznam.delete(0, tk.END)
    entry_seznam.insert(0, novy_vypis)
    entry_seznam.config(state="readonly")
    
    chyba.config(text="")
    
    vstup.select.range(0, tk.END)
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
okno.title("Nové GUI okno")
okno.geometry("300x300")

lb_vstup = tk.Label(okno, text= "Nové číslo")
lb_vstup.pack()

vstup = tk.Entry(okno)
vstup.pack()

chyba = tk.Label(okno, text="", fg="red")
chyba.pack()

tlacitko = tk.Button(okno, text="Přidej číslo", command=pridej_cislo)
tlacitko.pack()

tlacitko_reset = tk.Button(okno, text="Resetuj", command=resetuj)
tlacitko_reset.pack()

lb_vystup_popis = tk.Label(okno, text="Součet čísel")
lb_vystup_popis.pack()
 
lb_vystup = tk.Label(okno, text= "Nové číslo")
lb_vystup.pack()

lb_seznam = tk.Label(okno, text="Seznam čísel")
lb_seznam.pack()

entry_seznam = tk.Entry(okno, state="readonly")
entry_seznam.pack()

vstup.focus()

okno.mainloop()   
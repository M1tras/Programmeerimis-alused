import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Raami kood:
raam = tk.Tk()
raam.title("Kalkulaator")
raam.geometry("500x500")

# Soo valimine:
soo_valikud = ["Mees", "Naine"]
soo_tekst = Label(raam, text="Valige oma sugu: ")
soo_tekst.grid(row=0, column=0, padx=10, pady=10)

soo_valiku_kast = ttk.Combobox(raam, values=soo_valikud, width=10)
soo_valiku_kast.grid(row=0, column=2, padx=10, pady=10)
soo_valiku_kast.current(0)

# Kaalu märkimine:
kaalu_tekst = ttk.Label(raam, text="Sisestage oma kaal (Kg): ")
kaalu_tekst.grid(row=1, column=0, padx=10, pady=10)
kaalu_kast = ttk.Entry(raam)
kaalu_kast.grid(row=1, column=2, padx=10, pady=10)

# Pikkuse määramine:
pikkus_tekst = ttk.Label(raam, text="Sisestage oma pikkus(Cm): ")
pikkus_tekst.grid(row=2, column=0, padx=10, pady=10)
pikkus_kast = ttk.Entry(raam)
pikkus_kast.grid(row=2, column=2, padx=10, pady=10)

# Vanuse määramine:
vanuse_tekst = ttk.Label(raam, text="Sisestage oma vanus: ")
vanuse_tekst.grid(row=3, column=0, padx=10, pady=10)
vanuse_kast = ttk.Entry(raam)
vanuse_kast.grid(row=3, column=2, padx=10, pady=10)

# Aktiivsuse määramine:
aktiivsus_valikud = ["Istuv eluviis", "Väike aktiivsus", "Mõõdukas aktiivsus", "Kõrge aktiivsus", "Väga kõrge aktiivsus"]
aktiivsus_tekst = Label(raam, text="Valige oma aktiivsus tase: ")
aktiivsus_tekst.grid(row=4, column=0, padx=10, pady=10)

aktiivsus_valiku_kast = ttk.Combobox(raam, values=aktiivsus_valikud, width=20)
aktiivsus_valiku_kast.grid(row=4, column=2, padx=10, pady=10)
aktiivsus_valiku_kast.current(0)

# Eesmärgi valimine:
eesmarki_valikud = ["Kaalukaotus", "Kaalutõus"]
eesmark_tekst = Label(raam, text="Valige oma eesmärk: ")
eesmark_tekst.grid(row=5, column=0, padx=10, pady=10)

eesmarki_valiku_kast = ttk.Combobox(raam, values=eesmarki_valikud, width=10)
eesmarki_valiku_kast.grid(row=5, column=2, padx=10, pady=10)
eesmarki_valiku_kast.current(0)

# BMR arvutamine: (N = Naiste, M = Meeste)
def n_bmr(kaal, pikkus, vanus):
    n_bmr_start = 447.6
    n_bmr_kaal = 9.2 * kaal
    n_bmr_pikkus = 3.1 * pikkus
    n_bmr_vanus = 4.3 * vanus
    n_bmr_kokku = n_bmr_start + n_bmr_kaal + n_bmr_pikkus + n_bmr_vanus
    return n_bmr_kokku

def m_bmr(kaal, pikkus, vanus):
    m_bmr_start = 88.36
    m_bmr_kaal = 13.4 * kaal
    m_bmr_pikkus = 4.8 * pikkus
    m_bmr_vanus = 5.7 * vanus
    m_bmr_kokku = m_bmr_start + m_bmr_kaal + m_bmr_pikkus + m_bmr_vanus
    return m_bmr_kokku

# PAL arvutamine:
def pal(final_bmr, eluviis):
    if eluviis == "Istuv eluviis":
        pal_kcal = final_bmr * 1.2
    elif eluviis == "Väike aktiivsus":
        pal_kcal = final_bmr * 1.375
    elif eluviis == "Mõõdukas aktiivsus":
        pal_kcal = final_bmr * 1.55
    elif eluviis == "Kõrge aktiivsus":
        pal_kcal = final_bmr * 1.725
    elif eluviis == "Väga kõrge aktiivsus":
        pal_kcal = final_bmr * 1.9
    else:
        messagebox.showerror("Viga", "Vali õige aktiivsus tase!")
    return pal_kcal

# Eesmärgi järgi kalkulatsioonid:
def eesmark(pal_kcal, valitud_eesmärk):
    if valitud_eesmärk == "Kaalukaotus":
        em_kcal = pal_kcal - 500
    elif valitud_eesmärk == "Kaalutõus":
        em_kcal = pal_kcal + 250
    else:
        em_kcal = pal_kcal
    return em_kcal

# Function to validate user input
def valid_input():
    try:
        kaal = float(kaalu_kast.get())
        pikkus = float(pikkus_kast.get())
        vanus = int(vanuse_kast.get())
    except ValueError:
        messagebox.showerror("Viga", "Palun sisestage numbrilised väärtused kaalule, pikkusele ja vanusele.")
        return False
    
    if vanus < 0 or vanus > 120:
        messagebox.showerror("Viga", "Palun sisestage kehtiv vanus.")
        return False
    if pikkus < 54 or pikkus > 270:
        messagebox.showerror("Viga", "Palun sisestage kehtiv pikkus.")
        return False
    if kaal < 40 or kaal > 500:
        messagebox.showerror("Viga", "Palun sisestage kehtiv kaal.")
        return False
    return True

# Function to calculate everything when button is pressed
def arvuta_kalorid():
    # Validate inputs
    if not valid_input():
        return
    
    # Get values from input fields
    kaal = float(kaalu_kast.get())
    pikkus = float(pikkus_kast.get())
    vanus = int(vanuse_kast.get())
    
    sugu = soo_valiku_kast.get()
    eluviis = aktiivsus_valiku_kast.get()
    valitud_eesmärk = eesmarki_valiku_kast.get()
    
    # BMR kalkulatsioon.
    if sugu == "Mees":
        final_bmr = m_bmr(kaal, pikkus, vanus)
    elif sugu == "Naine":
        final_bmr = n_bmr(kaal, pikkus, vanus)
    else:
        messagebox.showerror("Viga", "Vali normaalne sugu")
        return

    # PAL kalkuleerimine:
    pal_kcal = pal(final_bmr, eluviis)

    # Calculate final kcal based on goal
    kcal = eesmark(pal_kcal, valitud_eesmärk)

    messagebox.showinfo("Kokkuvõte", f"Teie päevane kalorivajadus on: {kcal:.2f} kcal")
    
# Edasi mineku nupp:
arvuta_nupp = ttk.Button(raam, text="Jatka", command=arvuta_kalorid)
arvuta_nupp.grid(row=10, column=2, padx=30, pady=30)

raam.mainloop()

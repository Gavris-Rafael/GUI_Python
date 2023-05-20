import tkinter
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg)
from matplotlib.backends.backend_tkagg import (
     FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.figure
import numpy as np

from pvlib import pvsystem
import pandas as pd

from PIL import Image, ImageTk



def Afiseaza():
    if Model.get() == 'LG_Electronics_Inc__LG410N2W_A5':
        parameters = {
        'Name': 'LG_Electronics_Inc__LG410N2W_A5',
        'BIPV': 'N',
        'Date': '1/3/2019',
        'T_NOCT': 47.7,
        'A_c': 2.0,
        'N_s': 72,
        'I_sc_ref': 10.55,
        'V_oc_ref': 49.5,
        'I_mp_ref': 9.91,
        'V_mp_ref': 41.4,
        'alpha_sc': 0.003165,
        'beta_oc': -0.1287,
        'a_ref': 1.845517,
        'I_L_ref': 10.560924,
        'I_o_ref': 2.323845e-11,
        'R_s': 0.237774,
        'R_sh_ref': 229.651764,
        'Adjust': 11.573755,
        'gamma_r': -0.36,
        'Version': 'SAM 2018.11.11 r2',
        'PTC': 377.9,
        'Length': 5.08,
        'Width': 2.54,
        'Technology': 'Mono-c-Si',
        }
        Grafic(parameters)
        setareParametri(parameters)
    else: 
        if Model.get() == 'ECO_Future_ECO_290P72':
            parameters = {
            'Name': 'ECO_Future_ECO_290P72',
            'BIPV': 'N',
            'Date': '1/3/2019',
            'T_NOCT': 46.3,
            'A_c': 1.94,
            'N_s': 72,
            'I_sc_ref': 8.55,
            'V_oc_ref': 45.2,
            'I_mp_ref': 8.12,
            'V_mp_ref': 35.75,
            'alpha_sc': 0.007481,
            'beta_oc': -0.170901,
            'a_ref': 1.920896,
            'I_L_ref': 8.638638,
            'I_o_ref': 5.193898e-10,
            'R_s': 0.485357,
            'R_sh_ref': 1335.430786,
            'Adjust': -0.776848,
            'gamma_r': -0.4422,
            'Version': 'SAM 2018.11.11 r2',
            'PTC': 261.3,
            'Length': 4.95,
            'Width': 2.51,
            'Technology': 'Multi-c-Si',
            }
            Grafic(parameters)
            setareParametri(parameters)
        else:
            if Model.get() == 'Green_Energy_Technology_GET_180B':
                parameters = {
                'Name': 'Green_Energy_Technology_GET_180B',
                'BIPV': 'N',
                'Date': '1/3/2019',
                'T_NOCT': 44.3,
                'A_c': 2.86,
                'N_s': 216,
                'I_sc_ref': 1.5,
                'V_oc_ref': 193.96,
                'I_mp_ref': 1.22,
                'V_mp_ref': 147.6,
                'alpha_sc': 0.001455,
                'beta_oc': -0.67692,
                'a_ref': 7.403434,
                'I_L_ref': 1.545533,
                'I_o_ref': 5.225641e-12,
                'R_s': 19.760918,
                'R_sh_ref': 650.988953,
                'Adjust': -14.5147,
                'gamma_r': -0.259,
                'Version': 'SAM 2018.11.11 r2',
                'PTC': 169.2,
                'Length': 5.58,
                'Width': 3.3,
                'Technology': 'Thin Film',
                }
                Grafic(parameters)
                setareParametri(parameters)
            else:
                messagebox.showerror(title='Panou neales', message="Nu ai ales nici un panou din rubrica Alege Panoul!\nTe rog alege unul.")

def setareParametri(param):
    Tip.set(param['Technology'])
    Pmax.set(round((param['I_mp_ref']*param['V_mp_ref']),2))
    Vmp.set(param['V_mp_ref'])
    Imp.set(param['I_mp_ref'])
    Voc.set(param['V_oc_ref'])
    Isc.set(param['I_sc_ref'])
    Celule.set(param['N_s'])
    Lungime.set(param['Length'])
    Latime.set(param['Width'])
    Coef_Pmax.set(param['gamma_r'])
    Coef_Voc.set(param['beta_oc'])
    Coef_Isc.set(param['alpha_sc'])
    Rp.set(round(param['R_sh_ref'],2))
    Rs.set(round(param['R_s'],2))
    Ipv.set(round(param['I_L_ref'],2))
    Idealitate.set(round(param['a_ref'],2))
    I0.set(param['I_o_ref'])
    

def calculeazaAmor():
    if(int(Putere.get())<0  or  int(Sistem.get())<0 or float(Pret.get())<0 or int(Consum.get())<0 or int(Factura.get())<0):
        messagebox.showerror(title="Greseală!", message="Valorile trebuie să fie pozitive!")
    else:
        consum_cu_PV = 0.3 * int(Putere.get())
        curent_in_retea = 0.7 * int(Putere.get()) 

        curent_recuperat = curent_in_retea/3

        consum_dupa_PV= int(Consum.get())-consum_cu_PV
        factura_cu_PV= (consum_dupa_PV-curent_recuperat)*float(Pret.get())

        Economisire= int(Factura.get())-factura_cu_PV

        Amortizare= int(Sistem.get())/(Economisire*12)

    return Timp.set(round(Amortizare,1))


#Creare interfață
window = tkinter.Tk()

window.tk.call('source', 'Azure-ttk-theme-main/azure.tcl')
window.tk.call('set_theme', 'light')

#Titlu interfață
window.title("Caracteristica Curent-Tensiune")

frame = tkinter.Frame(window, background="#5DADE2")
frame.pack()

#Casuta alegere panou
Al_pan_frame = tkinter.LabelFrame(frame, text="Alege panoul", font =("TimesNewRoman", 12, 'bold'))
Al_pan_frame.grid(row = 0, column= 0, padx=20, pady=10, sticky="news")

#Casuta
Model = tkinter.StringVar()
Alegere_combobox = ttk.Combobox(Al_pan_frame, state="readonly", textvariable= Model, 
                                values=["","LG_Electronics_Inc__LG410N2W_A5", "ECO_Future_ECO_290P72", "Green_Energy_Technology_GET_180B"],
                                width=40)
#Alegere_combobox.grid()

#------------------------------

#Variabilele casutelor pentru calcule
Tip = tkinter.StringVar()
Pmax = tkinter.StringVar()
Vmp = tkinter.StringVar()
Imp = tkinter.StringVar()
Voc = tkinter.StringVar()
Isc = tkinter.StringVar()
Celule = tkinter.StringVar()
Lungime = tkinter.StringVar()
Latime = tkinter.StringVar()
Coef_Pmax = tkinter.StringVar()
Coef_Voc = tkinter.StringVar()
Coef_Isc = tkinter.StringVar()
Rp = tkinter.StringVar()
Rs = tkinter.StringVar()
Ipv = tkinter.StringVar()
Idealitate = tkinter.StringVar()
I0 = tkinter.StringVar()
Iradiatia = tkinter.StringVar()
Temperatura = tkinter.StringVar()

Consum = tkinter.StringVar()
Consum.set(200)
Factura = tkinter.StringVar()
Factura.set(160)
Sistem = tkinter.StringVar()
Sistem.set(10000)
Putere = tkinter.StringVar()
Putere.set(300)
Pret = tkinter.StringVar()
Pret.set(0.8)
Timp = tkinter.StringVar()

#------------------------------

#Casuța cu valori principale
Val_prin_frame = tkinter.LabelFrame(frame, text="Valori principale", font =("TimesNewRoman", 12, 'bold'))
Val_prin_frame.grid(row = 1, column= 0, padx=20, pady=10, sticky="news")

#Text valori
Tip_label = tkinter.Label(Val_prin_frame, text = "Tip panou")
Tip_label.grid(row=0, column=0)

Pmax_label = tkinter.Label(Val_prin_frame, text = "Pmax (W)")
Pmax_label.grid(row=1, column=0)

Vmp_label = tkinter.Label(Val_prin_frame, text = "Vmp (V)")
Vmp_label.grid(row=2, column=0)

Imp_label = tkinter.Label(Val_prin_frame, text = "Imp (A)")
Imp_label.grid(row=3, column=0)

Voc_label = tkinter.Label(Val_prin_frame, text = "Voc (V)")
Voc_label.grid(row=4, column=0)

Isc_label = tkinter.Label(Val_prin_frame, text = "Isc (A)")
Isc_label.grid(row=5, column=0)

Celule_label = tkinter.Label(Val_prin_frame, text = "Nr. celule")
Celule_label.grid(row=6, column=0)

Lungime_label = tkinter.Label(Val_prin_frame, text = "Lungime celulă (cm)")
Lungime_label.grid(row=7, column=0)

Latime_label = tkinter.Label(Val_prin_frame, text = "Lățime celulă (cm)")
Latime_label.grid(row=8, column=0)


#Casute text valori
Tip_entry = tkinter.Entry(Val_prin_frame, textvariable= Tip, justify= "center", state="readonly")
Tip_entry.grid(row=0, column=1)

Pmax_entry = tkinter.Entry(Val_prin_frame, textvariable= Pmax, justify= "center", state="readonly")
Pmax_entry.grid(row=1, column=1)

Vmp_entry = tkinter.Entry(Val_prin_frame, textvariable= Vmp, justify= "center", state="readonly")
Vmp_entry.grid(row=2, column=1)

Imp_entry = tkinter.Entry(Val_prin_frame, textvariable= Imp, justify= "center", state="readonly")
Imp_entry.grid(row=3, column=1)

Voc_entry = tkinter.Entry(Val_prin_frame, textvariable= Voc, justify= "center", state="readonly")
Voc_entry.grid(row=4, column=1)

Isc_entry = tkinter.Entry(Val_prin_frame, textvariable= Isc, justify= "center", state="readonly")
Isc_entry.grid(row=5, column=1)

Celule_entry = tkinter.Entry(Val_prin_frame, textvariable= Celule, justify= "center", state="readonly")
Celule_entry.grid(row=6, column=1)

Lungime_entry = tkinter.Entry(Val_prin_frame, textvariable= Lungime, justify= "center", state="readonly")
Lungime_entry.grid(row=7, column=1)

Latime_entry = tkinter.Entry(Val_prin_frame, textvariable= Latime, justify= "center", state="readonly")
Latime_entry.grid(row=8, column=1)

#-----------------------------

#Valori in functie de temperatura
Val_tem_frame = tkinter.LabelFrame(frame, text="Variație în funcție de temperatură", font =("TimesNewRoman", 12, 'bold'))
Val_tem_frame.grid(row = 2, column= 0, padx=20, pady=10, sticky="news")

#Text
Coef_Pmax_label = tkinter.Label(Val_tem_frame, text = "Coeficient Pmax (%/℃)")
Coef_Pmax_label.grid(row=0, column=0)

Coef_Voc_label = tkinter.Label(Val_tem_frame, text = "Coeficient Voc (%/℃)")
Coef_Voc_label.grid(row=1, column=0)

Coef_Isc_label = tkinter.Label(Val_tem_frame, text = "Coeficient Isc (%/℃)")
Coef_Isc_label.grid(row=2, column=0)

#Casute
Coef_Pmax_entry = tkinter.Entry(Val_tem_frame, textvariable= Coef_Pmax, justify= "center", state="readonly")
Coef_Pmax_entry.grid(row=0, column=1)

Coef_Voc_entry = tkinter.Entry(Val_tem_frame, textvariable= Coef_Voc, justify= "center", state="readonly")
Coef_Voc_entry.grid(row=1, column=1)

Coef_Isc_entry = tkinter.Entry(Val_tem_frame, textvariable= Coef_Isc, justify= "center", state="readonly")
Coef_Isc_entry.grid(row=2, column=1)

#Rezultate
Rezultate_frame = tkinter.LabelFrame(frame, text="Parametri panou", font =("TimesNewRoman", 12, 'bold'))
Rezultate_frame.grid(row = 1, column= 1, padx=20, pady=10, sticky="new")

#Text
Rp_label = tkinter.Label(Rezultate_frame, text = "Rp (Ω)")
Rp_label.grid(row=0, column=0)

Rs_label = tkinter.Label(Rezultate_frame, text = "Rs (Ω)")
Rs_label.grid(row=1, column=0)

Ipv_label = tkinter.Label(Rezultate_frame, text = "Ipv (A)")
Ipv_label.grid(row=2, column=0)

Idealitate_label = tkinter.Label(Rezultate_frame, text = "Factor de idealitate")
Idealitate_label.grid(row=3, column=0)

I0_label = tkinter.Label(Rezultate_frame, text = "I0 (A)")
I0_label.grid(row=4, column=0)

#Casute
Rp_entry = tkinter.Entry(Rezultate_frame, textvariable= Rp, justify= "center", state="readonly")
Rp_entry.grid(row=0, column=1)

Rs_entry = tkinter.Entry(Rezultate_frame, textvariable= Rs, justify= "center", state="readonly")
Rs_entry.grid(row=1, column=1)

Ipv_entry = tkinter.Entry(Rezultate_frame, textvariable= Ipv, justify= "center", state="readonly")
Ipv_entry.grid(row=2, column=1)

Idealitate_entry = tkinter.Entry(Rezultate_frame, textvariable= Idealitate, justify= "center", state="readonly")
Idealitate_entry.grid(row=3, column=1)

I0_entry = tkinter.Entry(Rezultate_frame, textvariable= I0, justify= "center", state="readonly")
I0_entry.grid(row=4, column=1)

#Valori variabile
Variabile_frame = tkinter.LabelFrame(frame, text="Factori externi", font =("TimesNewRoman", 12, 'bold'))
Variabile_frame.grid(row = 2, column= 1, padx=20, pady=10, sticky="new")

Iradiatia_label = tkinter.Label(Variabile_frame, text="Iradiația (W/m2)")
Iradiatia_spinbox = tkinter.Spinbox(Variabile_frame, justify= "center", from_= 0, to= 1000, increment= 50, textvariable= Iradiatia)
Iradiatia.set(1000)
Iradiatia_label.grid(row=0, column=0)
Iradiatia_spinbox.grid(row=0, column=1)

Temperatura_label = tkinter.Label(Variabile_frame, text="Temperatură (℃)")
Temperatura_Scale = tkinter.Scale(Variabile_frame, from_= 0, to= 100, orient= "horizontal", length=150, tickinterval=25, variable= Temperatura)
Temperatura.set(25)
Temperatura_label.grid(row=1, column=0)
Temperatura_Scale.grid(row=1, column=1)

#Amortizare
Titlu_Amortizare_label = tkinter.Label(frame, text="Calculare investiție", font =("TimesNewRoman", 20, 'bold') ,background='#5DADE2')
Titlu_Amortizare_label.grid(row=0, column=3)

#Frame amortizare
Amortizare_frame = tkinter.LabelFrame(frame, text="Valori", font =("TimesNewRoman", 12, 'bold'))
Amortizare_frame.grid(row = 1, column= 3, padx=20, pady=10, sticky="new")

#Text
Consum_lunar_label = tkinter.Label(Amortizare_frame, text = "Consum lunar (kWh)")
Consum_lunar_label.grid(row=0, column=0)

Factura_label = tkinter.Label(Amortizare_frame, text = "Factură medie lunar (RON)")
Factura_label.grid(row=1, column=0)

Sistem_label = tkinter.Label(Amortizare_frame, text = "Preț sistem (RON)")
Sistem_label.grid(row=2, column=0)

Putere_sistem_label = tkinter.Label(Amortizare_frame, text = "Putere sistem lunar (kWh)")
Putere_sistem_label.grid(row=3, column=0)

Pret_label = tkinter.Label(Amortizare_frame, text = "Pret/kw (RON)")
Pret_label.grid(row=4, column=0)

Timp_label = tkinter.Label(Amortizare_frame, text = "Timp de amortizare (ani)")
Timp_label.grid(row=5, column=0)

#Text
Consum_lunar_entry = tkinter.Entry(Amortizare_frame, textvariable= Consum, justify= "center")
Consum_lunar_entry.grid(row=0, column=1)

Factura_entry = tkinter.Entry(Amortizare_frame, textvariable= Factura, justify= "center")
Factura_entry.grid(row=1, column=1)

Sistem_entry = tkinter.Entry(Amortizare_frame, textvariable= Sistem, justify= "center")
Sistem_entry.grid(row=2, column=1)

Putere_entry = tkinter.Entry(Amortizare_frame, textvariable= Putere, justify= "center")
Putere_entry.grid(row=3, column=1)

Pret_entry = tkinter.Entry(Amortizare_frame, textvariable= Pret, justify= "center")
Pret_entry.grid(row=4, column=1)

Timp_entry = tkinter.Entry(Amortizare_frame, textvariable= Timp, justify= "center", state="readonly")
Timp_entry.grid(row=5, column=1)

#Button afisează graficul
Button_Calculare = tkinter.Button(frame, text= "Afișează graficul",font =("TimesNewRoman", 10, 'bold'), command= Afiseaza)
Button_Calculare.grid(row=3, column=0, padx=10, pady=10, ipadx=5, ipady=7)

#Button calculeaza elementele
Button_Calculare = tkinter.Button(Amortizare_frame, text= "Calculează", font =("TimesNewRoman", 10, 'bold'), command= calculeazaAmor)
Button_Calculare.grid(row=6, column=1, padx=10, pady=10, ipadx=5, ipady=7, columnspan=1)

#Spatiere intre elemente
for widget in Al_pan_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

for widget in Val_prin_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

for widget in Val_tem_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

for widget in Rezultate_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

for widget in Variabile_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

for widget in Amortizare_frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

#Adougare imagine
Imagine_Sun = Image.open("Sun.png")
Resize_Sun = Imagine_Sun.resize((170,170), Image.ANTIALIAS)
Convert = ImageTk.PhotoImage(Resize_Sun)

Imagine_label = tkinter.Label(frame,image=Convert, width=170, height=170, background='#5DADE2')
Imagine_label.grid(row=2,column=3)


#Grafic
fig, ax = plt.subplots(figsize=(6, 3))

Grafice_frame = tkinter.LabelFrame(frame, text="Grafic", font =("TimesNewRoman", 12, 'bold'))
Grafice_frame.grid(row = 1, column= 2, padx=20, pady=10, sticky="news")

Grafice_frame = FigureCanvasTkAgg(fig, master=Grafice_frame)  
Grafice_frame.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1, ipadx=1, ipady=1)

plt.title('Alege unul dintre panouri')

def Grafic(parametri):
    #Grafic
    fig, ax = plt.subplots(figsize=(6, 3))

    Grafice_frame = tkinter.LabelFrame(frame, text="Grafice", font="TimesNewRoman")
    Grafice_frame.grid(row = 1, column= 2, padx=20, pady=10, sticky="news")

    Grafice_frame = FigureCanvasTkAgg(fig, master=Grafice_frame)  
    Grafice_frame.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1, ipadx=1, ipady=1)

    cases = [
        (1000, 25), #Caz ideal în STC
        (int(Iradiatia.get()),int(Temperatura.get()))
    ]

    conditions = pd.DataFrame(cases, columns=['Geff', 'Tcell'])

    # adjust the reference parameters according to the operating
    # conditions using the De Soto model:
    IL, I0, Rs, Rsh, nNsVth = pvsystem.calcparams_desoto(
        # int(Iradiatia.get()),
        # int(Temperatura.get()),
        conditions['Geff'],
        conditions['Tcell'],
        alpha_sc=parametri['alpha_sc'],
        a_ref=parametri['a_ref'],
        I_L_ref=parametri['I_L_ref'],
        I_o_ref=parametri['I_o_ref'],
        R_sh_ref=parametri['R_sh_ref'],
        R_s=parametri['R_s'],
        EgRef=1.121,
        dEgdT=-0.0002677
    )

    # plug the parameters into the SDE and solve for IV curves:
    curve_info = pvsystem.singlediode(
        photocurrent=IL,
        saturation_current=I0,
        resistance_series=Rs,
        resistance_shunt=Rsh,
        nNsVth=nNsVth,
        ivcurve_pnts=100,
        method='lambertw'
    )

    # plot the calculated curves:
    #plt.figure()
    for i, case in conditions.iterrows():
        label = (
            "$G_{eff}$ " + f"{case['Geff']} $W/m^2$\n"
            "$T_{cell}$ " + f"{case['Tcell']} $\\degree C$"
        )
        plt.plot(curve_info['v'][i], curve_info['i'][i],label=label)
        v_mp = curve_info['v_mp'][i]
        i_mp = curve_info['i_mp'][i]
            # mark the MPP
        plt.plot([v_mp], [i_mp], ls='', marker='o', c='k')
        plt.annotate((float('{0:.3g}'.format(curve_info['v_mp'][i])),float('{0:.3g}'.format(curve_info['i_mp'][i]))),
                     (curve_info['v_mp'][i], curve_info['i_mp'][i]))

    plt.legend(loc='lower left')
    plt.xlabel('Module voltage [V]')
    plt.ylabel('Module current [A]')
    plt.title(parametri['Name'])
    #plt.show()
    plt.gcf().set_tight_layout(True)

    #draw_arrow(ax, 'Irradiance', 20, 2.5, 90, 15, 'r')
    #draw_arrow(ax, 'Temperature', 35, 1, 0, 15, 'l')

    print(pd.DataFrame({
        'i_sc': curve_info['i_sc'],
        'v_oc': curve_info['v_oc'],
        'i_mp': curve_info['i_mp'],
        'v_mp': curve_info['v_mp'],
        'p_mp': curve_info['p_mp'],
    }))

#Afișare interfață
window.mainloop()


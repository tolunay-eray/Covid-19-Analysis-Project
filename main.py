from cProfile import label
from tkinter import PhotoImage
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as mtl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # matplotlib interface for Tkinter
import tkinter
from matplotlib.font_manager import weight_dict

# CSV FILE
file_path = 'TR- Haftalık Rapor Verileri _ TURCOVID19 Açık Veri - Tablo1 (1).csv'
df = pd.read_csv(file_path, header=0)  # header=0, takes the first line as the header
df = df.dropna()  #  Removed lines containing NaN
df = df[["Tarih", "Toplam İyileşen","Toplam Hasta","Toplam Ölüm"]] # filtered coloumn
df.rename(columns={'Toplam Hasta': 'Total Patients','Toplam İyileşen': 'Total Recovered','Toplam Ölüm': 'Total Deaths'}, inplace=True)
df = df.reset_index(drop=True)
print(df) # shows datas

#GUI

window = tkinter.Tk()
window.minsize(width=600,height=600)
window.title("Covid-19 Veri Görselleştirme")
window.config(bg="gray")

#GRAPH

x= df["Tarih"]
def show_graph():
    fig, ax = plt.subplots(figsize=(6, 4)) #Creating a figure and axis for the plot
    ax.plot(x,df["Total Patients"],label ="Total Patients")
    ax.plot(x,df["Total Recovered"],label ="Total Recovered")
    ax.plot(x,df["Total Deaths"],label ="Total Deaths")
    ax.set_title("Covid-19 Data Analysis")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of People")
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#BUTTON
button= tkinter.Button()
button.config(text="Show Graph",command=show_graph)
button.config(height=2,width=20)
button.place(x= 225, y=285)

# IMAGE
img = PhotoImage(file="Covid 19.png")
img = img.subsample(2, 2)  # image scaled
label= tkinter.Label(window,image=img)
label.config(height=200,width=280)
label.pack(pady=10)

img2 = PhotoImage(file="mask.png")
label2=tkinter.Label(window,image=img2)
label.config(height=200,width=280)
label2.pack(pady=180)

window.mainloop()
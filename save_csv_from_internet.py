import io
import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog

    
def save_file_csv(csv_from_internet):
    data = requests.get(csv_from_internet).text
    df = pd.read_csv(io.StringIO(data))
    return df

def a(df):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
	
    def exp_func():
        export_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv(export_path, index=False)

    Butt = tk.Button(text='Push', command=exp_func)
    canvas.create_window(100, 100, window=Butt)

    root.mainloop()



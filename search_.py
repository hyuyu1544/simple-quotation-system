

import tkinter as tk
import pandas as pd
df=pd.read_csv('Quotation.csv',header=0)

def show_entry_fields():
    global df
    if len(e1.get())==0 and len(e2.get())==0 and len(e3.get())==0:
        a=df[df.Company.isin([e0.get()])]
        a.to_excel('result.xlsx')
    elif len(e0.get())==0 and len(e2.get())==0 and len(e3.get())==0:
        a=df[df.Item.isin([e1.get()])]
        a.to_excel('result.xlsx')
    elif len(e0.get()) == 0 and len(e1.get()) == 0 and len(e2.get())==0 and len(e3.get())==0:
        print("No Input!")

    elif len(e2.get())==0 and len(e3.get())==0:
        a=df[df.Item.isin([e1.get()])]
        a=a[a.Company.isin([e0.get()])]
        a.to_excel('result.xlsx')
    elif len(e1.get())==0 and len(e0.get())==0 and len(e3.get())==0:
        #bool = df.Company.contains(e2.get())
        a=df[df.Company.str.contains(e2.get())]
        a.to_excel('result.xlsx')
    elif len(e1.get())==0 and len(e0.get())==0 and len(e2.get())==0:
        #bool = df.Item.contains(e3.get())
        a=df[df.Item.str.contains(e3.get())]
        a.to_excel('result.xlsx')
    elif len(e1.get())==0 and len(e0.get())==0 :
        #bool = df.Item.contains(e3.get())
        #bool = bool.Company.contains(e2.get())
        a=df[df.Item.str.contains(e3.get())]
        a=a[a.Company.str.contains(e2.get())]
        a.to_excel('result.xlsx')


master = tk.Tk()
master.title("Search")
master.resizable(0,0)
tk.Label(master,text="Full Company name here: ").grid(row=0)
e0 = tk.Entry(master,width=20)
e0.grid(row=0, column=1)
tk.Label(master,text="Full Item name here: ").grid(row=1)
e1 = tk.Entry(master,width=20)
e1.grid(row=1, column=1)
tk.Label(master,text="Company keyword here: ").grid(row=2)
e2 = tk.Entry(master,width=20)
e2.grid(row=2, column=1)
tk.Label(master,text="Item keyword here: ").grid(row=3)
e3 = tk.Entry(master,width=20)
e3.grid(row=3, column=1)


tk.Button(master,
          text='Exit',
          command=master.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Search', command=show_entry_fields).grid(row=4,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()

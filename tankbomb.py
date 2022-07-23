# GUI
# with tkinter
#
# 07/05/22
# 23/07/22


"""
some progess

combo box creates different new windows


"""


import tkinter
from tkinter import PhotoImage, ttk

root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
frm.master.maxsize(630, 800)
frm.master.minsize(630, 480)
frm.master.resizable(0, 1)

# inital parts
ttk.Label(frm, text="pyXViewer   ").grid(column=0, row=0, sticky='w', padx=13)
ttk.Label(frm, text="v0.8").grid(column=0, row=1, sticky='w')
# important drop box
picker = ttk.Combobox(frm, textvariable="banger", 
values=('combo', 'dice', 'mango', 'queen')).grid(column=0, row=2, pady=30)

# sub frame
fuji = ttk.Frame(frm, relief='groove', borderwidth=6, padding=20)
fuji.grid(column=0, row= 4)
cola1 = ttk.Label(fuji, text='test').grid(column=0, row=0)
cola2 = ttk.Label(fuji, text='mouse').grid(column=1, row=0)
cola3 = ttk.Radiobutton(fuji, text='chubby').grid(column=2, row=0, padx=40)

# bottom shit
ttk.Button(frm, text='generate').grid(column=1, row=5, pady=33)

# pretty pic
# image

img = PhotoImage(file="pot icon small.png")
pic = ttk.Label(frm, image=img, justify='left')
pic.grid(column=3, row=5, ipady=1, padx=20, ipadx=80, sticky= 'e')


root.mainloop()
# GUI
# with tkinter
#


import tkinter
from tkinter import PhotoImage, ttk

root = tkinter.Tk()
mainApp = ttk.Frame(root, padding=10)
mainApp.grid()
mainApp.master.maxsize(630, 800)
mainApp.master.minsize(630, 480)
mainApp.master.resizable(0, 1)

# inital parts
ttk.Label(mainApp, text="pyXViewer   ").grid(column=0, row=0, sticky='w', padx=15)
ttk.Label(mainApp, text="v0.8").grid(column=0, row=1, sticky='w')
# important drop box
picker = ttk.Combobox(mainApp, textvariable="elements", 
values=('shade', 'zone', 'price', '[ light ]')).grid(column=0, row=2, pady=30)

# sub section
fuji = ttk.Frame(mainApp, relief='groove', borderwidth=6, padding=20)
fuji.grid(column=0, row= 4)
cola1 = ttk.Label(fuji, text='test').grid(column=0, row=0)
cola2 = ttk.Label(fuji, text='tes2').grid(column=1, row=0, padx=9)
cola3 = ttk.Radiobutton(fuji, text='botanical').grid(column=2, row=0, padx=40)

# main button
# generates new window
ttk.Button(mainApp, text='generate').grid(column=1, row=5, pady=33, sticky='s')

# window dressing
# image
img = PhotoImage(file="pot icon small.png")
pic = ttk.Label(mainApp, image=img, justify='left')
pic.grid(column=3, row=5, ipady=1, padx=20, ipadx=80, sticky= 'e')


root.mainloop()
# GUI
# with tkinter
#


import tkinter
from tkinter import PhotoImage, ttk

root = tkinter.Tk()
mainApp = ttk.Frame(root, padding=10)
mainApp.grid()
mainApp.master.maxsize(630, 800)
mainApp.master.minsize(630, 510)
mainApp.master.resizable(0, 1)

# sub section 1
# 
canon = ttk.Frame(mainApp, relief='groove', borderwidth=60, padding=6)
canon.grid(column=0, row= 0)
# inital parts
ttk.Label(canon, text="pyXViewer   ").grid(column=0, row=0, padx=5, sticky='w')
ttk.Label(canon, text="v0.8").grid(column=0, row=1)
# important drop box
picker = ttk.Combobox(canon, textvariable="elements", 
values=('shade', 'zone', 'price', '[ light ]')).grid(column=1, row=2, pady=30)

# sub section 2
#
fuji = ttk.Frame(mainApp, relief='groove', borderwidth=6, padding=20)
fuji.grid(column=0, row=1, sticky='w')
cola1 = ttk.Label(fuji, text='test').grid(column=0, row=0)
cola2 = ttk.Label(fuji, text='test2').grid(column=1, row=0, padx=9)
cola3 = ttk.Radiobutton(fuji, text='botanical').grid(column=2, row=0, padx=40)

# sub section 3
#
epson = ttk.Frame(mainApp, relief='groove', borderwidth=6, padding=20)
epson.grid(column=0, row= 2, sticky='e')
# main button
# generates new window
ttk.Button(epson, text='generate').grid(column=1, row=5, pady=33, sticky='s')

# window dressing
# image
img = PhotoImage(file="pot icon small.png")
pic = ttk.Label(epson, image=img, justify='left')
pic.grid(column=3, row=5, ipady=1, padx=20, ipadx=141, sticky= 'e')


root.mainloop()
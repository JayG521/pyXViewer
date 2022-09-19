# GUI
# with tkinter
#
#

import plantreader
import tkinter
from tkinter import PhotoImage, Toplevel, ttk

root = tkinter.Tk()
mainApp = ttk.Frame(root, padding=10)
mainApp.grid()
mainApp.master.maxsize(680, 800)
mainApp.master.minsize(680, 510)
mainApp.master.resizable(0, 1)


tags_drop = ['[none]', 'shade', 'zone', 'price', 'light']
rush = 'test string'
i_list = range(0, 15, 1)


# expApp frame news to hold dependant 
#
def lazysummer():
   wNew = Toplevel()
   expApp = ttk.Frame(wNew, padding=10)
   expApp.master.minsize(700, 700)
   ttk.Label(wNew, text=rush).grid(column=0, row=1, padx=259, pady=188)
   
   for gg in i_list:
      ttk.Label(wNew, text='test me').grid(column=0, row=1+gg, padx=130)
      ttk.Label(wNew, text=' collume 2222').grid(column=1, row=1+gg, padx=90)


# sub section 1
# 
canon = ttk.Frame(mainApp, relief='groove', borderwidth=60, padding=6)
canon.grid(column=0, row=0, sticky='w')
# inital parts
ttk.Label(canon, text="pyXViewer   ").grid(column=0, row=0, padx=5, sticky='w')
ttk.Label(canon, text="v0.8").grid(column=0, row=1, padx=59)

# sub section 2
#
fuji = ttk.Frame(mainApp, relief='groove', borderwidth=6, padding=20)
fuji.grid(column=0, row=1, sticky='w')
cola1 = ttk.Label(fuji, text='element 1').grid(column=0, row=0, sticky='w')
cola2 = ttk.Label(fuji, text='element 2').grid(column=2, row=0, pady =6)
cola1 = ttk.Label(fuji, text='element 3').grid(column=4, row=0, padx =6)
# important drop box
picker1 = ttk.Combobox(fuji, textvariable="melon", 
   values=tags_drop, state='readonly')
picker1.grid(column=1, row=0, pady=30)
picker2 = ttk.Combobox(fuji, textvariable="chicken", 
   values=tags_drop, state='readonly')
picker2.grid(column=3, row=0, pady=10)
picker3 = ttk.Combobox(fuji, textvariable="egypt", 
   values=tags_drop, state='readonly')
picker3.grid(column=5, row=0, pady=30)

# sub section 3
#
epson = ttk.Frame(mainApp, relief='groove', borderwidth=6, padding=20)
epson.grid(column=0, row= 2, sticky='w')
# main button
# generates new window
ttk.Button(epson, text='generate', command=testgetwidget).grid(column=1, row=5, pady=33, sticky='s')


# window dressing
# image
img = PhotoImage(file="pot icon small.png")
pic = ttk.Label(epson, image=img, justify='left')
pic.grid(column=3, row=5, ipady=1, padx=20, ipadx=141, sticky= 'e')


root.mainloop()
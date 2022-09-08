# GUI
# with tkinter
#

# temporary stuck
# testprinttt function
#
import tkinter
from tkinter import PhotoImage, Toplevel, ttk

root = tkinter.Tk()
mainApp = ttk.Frame(root, padding=10)
mainApp.grid()
mainApp.master.maxsize(680, 800)
mainApp.master.minsize(680, 510)
mainApp.master.resizable(0, 1)


geez = ['[none]', 'shade', 'zone', 'price', 'light']
# user function for later
def testgetwidget():
    if picker1 == '[none]':
        print('empty feild')
        vvv = picker1.get()
        print(vvv)
    else:
        print('option selected')
        vvv = picker1.get()
        print(vvv)

def lazysummer():
   wNew = Toplevel()
   expApp = ttk.Frame(wNew, padding=10)
   expApp.master.minsize(700, 700)
   ttk.Label(wNew, text="text groove maxout").grid(column=0, row=1, padx=259, pady=188)


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
   values=geez)
picker1.grid(column=1, row=0, pady=30)
picker2 = ttk.Combobox(fuji, textvariable="chicken", 
   values=('[none]',' shade', 'zone', 'price', 'light'))
picker2.grid(column=3, row=0, pady=10)
picker3 = ttk.Combobox(fuji, textvariable="egypt", 
   values=('[none]', 'shade', 'zone', 'price', 'light'))
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
# GUI
# with tkinter
#
#
# import tools
import plantreader
import tkinter
from tkinter import PhotoImage, Toplevel, ttk


# multiple inital variables
#
i_list = range(0, 35, 1)

tags_drop = ['[none]', 'zone', 'price', 'light']
rush = 'test top anchor'
granTur = 'test bottom achor'

catEl1 = ['sample']
catEl2 = ['sample']
catEl3 = ['sample']
for catfill in i_list:
    catfill = ['sample']
    catEl1 = catEl1 + catfill
    catEl2 = catEl2 + catfill
    catEl3 = catEl3 + catfill


# gen new window
# expApp frame news to hold dependant variables
#
def lazysummer():
   wNew = Toplevel()
   expApp = ttk.Frame(wNew, padding=10)
   expApp.master.minsize(700, 785)
   ttk.Label(wNew, text=rush).grid(column=0, row=0, padx=9, pady=9)
   ttk.Label(wNew, text=granTur).grid(column=8, row=40, padx=79, pady=1)

   # variable lists
   # needs re work 
   # 
   # choosen for first catagory (element)
   if picker1.get() == '[none]':
      for tyty in i_list:
         catEl1[tyty] = ''
   elif picker1.get() == 'zone':
      for tyty in i_list:
         catEl1[tyty] = plantreader.plantZone[tyty]
   elif picker1.get() == 'price':
      for tyty in i_list:
         catEl1[tyty] = plantreader.plantPrice[tyty]
   elif picker1.get() == 'light':
      for tyty in i_list:
         catEl1[tyty] = plantreader.plantLight[tyty]
   else:
      for tyty in i_list:
         catEl1[tyty] = ''


   for gg in i_list:
      # column 1 (name)
      ttk.Label(wNew, text=plantreader.plantNames[gg]).grid(column=1, row=2+gg, padx=80)
      # column 2 (elemnt 1)
      ttk.Label(wNew, text=catEl1[gg]).grid(column=2, row=2+gg, padx=20)
      # column 3 (elemnt 2)
      ttk.Label(wNew, text=catEl2[gg]).grid(column=3, row=2+gg, padx=20)
      # column 3 (elemnt 3)
      ttk.Label(wNew, text=catEl3[gg]).grid(column=4, row=2+gg, padx=20)


# Main Window App
root = tkinter.Tk()
mainApp = ttk.Frame(root, padding=10)
mainApp.grid()
mainApp.master.maxsize(680, 800)
mainApp.master.minsize(680, 510)
mainApp.master.resizable(0, 1)

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
ttk.Button(epson, text='generate', command=lazysummer).grid(column=1, row=5, pady=33, sticky='s')

# window dressing
# image
img = PhotoImage(file="pot icon small.png")
pic = ttk.Label(epson, image=img, justify='left')
pic.grid(column=3, row=5, ipady=1, padx=20, ipadx=141, sticky= 'e')


root.mainloop()
from tkinter import *

from tkinter import ttk


#------------GUI--------
#main screen
master= Tk()
master.title('SIFRAVIMAS CEZARIO ALGORITMU')


#Label(master,text = "SIFRAVIMAS",font=("Arial",18)).grid(row = 0, column=1,sticky = N)
#field for text:
Label(master,text = "Jusu tekstas",font=("Arial",15)).grid(row = 2, sticky = W,padx=5)
TextEntry=Entry(master)
TextEntry.grid(row=2,column=1)

#choose an operation:
Label(master,text = "Operacija:",font=("Arial",15)).grid(row = 3, sticky = W,padx=5)
O1 = Radiobutton(master, text="Sifravimas",  value=1)
O1.grid( row=3,column=1 )
O2 = Radiobutton(master, text="Atsifravimas",  value=2)
O2.grid( row=4,column=1 )

#shift: 
Label(master,text = "Poslinkis:",font=("Arial",15)).grid(row = 5, sticky = W,padx=5)

optionList = ('0', '1', '2','3', '4', '5','6', '7', '8','9', '10', '11','12', '13', '14','15', '16', '17','18', '19', '20','21','22', '23', '24','25')
v = StringVar()
v.set(optionList[0])
om = OptionMenu(master,v, *optionList)
om.grid(row=5, column=1)

#field for result:
Label(master,text = "Rezultatas",font=("Arial",15)).grid(row = 6, sticky = W,padx=5)
ResultEntry=Entry(master)
ResultEntry.grid(row=6,column=1)

#size of the page
master.geometry('300x300')
master.mainloop()
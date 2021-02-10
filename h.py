from tkinter import *
from tkinter import ttk

upper = {ascii:chr(ascii) for ascii in range(65,91)}
lower = {ascii:chr(ascii) for ascii in range(97,123)}
number = {ascii:chr(ascii) for ascii in range(48,58)}

#----functions
def EnCeasar(s, k):
    for c in s:
        #ord() to convert a character to its numeric representation in Unicode
        o = ord(c)
        # yield insted of return
        if (o not in upper and o not in lower) or o in number:
            yield o
        else:
            # If it's upper case 
            if o in upper and o + k % 26 in upper:
                yield o + k % 26
            # If it's lower case 
            elif o in lower and o + k % 26 in lower:
                yield o + k % 26
            # Otherwise go back 26 (to stay in alphabet)
            else: 
                yield o + k % 26 -26

#function for decryption
def DeCeasar(s, k):
    for c in s:
        o = ord(c)
        if (o not in upper and o not in lower) or o in number:
            yield o
        else:
            if o in upper and o - k +26 % 26 in upper:
                yield o - k +26 % 26
            elif o in lower and o - k+26 % 26 in lower:
                yield o - k +26 % 26
            else: 
                yield o - k +26 % 26 +26

def clean():
    ResultEntry.delete(0, END)

#function for choice:
def validate():
    value = option.get()
    if value == "1":
        #print("sifravimas")
        #choosen shift:
        k=int(ShiftEntry.get())
        if k>26 or k<0:
            print("wrong")
        #text to encrypt
        s=TextEntry.get()
        #then goes to encryption function
        x = (''.join(map(chr, EnCeasar(s, k))))
        print (x)
        ResultEntry.insert(0,x)

    elif value == "2":
        #print("desifravimas")
        k=int(ShiftEntry.get())
        if k>26 or k<0:
            print("wrong")
        s=TextEntry.get()
        #then goes to encryption function
        x = (''.join(map(chr, DeCeasar(s, k))))
        print (x)
        ResultEntry.insert(0,x)

    else:
        print("An option must be selected")


#------------GUI--------
#main screen
master= Tk()
master.title('SIFRAVIMAS CEZARIO ALGORITMU')
option = StringVar()

#field for text:
Label(master,text = "Jusu tekstas",font=("Arial",15)).grid(row = 2, sticky = W,padx=5)
TextEntry=Entry(master)
TextEntry.grid(row=2,column=1)

#choose an operation:
Label(master,text = "Operacija:",font=("Arial",15)).grid(row = 3, sticky = W,padx=5)
O1 = Radiobutton(master, text="Sifravimas",  value=1, var=option)
O1.grid( row=3,column=1 )
O2 = Radiobutton(master, text="Atsifravimas",  value=2, var=option)
O2.grid( row=4,column=1 )

#shift: 
Label(master,text = "Poslinkis (nuo 0 iki 26)",font=("Arial",15)).grid(row = 5, sticky = W,padx=5)
ShiftEntry=Entry(master)
ShiftEntry.grid(row=5,column=1)


#button to get result
button = Button(master, text='GO', width=5,command=validate)
button.grid(row=6,column=1)



#field for result:
Label(master,text = "Rezultatas",font=("Arial",15)).grid(row = 7, sticky = W,padx=5)
ResultEntry=Entry(master)
ResultEntry.grid(row=7,column=1)

#button to clean result
button = Button(master, text='ISVALYTI', width=8,command=clean)
button.grid(row=8,column=1)

#size of the page
master.geometry('400x200')
master.mainloop()
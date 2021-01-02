from tkinter import *
import backend 


def view_comm():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row) #folosim END,row -> indexul 1 va fi pus primul indexul 2 dupa el si tot asa 

def cautare_comm():
    list1.delete(0,END)
    for row in backend.search(title_text.get()): #title_text initial este un StrinVar, dar nu este string, de aceea in convertim cu .get()
        list1.insert(END,row)

def adaugare_comm():
    backend.insert(title_text.get(),autor_text.get(),an_int.get(),editura_text.get())
    list1.delete(0,END)
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def actualizare_comm():
    stringlist = list1.selection_get()
    index = stringlist[0:1]
    backend.update(index,title_text.get(),autor_text.get(),an_int.get(),editura_text.get())
    list1.delete(0,END)
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def stergere_comm():
    #backend.delete(selected_tuple[0]) #deoarece in listobx incep de la 0 si in mysql de la 1 am adaugat +1
    print(list1.selection_get())
    stringlist = list1.selection_get()
    index = stringlist[0:1]
    print("Indexul este: "+index)
    backend.delete(index)
    list1.delete(0,END)
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def exit_comm():
    exit()

window=Tk()

l1=Label(window,text="Titlu")
l1.grid(row=0,column=0)

l2=Label(window,text="Autor")
l2.grid(row=0,column=2)

l3=Label(window,text="An lansare")
l3.grid(row=1,column=0)

l4=Label(window,text="Editura")
l4.grid(row=1,column=2)

title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

autor_text = StringVar()
e2=Entry(window,textvariable=autor_text)
e2.grid(row=0,column=3)

an_int = IntVar()
e3=Entry(window,textvariable=an_int)
e3.grid(row=1,column=1)

editura_text = StringVar()
e4=Entry(window,textvariable=editura_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)  
""" rowspan pe cate randuri sa se intinda si columnspan pe cate coloane """


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="Afisare",width = 12,comm=view_comm)
b1.grid(row=2,column=3)

b2=Button(window,text="Cautare",width = 12,comm=cautare_comm)
b2.grid(row=3,column=3)

b3=Button(window,text="Adaugare",width = 12,comm=adaugare_comm)
b3.grid(row=4,column=3)

b4=Button(window,text="Actualizeaza \n (carte selectata)",width = 12,comm=actualizare_comm)
b4.grid(row=5,column=3)

b5=Button(window,text="Sterge \n (carte selectata)",width = 12,comm=stergere_comm)
b5.grid(row=6,column=3)

b6=Button(window,text="Inchidere",width = 12,comm=exit_comm)
b6.grid(row=7,column=3)

window.mainloop()


"""

Interfaz gráfica Login

"""

import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

user = 'user'

root = tkinter.Tk()
root.title( 'Login' )
root.geometry( '260x125' )
root.resizable( width = False, height = False )

def app():
    userl = Label( text = 'Usuario' )
    userl.grid( row = 0, column = 0, padx = '2.5', pady = '2.5' )
    usere = Entry( root )
    usere.grid( row = '0', column = '1', padx = '2.5', pady = '2.5' )

    passl = Label( text = 'Contraseña' )
    passl.grid( row = '1', column = '0', padx = '2.5', pady = '2.5' )
    passe = Entry( root, show = '*' )
    passe.grid( row = '1', column = '1', padx = '2.5', pady = '2.5' )
    ttk.Checkbutton( root ).grid( row = '1', column = '2', padx = '2.5', pady = '2.5' )

    ttk.Button( text = 'Salir', command = quit ).grid( sticky = 'ew', row = '2', column = '0', padx = '2.5', pady = '2.5' )
    ttk.Button( text = 'Acceder', command = entry ).grid( sticky = 'ew', row = '2', column = '1', padx = '2.5', pady = '2.5' )
    ttk.Button( text = 'Olvide mi contraseña', command = fmpass ).grid( sticky = 'ew', columnspan = '2', padx = '2.5', pady = '2.5' )

    usere.focus()

def entry():
    print( 'Acceder' )
    messagebox.showinfo( 'Acceso' )

def fmpass():
    print( 'Olvide mi contraseña' )
    messagebox.showwarning( 'Olvide mi contraseña' )

def login():
    root.mainloop()
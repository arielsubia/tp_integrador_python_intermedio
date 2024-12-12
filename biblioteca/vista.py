import tkinter as tk
from tkinter import *
from tkinter import ttk


from .prestamo import abrir_vista_prestamo
from .usuario import abrir_vista_usuario
from .libro import abrir_vista_libros

'''
from .licencia import abrir_vista_licencia
'''

#from modelo.consultasbiblio import crear_tabla

def barra_menu(root):
    barra=tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inicio=tk.Menu(barra, tearoff=0)
    menu_acerca=tk.Menu(barra, tearoff=0)
    menu_ayuda=tk.Menu(barra, tearoff=0)
    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Acerca de..', menu = menu_acerca)
    barra.add_cascade(label='Ayuda', menu = menu_ayuda)

        #submenu
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)

    menu_acerca.add_command(label='Acerca de Gestión Bibliotecas')
    menu_ayuda.add_command(label='Ayuda')



class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480,height=320)
        
        self.root=root
        self.pack()

        self.label_principal()
        self.botonera_principal(root)
        self.label_comentario()
                

    def label_principal(self):
        self.label_titulo = tk.Label(self, text="Gestión de Préstamos de Biblioteca")
        self.label_titulo.config(font=('Calibri',20,'bold'))
        self.label_titulo.grid(row= 1, column=0,padx=10,pady=10, columnspan=4)

    def label_comentario(self):
        self.label_titulo = tk.Label(self, text="Gaby: Con este \nbotón se ejecuta la ---> \nfuncionalidad del CRUD")
        self.label_titulo.config(font=('Calibri',8),bg='#d8d8d8')
        self.label_titulo.place(x=4, y=70, width=120,height=35)

    
    def botonera_principal(self,root):
        self.btn_cliente = tk.Button(self, text='Gestión de Préstamos', command=lambda: abrir_vista_prestamo(root))
        self.btn_cliente.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' , bg="gray",cursor='hand2')
        self.btn_cliente.grid(row= 4, column=0,padx=10,pady=10)

        self.btn_vehiculos = tk.Button(self, text='Gestión de Usuarios', command=lambda: abrir_vista_usuario(root))
        self.btn_vehiculos.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' , bg="gray",cursor='hand2')
        self.btn_vehiculos.grid(row= 3, column=0,padx=10,pady=10)

        self.btn_vehiculos = tk.Button(self, text='Libros', command=lambda: abrir_vista_libros(root))
        self.btn_vehiculos.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' , bg="gray",cursor='hand2')
        self.btn_vehiculos.grid(row= 5, column=0,padx=10,pady=10)

        self.img=tk.PhotoImage(file='img/Encabezado.png')
        self.l2=tk.Label(self,image=self.img)
        self.l2.grid(row=6,column=0,padx=10,pady=10)
    



        
    

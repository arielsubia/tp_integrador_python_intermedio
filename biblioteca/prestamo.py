import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .claseg import Frame
#from controlador.cliente_dao import leer_cliente, guardar_cliente, editar_cliente, eliminar_cliente, buscar_cliente

def abrir_vista_prestamo(root):
    vista_prestamo = tk.Toplevel(root)
    vista_prestamo.title('Gestión de Préstamos')
    vista_prestamo.iconbitmap('img/biblioteca.ico')
    vista_prestamo.resizable(None,None)

    app = Frame3(root = vista_prestamo)
    app.config(background='#F7F9AF')


class Frame3(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_cli = None

        self.label_principal()
        self.label_form()
        self.input_form()
        self.tabla_prestamos()
        self.botones_principales()


    def label_principal(self):
        self.label_titulo = tk.Label(self, text="Gestión de Préstamos de Biblioteca")
        self.label_titulo.config(font=('Calibri',15,'bold'))
        self.label_titulo.grid(row= 1, column=0,padx=10,pady=10, columnspan=4)

    def label_form(self):
        self.label_nombre_libro = tk.Label(self, text="Nombre de Libro:")
        self.label_nombre_libro.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_nombre_libro.grid(row= 2, column=0,padx=10,pady=10)

        self.label_autor = tk.Label(self, text="Autor:")
        self.label_autor.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_autor.grid(row= 3, column=0,padx=10,pady=10)

        self.label_editorial = tk.Label(self, text="Editorial:")
        self.label_editorial.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_editorial.grid(row= 4, column=0,padx=10,pady=10)

        self.label_disponible = tk.Label(self, text="Disponible:")
        self.label_disponible.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_disponible.grid(row= 5, column=0,padx=10,pady=10)


    def input_form(self):
        self.nombre_libro_c = tk.StringVar()
        self.entry_nombre_libro = tk.Entry(self,textvariable=self.nombre_libro_c)
        self.entry_nombre_libro.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_nombre_libro.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.autor_c = tk.StringVar()
        self.entry_autor = tk.Entry(self,textvariable=self.autor_c)
        self.entry_autor.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_autor.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')

        self.editorial_c = tk.StringVar()
        self.entry_editorial = tk.Entry(self,textvariable=self.editorial_c)
        self.entry_editorial.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_editorial.grid(row= 4, column=1,padx=10,pady=10, columnspan='2')

        self.disponibilidad_c = tk.StringVar()
        self.entry_disponibilidad = tk.Entry(self,textvariable=self.disponibilidad_c)
        self.entry_disponibilidad.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_disponibilidad.grid(row= 5, column=1,padx=10,pady=10, columnspan='2')

    def tabla_prestamos(self):

        #self.contenido_cli = leer_prestamos('prestamos')
        #self.contenido_cli.reverse()

        self.tabla = ttk.Treeview(self, columns=('LIbro','Fecha Préstamo','Fecha Devolución','Nombre Usuario','Apellido Usuario'))
        self.tabla.grid(row=8,column=0,columnspan=3,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=8, column=2,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0',text='Libro')
        self.tabla.heading('#1',text='Fecha Préstamo')
        self.tabla.heading('#2',text='Fecha Devolución')
        self.tabla.heading('#3',text='Nombre Usuario')
        self.tabla.heading('#4',text='Apellido Usuario')

        self.tabla.column('#0', width=120)
        self.tabla.column('#1', width=120)
        self.tabla.column('#2', width=120)
        self.tabla.column('#3', width=120)
        self.tabla.column('#4', width=120)


'''
    def botones_principales(self):
        self.btn_ver = tk.Button(self, text='Ver Présatmos',command= self.habilitar_campos)
        self.btn_ver.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_ver.grid(row= 5, column=0,padx=10,pady=10, columnspan='2')

        self.btn_modi = tk.Button(self, text='Guardar',command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row= 5, column=2,padx=10,pady=10, columnspan='2')

        self.btn_cance = tk.Button(self, text='Cancelar', command= self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row= 5, column=4,padx=10,pady=10, columnspan='2')
    '''
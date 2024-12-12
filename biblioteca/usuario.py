import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .claseg import Frame
from modelo.usuario_dao import Usuario, guardar_usuario, cargar, editar_usuario, eliminar_usuario, listar_genero, listar_provincia



def abrir_vista_usuario(root):
    vista_usuario = tk.Toplevel(root)
    vista_usuario.title('Gestión de Usuarios')
    vista_usuario.iconbitmap('img/biblioteca.ico')
    vista_usuario.resizable(None,None)

    app = Frame2(root = vista_usuario)
    app.config(background='#d8d8d8')


class Frame2(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_usuario = None

        self.label_principal()
        self.label_form()
        self.input_form()
        self.tabla_usuarios()
        self.botonera_principal()


    def label_principal(self):
        self.label_titulo = tk.Label(self, text="Gestión de Usuarios")
        self.label_titulo.config(font=('Calibri',20,'bold'),bg="#d8d8d8")
        self.label_titulo.grid(row= 1, column=0,padx=10,pady=10, columnspan=4)

    def label_form(self):
        self.label_nombre_usuario = tk.Label(self, text="Nombre del Usuario:")
        self.label_nombre_usuario.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_nombre_usuario.grid(row= 2, column=0,padx=10,pady=10)

        self.label_apellido_usuario = tk.Label(self, text="Apellido del Usuario:")
        self.label_apellido_usuario.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_apellido_usuario.grid(row= 3, column=0,padx=10,pady=10)

        self.label_dni = tk.Label(self, text="DNI:")
        self.label_dni.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_dni.grid(row= 4, column=0,padx=10,pady=10)

        self.label_fecha_nacimiento = tk.Label(self, text="Fecha de Nacimiento:")
        self.label_fecha_nacimiento.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_fecha_nacimiento.grid(row= 5, column=0,padx=10,pady=10)

        self.label_email = tk.Label(self, text="E-mail:")
        self.label_email.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_email.grid(row= 6, column=0,padx=10,pady=10)

        self.label_direccion = tk.Label(self, text="Dirección:")
        self.label_direccion.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_direccion.grid(row= 7, column=0,padx=10,pady=10)

        self.label_provincia = tk.Label(self, text="Provincia:")
        self.label_provincia.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_provincia.grid(row= 8, column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text="Género:")
        self.label_genero.config(font=('Calibri',12,'bold'),fg ='#FFFFFF' , bg="gray",activebackground='#3FD83F',activeforeground='#000000')
        self.label_genero.grid(row= 9, column=0,padx=10,pady=10)

    def input_form(self):
        self.nombre_usuario_c = tk.StringVar()
        self.entry_nombre_usuario = tk.Entry(self,textvariable=self.nombre_usuario_c)
        self.entry_nombre_usuario.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_nombre_usuario.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.apellido_usuario_c = tk.StringVar()
        self.entry_apellido_usuario = tk.Entry(self,textvariable=self.apellido_usuario_c)
        self.entry_apellido_usuario.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_apellido_usuario.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')

        self.dni_c = tk.StringVar()
        self.entry_dni = tk.Entry(self,textvariable=self.dni_c)
        self.entry_dni.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_dni.grid(row= 4, column=1,padx=10,pady=10, columnspan='2')

        self.fecha_nacimiento_c = tk.StringVar()
        self.entry_fecha_nacimiento = tk.Entry(self,textvariable=self.fecha_nacimiento_c)
        self.entry_fecha_nacimiento.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_fecha_nacimiento.grid(row= 5, column=1,padx=10,pady=10, columnspan='2')

        self.email_c = tk.StringVar()
        self.entry_email = tk.Entry(self,textvariable=self.email_c)
        self.entry_email.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_email.grid(row= 6, column=1,padx=10,pady=10, columnspan='2')

        self.direccion_c = tk.StringVar()
        self.entry_direccion = tk.Entry(self,textvariable=self.direccion_c)
        self.entry_direccion.config(width=20, font=('Calibri',12),state='disabled')
        self.entry_direccion.grid(row= 7, column=1,padx=10,pady=10, columnspan='2')

        x = listar_provincia()
        y = []
        for i in x:
            y.append(i[1])

        self.provincia_c = ['Seleccione una Provincia'] + y
        self.entry_provincia = ttk.Combobox(self,state="readonly")
        self.entry_provincia['values'] = self.provincia_c
        self.entry_provincia.current(0)
        self.entry_provincia.config(width=20, font=('Calibri',12))
        self.entry_provincia.bind("<<ComboboxSelected>>")        
        self.entry_provincia.grid(row= 8, column=1,padx=10,pady=10)

        x = listar_genero()
        y = []
        for i in x:
            y.append(i[1])

        self.genero_c = ['Seleccione un Género'] + y
        self.entry_genero = ttk.Combobox(self,state="readonly")
        self.entry_genero['values'] = self.genero_c
        self.entry_genero.current(0)
        self.entry_genero.config(width=20, font=('Calibri',12))
        self.entry_genero.bind("<<ComboboxSelected>>")        
        self.entry_genero.grid(row= 9, column=1,padx=10,pady=10)


    def botonera_principal(self):    

        self.btn_busqueda = tk.Button(self, text='Búsqueda de Usuario',command=self.cargar_datas_tabla)    
        self.btn_busqueda.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='grey',cursor='hand2',activeforeground='#000000')    
        self.btn_busqueda.grid(row= 10, column=0,padx=10,pady=10) 

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_datos)    
        self.btn_editar.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='#84ce95',cursor='hand2',activeforeground='#000000')    
        self.btn_editar.grid(row= 10, column=1,padx=10,pady=10)

        self.btn_alta = tk.Button(self, text='Nuevo Usuario' , command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='#84ce95',cursor='hand2',activeforeground='#000000')    
        self.btn_alta.grid(row= 11, column=0,padx=10,pady=10)    
        
        self.btn_modi = tk.Button(self, text='Guardar',command=self.guardar_datos)    
        self.btn_modi.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='#84ce95',cursor='hand2',activeforeground='#000000')    
        self.btn_modi.grid(row= 11, column=1,padx=10,pady=10)    
        
        self.btn_cance = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)    
        self.btn_cance.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='gray',cursor='hand2',activeforeground='#000000') 
        self.btn_cance.grid(row= 13, column=0,padx=10,pady=10)   

        self.btn_cance = tk.Button(self, text='Eliminar',command=self.eliminar_datos)    
        self.btn_cance.config(width= 20,font=('Calibri', 12,'bold'),fg ='#FFFFFF' ,bg='#f07171',cursor='hand2',activeforeground='#000000') 
        self.btn_cance.grid(row= 13, column=1,padx=10,pady=10) 

    def habilitar_campos(self):    
        self.entry_nombre_usuario.config(state='normal')    
        self.entry_apellido_usuario.config(state='normal')    
        self.entry_dni.config(state='normal')    
        self.entry_fecha_nacimiento.config(state='normal')
        self.entry_email.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_provincia.config(state='normal')
        self.entry_genero.config(state='normal')
        self.id_usuario=None

    def deshabilitar_campos(self):
        self.nombre_usuario_c.set('')
        self.apellido_usuario_c.set('')
        self.dni_c.set('')
        self.email_c.set('')
        self.fecha_nacimiento_c.set('')
        self.direccion_c.set('')

        self.entry_nombre_usuario.config(state='disabled')    
        self.entry_apellido_usuario.config(state='disabled')    
        self.entry_dni.config(state='disabled')    
        self.entry_fecha_nacimiento.config(state='disabled')
        self.entry_email.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_provincia.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.id_usuario=None


    def guardar_datos(self):

        # Paso de string a integer
        self.genero_c_int = 0
        if self.entry_genero.current() == "Masculino":
            self.genero_c_int = 1
        elif self.entry_genero.current() == "Femenino":
            self.genero_c_int = 2
        elif self.entry_genero.current() == "No Binario":
            self.genero_c_int = 3
        else:
            self.genero_c_int = 4
        
        usuario=Usuario(
            self.nombre_usuario_c.get(),
            self.apellido_usuario_c.get(),
            self.dni_c.get(),
            self.fecha_nacimiento_c.get(),
            self.email_c.get(),
            self.direccion_c.get(),
            self.genero_c_int,
        )

        if self.id_usuario == None:
            guardar_usuario(usuario)
        else:
            editar_usuario(usuario, int(self.id_usuario))

        self.cargar_datas_tabla()
        self.deshabilitar_campos()


    def cargar_datas_tabla(self):
        self.lista_usuarios=cargar()
        self.lista_usuarios.reverse()
        for u in self.lista_usuarios:
            self.tabla.insert('',0,text=u[0],values=(u[1],u[2],u[3],u[4],u[5],u[6],u[7]))

    def tabla_usuarios(self):

        self.tabla = ttk.Treeview(self, column=('Nombre de Usuario','Apellido del Usuario','DNI','Fecha de Nacimiento','E-mail','Dirección','Género'))
        self.tabla.grid(row=12,column=0,columnspan=2,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=12, column=2,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0',text='ID Usuario')
        self.tabla.heading('#1',text='Nombre de Usuario')
        self.tabla.heading('#2',text='Apellido de Usuario')
        self.tabla.heading('#3',text='DNI')
        self.tabla.heading('#4',text='Fecha de Nacimiento')
        self.tabla.heading('#5',text='E-mail')
        self.tabla.heading('#6',text='Dirección')
        self.tabla.heading('#7',text='Género')

        self.tabla.column('#0', width=70)
        self.tabla.column('#1', width=120)
        self.tabla.column('#2', width=120)
        self.tabla.column('#3', width=80)
        self.tabla.column('#4', width=100)
        self.tabla.column('#5', width=120)
        self.tabla.column('#6', width=100)
        self.tabla.column('#7', width=60)

    def editar_datos(self):
        self.deshabilitar_campos()
        try:
            self.id_usuario=self.tabla.item(self.tabla.selection())['text']
            self.nombre_usuario=self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_usuario=self.tabla.item(self.tabla.selection())['values'][1]
            self.dni=self.tabla.item(self.tabla.selection())['values'][2]
            self.fecha_nacimiento=self.tabla.item(self.tabla.selection())['values'][3]
            self.email=self.tabla.item(self.tabla.selection())['values'][4]
            self.direccion=self.tabla.item(self.tabla.selection())['values'][5]

            self.habilitar_campos()

            self.entry_nombre_usuario.insert(0, self.nombre_usuario)    
            self.entry_apellido_usuario.insert(0, self.apellido_usuario)    
            self.entry_dni.insert(0, self.dni)    
            self.entry_fecha_nacimiento.insert(0, self.fecha_nacimiento)
            self.entry_email.insert(0, self.email)
            self.entry_direccion.insert(0, self.direccion)

        except:
            titulo='Atención'
            mensaje='No se ha seleccionado ningún registro.'
            messagebox.showwarning(titulo,mensaje)

    def eliminar_datos(self):
        try:
            self.id_usuario=self.tabla.item(self.tabla.selection())['text']
            eliminar_usuario(int(self.id_usuario))
            self.cargar_datas_tabla()
            self.id_usuario=None
        except:
            titulo='Atención'
            mensaje='No se ha seleccionado ningún registro.'
            messagebox.showwarning(titulo,mensaje)

    def salir(self):
        self.destroy()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .claseg import Frame
#from controlador.cliente_dao import leer_cliente, guardar_cliente, editar_cliente, eliminar_cliente, buscar_cliente

def abrir_vista_libros(root):
    vista_prestamo = tk.Toplevel(root)
    vista_prestamo.title('Gestión de Libros')
    vista_prestamo.iconbitmap('img/biblioteca.ico')
    vista_prestamo.resizable(0,0)

    app = Frame3(root = vista_prestamo)
    app.config(background='gray')


class Frame3(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_cli = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.tabla_cliente()
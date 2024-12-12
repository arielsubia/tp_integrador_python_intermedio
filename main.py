import tkinter as tk
from biblioteca.vista import Frame, barra_menu

def main():
    ventana = tk.Tk()
    ventana.title('Gestión de Bibliotecas')
    ventana.iconbitmap('img/biblioteca.ico')
    ventana.geometry('450x380')
    ventana.resizable(None,None)

    barra_menu(ventana)
    app = Frame(root=ventana)
    
    
    ventana.mainloop()

if __name__ == '__main__':
    main()
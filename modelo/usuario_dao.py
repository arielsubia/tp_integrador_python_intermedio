import sqlite3
from .conexion_db import Conexion
from tkinter import messagebox

class Usuario:
    def __init__(self, nombre_usuario, apellido_usuario, dni, fecha_nacimiento, email, direccion, genero):
        self.id_usuario=None
        self.nombre_usuario=nombre_usuario
        self.apellido_usuario=apellido_usuario
        self.dni=dni
        self.fecha_nacimiento=fecha_nacimiento
        self.email=email
        self.direccion=direccion
        self.genero=genero
    
    def __str__(self):
        return f'Usuario[{self.nombre_usuario},{self.apellido_usuario},{self.dni},{self.fecha_nacimiento},{self.email},{self.direccion}, {self.genero}]'
    
def guardar_usuario(usuario):
    conexion=Conexion()
    sql = f'''
    INSERT INTO usuario (nombre,apellido,dni,fechaNacimiento,email,direccion,idGenero)
    VALUES("{usuario.nombre_usuario}","{usuario.apellido_usuario}","{usuario.dni}","{usuario.fecha_nacimiento}","{usuario.email}","{usuario.direccion}","{usuario.genero}")
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_con()
    except:
        titulo='Atención'
        mensaje='Verifique que los datos estén completos y que no se repitan usuarios.'
        messagebox.showwarning(titulo,mensaje) 

def cargar():
    conexion=Conexion()
    lista_usuarios= []

    sql = '''SELECT * FROM usuario as u
        INNER JOIN genero as g
        ON u.idGenero=g.idGenero
        '''
    try:
        conexion.cursor.execute(sql)
        lista_usuarios=conexion.cursor.fetchall()
        conexion.cerrar_con()
        return lista_usuarios
    except:
        titulo='Atención'
        mensaje='Verifique la conexión a la base de datos.'
        messagebox.showwarning(titulo,mensaje) 

def listar_genero():
    conexion=Conexion()
    lista_genero= []

    sql = 'SELECT * FROM genero'

    try:
        conexion.cursor.execute(sql)
        lista_genero=conexion.cursor.fetchall()
        conexion.cerrar_con()
        return lista_genero
    except:
        titulo='Atención'
        mensaje='Verifique la conexión a la base de datos.'
        messagebox.showwarning(titulo,mensaje)

def listar_provincia():
    conexion=Conexion()
    lista_provincia= []

    sql = 'SELECT * FROM provincias'

    try:
        conexion.cursor.execute(sql)
        lista_provincia=conexion.cursor.fetchall()
        conexion.cerrar_con()
        return lista_provincia
    except:
        titulo='Atención'
        mensaje='Verifique la conexión a la base de datos.'
        messagebox.showwarning(titulo,mensaje)


def editar_usuario(usuario, id_usuario):
    conexion=Conexion()
    
    sql = f'''
    UPDATE usuario SET nombre = '{usuario.nombre_usuario}', apellido = '{usuario.apellido_usuario}', dni='{usuario.dni}',
    fechaNacimiento='{usuario.fecha_nacimiento}',email='{usuario.email}',direccion='{usuario.direccion}',idGenero={usuario.genero}
    WHERE idUsuario = {id_usuario}
    '''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_con()
    except:
        titulo='Atención'
        mensaje='No se pudo editar el registro solicitado.'
        messagebox.showwarning(titulo,mensaje) 


def eliminar_usuario(id_usuario):
    conexion=Conexion()
    sql = f'DELETE FROM usuario WHERE idUsuario = {id_usuario}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_con()
    except:
        titulo='Atención'
        mensaje='No se pudo eliminar el registro solicitado.'
        messagebox.showwarning(titulo,mensaje) 
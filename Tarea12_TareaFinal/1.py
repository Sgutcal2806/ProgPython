import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Alumnos")
        
        # Etiquetas y campos de entrada
        tk.Label(self.ventana, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(self.ventana)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.ventana)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.ventana, text="Apellidos:").grid(row=2, column=0, padx=5, pady=5)
        self.apellidos_entry = tk.Entry(self.ventana)
        self.apellidos_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.ventana, text="Nota:").grid(row=3, column=0, padx=5, pady=5)
        self.nota_entry = tk.Entry(self.ventana)
        self.nota_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botones
        self.btn_alta = tk.Button(self.ventana, text="Alta de Alumno", command=self.alta_alumno)
        self.btn_alta.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.btn_aprobados = tk.Button(self.ventana, text="Consultar Aprobados", command=self.consultar_aprobados)
        self.btn_aprobados.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.btn_suspendidos = tk.Button(self.ventana, text="Consultar Suspendidos", command=self.consultar_suspendidos)
        self.btn_suspendidos.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.btn_informe = tk.Button(self.ventana, text="Generar Informe", command=self.generar_informe)
        self.btn_informe.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.btn_salir = tk.Button(self.ventana, text="Salir", command=self.salir)
        self.btn_salir.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.ventana.mainloop()

    def alta_alumno(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        nota = self.nota_entry.get()

        if codigo and nombre and apellidos and nota:
            with open("alumnos.txt", "a") as archivo:
                archivo.write(f"{codigo},{nombre},{apellidos},{nota}\n")
            mb.showinfo("Alta de Alumno", "Alumno añadido correctamente.")
        else:
            mb.showerror("Error", "Por favor, rellene todos los campos.")

    def consultar_aprobados(self):
        self.consultar_alumnos("Aprobados")

    def consultar_suspendidos(self):
        self.consultar_alumnos("Suspendidos")

    def consultar_alumnos(self, estado):
        with open("alumnos.txt", "r") as archivo:
            alumnos = archivo.readlines()

        alumnos_estado = [alumno.strip().split(",") for alumno in alumnos if self.evaluar_estado(alumno, estado)]

        if alumnos_estado:
            mensaje = "\n".join([f"Código: {alumno[0]}, Nombre: {alumno[1]}, Apellidos: {alumno[2]}, Nota: {alumno[3]}" for alumno in alumnos_estado])
            mb.showinfo(f"Alumnos {estado}", mensaje)
        else:
            mb.showinfo(f"Alumnos {estado}", f"No hay alumnos {estado}.")

    def evaluar_estado(self, alumno, estado):
        nota = int(alumno.strip().split(",")[-1])
        if estado == "Aprobados":
            return nota >= 5
        elif estado == "Suspendidos":
            return nota < 5

    def generar_informe(self):
        nombre_archivo = fd.asksaveasfilename(defaultextension=".txt", filetypes=(("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))
        if nombre_archivo:
            with open("alumnos.txt", "r") as archivo:
                contenido = archivo.read()
            with open(nombre_archivo, "w") as nuevo_archivo:
                nuevo_archivo.write(contenido)
            mb.showinfo("Informe Generado", f"Informe generado correctamente como '{nombre_archivo}'.")

    def salir(self):
        self.ventana.destroy()

aplicacion = Aplicacion()

from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from sty import configurar_estilos, MARGEN_GENERAL, MARGEN_INTERNO
from logica import iniciar_descarga_audio

def construir_interfaz(ventana_principal):
    estilo = ttk.Style()
    color_fondo = configurar_estilos(estilo)
    ventana_principal.configure(background=color_fondo)
    
    ventana_principal.title("Descargador de Audio YouTube")
    ventana_principal.geometry("580x680")
    ventana_principal.resizable(False, True)

    #para ir guardardo labelss y entradas, y tenerlas ordenadoas
    componentes = {}

    #Marco Principal
    marco_principal = ttk.Frame(ventana_principal, padding=MARGEN_GENERAL)
    marco_principal.pack(fill=BOTH, expand=True)

    etiqueta_titulo = ttk.Label(marco_principal, text="Descargador de Audio", style="Titulo.TLabel", anchor="center")
    etiqueta_titulo.pack(fill=X, pady=(0, MARGEN_INTERNO))

    
    marco_url = ttk.Labelframe(marco_principal, text=" Enlace del Video ", padding=MARGEN_INTERNO)
    marco_url.pack(fill=X, pady=(0, MARGEN_INTERNO))

    componentes["entrada_url"] = ttk.Entry(marco_url, font=("Segoe UI", 11))
    componentes["entrada_url"].pack(fill=X, padx=5, pady=5)
    componentes["entrada_url"].focus() #para darle solo ctrl v de un solo y no tener que darle click a mi entrada de url

    #btn de Descarga
    componentes["boton_descargar"] = ttk.Button(
        marco_principal,
        text="Descargar Audio MP3",
        command=lambda: manejar_clic_descarga(ventana_principal, componentes)
    )
    componentes["boton_descargar"].pack(fill=X, pady=MARGEN_INTERNO)

    #Marco Estado
    marco_estado = ttk.Labelframe(marco_principal, text=" Estado del Proceso ", padding=MARGEN_INTERNO)
    marco_estado.pack(fill=BOTH, expand=True, pady=(5, 0))

    componentes["etiqueta_titulo_video"] = ttk.Label(marco_estado, text="Título: -", style="Subtitulo.TLabel", wraplength=500)
    componentes["etiqueta_titulo_video"].pack(anchor=W, pady=(0, 8))

    componentes["etiqueta_estado"] = ttk.Label(marco_estado, text="Estado: Esperando enlace...", style="Subtitulo.TLabel")
    componentes["etiqueta_estado"].pack(anchor=W, pady=(0, 10))

    componentes["barra_progreso"] = ttk.Progressbar(marco_estado, mode="indeterminate", bootstyle="pink")
    componentes["barra_progreso"].pack(fill=X)

def manejar_clic_descarga(ventana_principal, componentes):
    url = componentes["entrada_url"].get().strip()

    #COMRPOBAR QUE TE ESTE LLENO LA ENTRADA
    if not url:
        messagebox.showwarning("Campo Vacío", "Por favor, ingresa una URL de YouTube.")
        return

    #DESACTIVAR MIENTRAS CARGA
    componentes["boton_descargar"].config(state="disabled")
    componentes["entrada_url"].config(state="disabled")
    componentes["etiqueta_estado"].config(text="Estado: Conectando...")
    componentes["etiqueta_titulo_video"].config(text="Título: Cargando información...")
    componentes["barra_progreso"].start(10)

    #CAMBIAR LAS ETIQUETAS CIANDO INICIA
    def al_iniciar(titulo):
        ventana_principal.after(0, lambda: [
            componentes["etiqueta_titulo_video"].config(text=f"Título: {titulo}"),
            componentes["etiqueta_estado"].config(text="Estado: Descargando...")
        ])

    def al_exito(ruta_archivo):
        ventana_principal.after(0, lambda: [
            componentes["barra_progreso"].stop(),
            componentes["boton_descargar"].config(state="normal"),
            componentes["entrada_url"].config(state="normal"),
            componentes["etiqueta_estado"].config(text="Estado: ¡Descarga completada!"),
            messagebox.showinfo("Éxito", f"Audio descargado correctamente.\n\nGuardado en:\n{ruta_archivo}")
        ])

    def al_error(mensaje):
        ventana_principal.after(0, lambda: [
            componentes["barra_progreso"].stop(),
            componentes["boton_descargar"].config(state="normal"),
            componentes["entrada_url"].config(state="normal"),
            componentes["etiqueta_estado"].config(text="Estado: Error en la descarga"),
            messagebox.showerror("Error", mensaje)
        ])

    manejadores = {
        "al_iniciar": al_iniciar,
        "al_exito": al_exito,
        "al_error": al_error
    }

    iniciar_descarga_audio(url, manejadores)
import os
import threading
from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError

def iniciar_descarga_audio(url_video, manejadores):

    def proceso_hilo():
        try:
            video = YouTube(url_video)
            titulo_video = video.title
            
            #para usar la def de al_iniciar y mandamos el parametro
            manejadores["al_iniciar"](titulo_video)

            #solo el audio
            flujo_audio = video.streams.get_audio_only()
            
            #para la carpeta (nos hace falta probar con "Descargas")
            carpeta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            if not os.path.exists(carpeta_descargas):
                carpeta_descargas = os.getcwd()

            #Descargar archivo
            archivo_descargado = flujo_audio.download(output_path=carpeta_descargas)
            
            #Cambiar extensión a .mp3
            ruta_base, _ = os.path.splitext(archivo_descargado)
            archivo_mp3 = ruta_base + ".mp3"
            if os.path.exists(archivo_mp3):
                os.remove(archivo_mp3)
            os.rename(archivo_descargado, archivo_mp3)

            #usamos la def de al_exito y damos el parametrooo que seria la ruta tmb
            manejadores["al_exito"](archivo_mp3)

        except PytubeFixError as error:
            manejadores["al_error"](f"Error de YouTube: {str(error)}")
        except Exception as error:
            manejadores["al_error"](f"Error inesperado: {str(error)}")

    #para que no quede congelado
    threading.Thread(target=proceso_hilo, daemon=True).start()
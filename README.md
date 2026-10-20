# PM-IIIP-2026-APP-DOWNLOAD-AUDIO-YT

Desarrollar una aplicación de escritorio en Python que permita descargar el audio de videos de YouTube. La interfaz gráfica debe hacerse con la librería ttkbootstrap y la descarga con pytubefix.

Requisitos de la aplicación

La aplicación debe:

Tener un campo para ingresar la URL del video de YouTube.
Validar que la URL no esté vacía antes de descargar. Si está vacía, debe mostrar un mensaje de advertencia y no iniciar la descarga.
Descargar únicamente el audio del video.
Mostrar en la interfaz el título del audio que se está descargando.
Mostrar un mensaje de "Descargando..." mientras la descarga está en proceso. La ventana no debe quedarse congelada durante la descarga.
Mostrar un mensaje de aviso cuando la descarga termine correctamente.

Ejecutables

Generar el ejecutable de la aplicación para:

Windows (.exe)
Linux

Uso responsable de la IA

Pueden usar herramientas de inteligencia artificial como apoyo, con estas condiciones:

Deben entender y poder explicar todo el código que entreguen.
Deben incluir una breve bitácora que diga qué herramienta usaron, para qué la usaron y qué partes modificaron o aprendieron por su cuenta.
El docente podrá pedir que expliquen o modifiquen cualquier parte del código.

Entregables

Código fuente (.py)
Ejecutables de Windows y Linux
Bitácora de uso de IA (PDF o documento)
Rúbrica de evaluación

Criterio	Puntos
Interfaz funcional y ordenada con ttkbootstrap	4
Validación de URL vacía con mensaje de advertencia	3
Descarga correcta del audio	6
Muestra el título del audio en descarga	3
Mensaje de "Descargando..." sin congelar la ventana	4
Aviso de descarga completada	2
Ejecutable de Windows funcional	3
Ejecutable de Linux funcional	3
Bitácora de uso responsable de la IA	2
Total	30
Nota: El problema con pytubefix no es que Python haya dejado de funcionar, sino que YouTube ha cambiado la forma en que entrega los videos. Antes era común encontrar un stream progresivo(forma de entregar un video donde el video y el audio vienen juntos en el mismo archivo/stream) que contenía video y audio juntos, por lo que pytubefix podía descargar un solo archivo directamente. Ahora muchos videos, especialmente en resoluciones altas, se entregan mediante streams adaptativos, donde el video y el audio vienen separados. Por eso pytubefix puede encontrar el video, pero no necesariamente un archivo que contenga ambas pistas. 

Para obtener el archivo final hay que descargar ambas pistas y combinarlas, normalmente usando FFmpeg.

Si se puede unir luego de la descarga pero habria que instalar el programa FFmpeg para que haga ese proceso o estar usando vlc que podria reproducirlos, el problema de esto es cuando se genere el ejecutable ya que el FFmpeg es aparte no de python.

Permitido entrega en parejas.
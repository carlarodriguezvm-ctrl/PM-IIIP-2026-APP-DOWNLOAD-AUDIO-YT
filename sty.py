import ttkbootstrap as ttk

MARGEN_GENERAL = 20
MARGEN_INTERNO = 10

def configurar_estilos(estilo: ttk.Style):

    estilo.theme_use("journal")
    
    # Paleta de colores rosaditos
    color_fondo = "#FFF0F5"         # Fondo rosa pastel suave
    rosa_principal = "#FF69B4"     # Rosa principal
    rosa_oscuro = "#C71585"        # Fucsia/Rosa oscuro para textos y acentos
    texto_oscuro = "#4A0E2E"       # Texto principal oscuro

    estilo.configure(".", background=color_fondo, font=("Segoe UI", 10))

    # Estilo de Botones
    estilo.configure(
        "TButton",
        font=("Segoe UI", 11, "bold"),
        background=rosa_principal,
        foreground="white",
        padding=10
    )
    estilo.map(
        "TButton",
        background=[("active", rosa_oscuro)]
    )

    # Estilo de Marcos (Labelframes)
    estilo.configure(
        "TLabelframe",
        background=color_fondo,
        bordercolor="#CC717F",
        borderwidth=5
    )
    estilo.configure(
        "TLabelframe.Label",
        font=("Segoe UI", 11, "bold"),
        foreground=rosa_oscuro,
        background=color_fondo
    )
    
    # Estilos de Etiquetas
    estilo.configure(
        "Titulo.TLabel",
        font=("Segoe UI", 16, "bold"),
        foreground=rosa_oscuro,
        background=color_fondo
    )

    estilo.configure(
        "Subtitulo.TLabel",
        font=("Segoe UI", 10, "bold"),
        foreground=texto_oscuro,
        background=color_fondo
    )
    
    return color_fondo
import customtkinter as ctk
import tkinter as tk  # Importamos tkinter para usar IntVar

# Configuración de la ventana principal
app = ctk.CTk()
app.geometry("1024x768") # Resolución de NOAX de empaque
app.title("Encajonado Doble - Desktop")

# Configuración del modo claro
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Variables para los checkboxes del Puesto 1
ctrl_homog_var_1 = tk.IntVar(value=1)  # Checkbox Ctrl Homog del Puesto 1 arranca marcado
validar_peso_var_1 = tk.IntVar(value=1)  # Checkbox Validar Peso del Puesto 1 arranca marcado

# Variables para los checkboxes del Puesto 2
ctrl_homog_var_2 = tk.IntVar(value=1)  # Checkbox Ctrl Homog del Puesto 2 arranca marcado
validar_peso_var_2 = tk.IntVar(value=1)  # Checkbox Validar Peso del Puesto 2 arranca marcado

# Configuración de las columnas de la ventana principal para centrar los frames
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Variables para controlar las cajas seleccionadas
caja_seleccionada_1 = tk.IntVar(value=0)  # Ninguna caja seleccionada en el contenedor 1
caja_seleccionada_2 = tk.IntVar(value=0)  # Ninguna caja seleccionada en el contenedor 2

# Función para manejar la selección de cajas en el contenedor 1
def seleccionar_caja(contenedor, numero):
    if contenedor == 1:
        caja_seleccionada_1.set(numero)
    else:
        caja_seleccionada_2.set(numero)

    # Actualizamos el aspecto de las cajas después de cada selección
    actualizar_cajas(contenedor)

# Función para actualizar el color y tamaño de las cajas seleccionadas
def actualizar_cajas(contenedor):
    if contenedor == 1:
        for i in range(1, 4):
            if caja_seleccionada_1.get() == i:
                botones_cajas_1[i-1].configure(fg_color="#4a90e2", width=130, height=55)  # Caja seleccionada
            else:
                botones_cajas_1[i-1].configure(fg_color="#727272", width=120, height=50)  # Cajas no seleccionadas
    else:
        for i in range(4, 7):
            if caja_seleccionada_2.get() == i:
                botones_cajas_2[i-4].configure(fg_color="#4a90e2", width=130, height=55)  # Caja seleccionada
            else:
                botones_cajas_2[i-4].configure(fg_color="#727272", width=120, height=50)  # Cajas no seleccionadas

# Variable para controlar los radio buttons de ingreso/egreso en cada contenedor
modo_1 = tk.IntVar(value=1)  # Contenedor 1: 1 = Ingreso, 2 = Egreso
modo_2 = tk.IntVar(value=1)  # Contenedor 2: 1 = Ingreso, 2 = Egreso

# Creación de los marcos principales para Puesto 1 y Puesto 2
frame_1 = ctk.CTkFrame(app, width=450, height=500, corner_radius=15)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
frame_1.grid_columnconfigure(0, weight=1)

frame_2 = ctk.CTkFrame(app, width=450, height=500, corner_radius=15)
frame_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
frame_2.grid_columnconfigure(0, weight=1)

# Función de radio buttons para Puesto 1
def cambio_modo():
    print(f"Modo cambiado en contenedor 1: {modo_1.get()}")
    print(f"Modo cambiado en contenedor 2: {modo_2.get()}")

# Título para Puesto 1, centrado
puesto_label_1 = ctk.CTkLabel(frame_1, text="Puesto 1", font=("Arial", 16, "bold"))
puesto_label_1.grid(row=0, column=0, padx=10, pady=10)

# Radio buttons para Ingreso / Egreso en Puesto 1, vinculados a la variable modo_1
ingreso_1 = ctk.CTkRadioButton(frame_1, text="Ingreso", variable=modo_1, value=1, command=cambio_modo, fg_color="green")
ingreso_1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

egreso_1 = ctk.CTkRadioButton(frame_1, text="Egreso", variable=modo_1, value=2, command=cambio_modo, fg_color="red")
egreso_1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Centramos las cajas y las alineamos, configurando columnas en el frame
caja_frame = ctk.CTkFrame(frame_1)
caja_frame.grid(row=2, column=0, padx=10, pady=10)
caja_frame.grid_columnconfigure((0, 1, 2), weight=1)  # Distribución igual de columnas

# Almacenamos los botones de las cajas en una lista para hacer fácil la actualización
botones_cajas_1 = []
for i in range(1, 4):
    caja = ctk.CTkButton(caja_frame, text=f"Caja {i}", width=120, height=50, corner_radius=10,
                         fg_color="#727272", hover_color="#4a90e2", command=lambda num=i: seleccionar_caja(1, num))
    caja.grid(row=0, column=i-1, padx=10, pady=5)
    botones_cajas_1.append(caja)

    cantidad_label = ctk.CTkLabel(caja_frame, text=f"Cant: {i-1}", font=("Arial", 12))  # Etiqueta de cantidad debajo de cada botón
    cantidad_label.grid(row=1, column=i-1, padx=10, pady=5)

# Campo de texto para el código de barras, centrado
codbar_1 = ctk.CTkEntry(frame_1, placeholder_text="Codbar", width=300, height=30)
codbar_1.grid(row=3, column=0, padx=10, pady=10)

# Etiqueta para la sección DATA, centrada
data_label_1 = ctk.CTkLabel(frame_1, text="DATA", font=("Arial", 14, "bold"), fg_color="black", text_color="white", width=300)
data_label_1.grid(row=4, column=0, padx=10, pady=10)

# Información del producto, centrada
desc_label_1 = ctk.CTkLabel(frame_1, text="Descripción de Producto", font=("Arial", 12))
desc_label_1.grid(row=5, column=0, padx=10, pady=5)

insumo_label_1 = ctk.CTkLabel(frame_1, text="Insumo Articulo", font=("Arial", 12))
insumo_label_1.grid(row=6, column=0, padx=10, pady=5)

# Añadimos las etiquetas de pesos mínimos y máximos debajo de "Insumo Articulo"
pesos_min_max_1 = ctk.CTkLabel(frame_1, text="Mínimo: X kg - Máximo: X kg", font=("Arial", 12))
pesos_min_max_1.grid(row=7, column=0, padx=10, pady=5)

# Peso y Piezas en Puesto 1, reubicados a la izquierda y derecha
peso_piezas_frame_1 = ctk.CTkFrame(frame_1)
peso_piezas_frame_1.grid(row=8, column=0, padx=10, pady=5, sticky="ew")
peso_piezas_frame_1.grid_columnconfigure((0, 1), weight=1)

# Ajustamos el margen de los pesos para que queden más centrados
peso_label_1 = ctk.CTkLabel(peso_piezas_frame_1, text="Peso Actual: 0 Kg", font=("Arial", 12, "bold"))
peso_label_1.grid(row=0, column=0, padx=(100, 10), pady=5, sticky="w")

piezas_label_1 = ctk.CTkLabel(peso_piezas_frame_1, text="Piezas: 0", font=("Arial", 12, "bold"))
piezas_label_1.grid(row=0, column=1, padx=(10, 100), pady=5, sticky="e")

# Botones de control en Puesto 1
ctrl_homog_1 = ctk.CTkCheckBox(frame_1, text="Ctrl Homog", font=("Arial", 12), variable=ctrl_homog_var_1)
ctrl_homog_1.grid(row=9, column=0, padx=(120, 10), pady=10, sticky="w")

validar_peso_1 = ctk.CTkCheckBox(frame_1, text="Validar Peso", font=("Arial", 12), variable=validar_peso_var_1)
validar_peso_1.grid(row=9, column=0, padx=(10, 120), pady=10, sticky="e")

# Añadimos el botón de EDIT CTRL y el botón de cruz roja
edit_ctrl_frame_1 = ctk.CTkFrame(frame_1)
edit_ctrl_frame_1.grid(row=10, column=0, padx=10, pady=10, sticky="ew")
edit_ctrl_frame_1.grid_columnconfigure((0, 1), weight=1)

edit_ctrl_button_1 = ctk.CTkButton(edit_ctrl_frame_1, text="EDIT CTRL", width=120, height=30, corner_radius=10, fg_color="#4a90e2", hover_color="#3e7db4")
edit_ctrl_button_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Añadimos el botón con la cruz roja
cerrar_button_1 = ctk.CTkButton(edit_ctrl_frame_1, text="✖", width=80, height=30, corner_radius=10, fg_color="#ff4d4d")
cerrar_button_1.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Repetimos lo mismo para Puesto 2
puesto_label_2 = ctk.CTkLabel(frame_2, text="Puesto 2", font=("Arial", 16, "bold"))
puesto_label_2.grid(row=0, column=0, padx=10, pady=10)

ingreso_2 = ctk.CTkRadioButton(frame_2, text="Ingreso", variable=modo_2, value=1, command=cambio_modo, fg_color="green")
ingreso_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

egreso_2 = ctk.CTkRadioButton(frame_2, text="Egreso", variable=modo_2, value=2, command=cambio_modo, fg_color="red")
egreso_2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

caja_frame_2 = ctk.CTkFrame(frame_2)
caja_frame_2.grid(row=2, column=0, padx=10, pady=10)
caja_frame_2.grid_columnconfigure((0, 1, 2), weight=1)

# Almacenamos los botones de las cajas del contenedor 2
botones_cajas_2 = []
for i in range(4, 7):
    caja = ctk.CTkButton(caja_frame_2, text=f"Caja {i}", width=120, height=50, corner_radius=10,
                         fg_color="#727272", hover_color="#4a90e2", command=lambda num=i: seleccionar_caja(2, num))
    caja.grid(row=0, column=i-4, padx=10, pady=5)
    botones_cajas_2.append(caja)

    cantidad_label = ctk.CTkLabel(caja_frame_2, text=f"Cant: {i-4}", font=("Arial", 12))  # Etiqueta de cantidad debajo de cada botón
    cantidad_label.grid(row=1, column=i-4, padx=10, pady=5)

# Campo de texto para el código de barras
codbar_2 = ctk.CTkEntry(frame_2, placeholder_text="Codbar", width=300, height=30)
codbar_2.grid(row=3, column=0, padx=10, pady=10)

# Etiqueta para la sección DATA
data_label_2 = ctk.CTkLabel(frame_2, text="DATA", font=("Arial", 14, "bold"), fg_color="black", text_color="white", width=300)
data_label_2.grid(row=4, column=0, padx=10, pady=10)

desc_label_2 = ctk.CTkLabel(frame_2, text="Descripción de Producto", font=("Arial", 12))
desc_label_2.grid(row=5, column=0, padx=10, pady=5)

insumo_label_2 = ctk.CTkLabel(frame_2, text="Insumo Articulo", font=("Arial", 12))
insumo_label_2.grid(row=6, column=0, padx=10, pady=5)

# Añadimos las etiquetas de pesos mínimos y máximos debajo de "Insumo Articulo"
pesos_min_max_2 = ctk.CTkLabel(frame_2, text="Mínimo: X kg - Máximo: X kg", font=("Arial", 12))
pesos_min_max_2.grid(row=7, column=0, padx=10, pady=5)

# Peso y Piezas en Puesto 2
peso_piezas_frame_2 = ctk.CTkFrame(frame_2)
peso_piezas_frame_2.grid(row=8, column=0, padx=10, pady=5, sticky="ew")
peso_piezas_frame_2.grid_columnconfigure((0, 1), weight=1)

peso_label_2 = ctk.CTkLabel(peso_piezas_frame_2, text="Peso Actual: 0 Kg", font=("Arial", 12, "bold"))
peso_label_2.grid(row=0, column=0, padx=(100, 10), pady=5, sticky="w")

piezas_label_2 = ctk.CTkLabel(peso_piezas_frame_2, text="Piezas: 0", font=("Arial", 12, "bold"))
piezas_label_2.grid(row=0, column=1, padx=(10, 100), pady=5, sticky="e")

# Botones de control en Puesto 2
ctrl_homog_2 = ctk.CTkCheckBox(frame_2, text="Ctrl Homog", font=("Arial", 12), variable=ctrl_homog_var_2)
ctrl_homog_2.grid(row=9, column=0, padx=(120, 10), pady=10, sticky="w")

validar_peso_2 = ctk.CTkCheckBox(frame_2, text="Validar Peso", font=("Arial", 12), variable=validar_peso_var_2)
validar_peso_2.grid(row=9, column=0, padx=(10, 120), pady=10, sticky="e")

# Añadimos el botón de EDIT CTRL y el botón de cruz roja
edit_ctrl_frame_2 = ctk.CTkFrame(frame_2)
edit_ctrl_frame_2.grid(row=10, column=0, padx=10, pady=10, sticky="ew")
edit_ctrl_frame_2.grid_columnconfigure((0, 1), weight=1)

edit_ctrl_button_2 = ctk.CTkButton(edit_ctrl_frame_2, text="EDIT CTRL", width=120, height=30, corner_radius=10, fg_color="#4a90e2", hover_color="#3e7db4")
edit_ctrl_button_2.grid(row=0, column=0, padx=10, pady=10, sticky="w")

cerrar_button_2 = ctk.CTkButton(edit_ctrl_frame_2, text="✖", width=80, height=30, corner_radius=10, fg_color="#ff4d4d")
cerrar_button_2.grid(row=0, column=1, padx=10, pady=10, sticky="e")

# Configuración del loop principal de la app
app.mainloop()

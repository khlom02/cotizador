import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cotizador")
app.geometry("1000x720")
app.resizable(True, True)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

container = ctk.CTkFrame(app, corner_radius=0)
container.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

img_frame = ctk.CTkFrame(
    container,
    height=40,
    corner_radius=2,
    fg_color="white",
    border_width=1,
    border_color="#333333",
)
img_frame.grid(row=0, column=0, columnspan=4, padx=20, pady=(10, 12), sticky="ew")
img_label = ctk.CTkLabel(img_frame, text="IMAGEN PRINCIPAL", text_color="#333333")
img_label.place(relx=0.5, rely=0.5, anchor="center")

btn_nombre = ctk.CTkButton(
    container, text="NOMBRE", height=24, fg_color="#2c5aa0", corner_radius=2
)
btn_nombre.grid(row=1, column=0, columnspan=2, padx=(20, 8), pady=6, sticky="ew")

btn_fecha = ctk.CTkButton(
    container, text="FECHA", height=24, fg_color="#2c5aa0", corner_radius=2
)
btn_fecha.grid(row=1, column=2, columnspan=2, padx=(8, 20), pady=6, sticky="ew")

btn_equipaje = ctk.CTkButton(
    container, text="EQUIPAJE", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_equipaje.grid(row=2, column=0, padx=(20, 8), pady=6, sticky="ew")

btn_aerolinea = ctk.CTkButton(
    container, text="AEROLINEA", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_aerolinea.grid(row=2, column=1, padx=8, pady=6, sticky="ew")

btn_hora_arrivo = ctk.CTkButton(
    container, text="HORA ARRIVO", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_hora_arrivo.grid(row=2, column=2, columnspan=2, padx=(8, 20), pady=6, sticky="ew")

btn_origen = ctk.CTkButton(
    container, text="ORIGEN", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_origen.grid(row=3, column=0, padx=(20, 8), pady=6, sticky="ew")

btn_destino = ctk.CTkButton(
    container, text="DESTINO", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_destino.grid(row=3, column=1, padx=8, pady=6, sticky="ew")

btn_hora_salida = ctk.CTkButton(
    container, text="HORA SALIDA", height=22, fg_color="#2c5aa0", corner_radius=2
)
btn_hora_salida.grid(row=3, column=2, padx=8, pady=6, sticky="ew")

btn_tarifa = ctk.CTkButton(
    container,
    text="TARIFA",
    height=22,
    fg_color="#f2c94c",
    text_color="#000000",
    corner_radius=2,
)
btn_tarifa.grid(row=3, column=3, padx=(8, 20), pady=6, sticky="ew")

obs_frame = ctk.CTkFrame(
    container,
    height=90,
    corner_radius=2,
    fg_color="white",
    border_width=1,
    border_color="#333333",
)
obs_frame.grid(row=4, column=0, columnspan=4, padx=20, pady=(10, 8), sticky="nsew")
obs_label = ctk.CTkLabel(
    obs_frame, text="OBSERVACIONES Y CONDICIONES", text_color="#333333"
)
obs_label.place(relx=0.5, rely=0.5, anchor="center")

cond_frame = ctk.CTkFrame(
    container,
    height=90,
    corner_radius=2,
    fg_color="white",
    border_width=1,
    border_color="#333333",
)
cond_frame.grid(row=5, column=0, columnspan=4, padx=20, pady=(6, 12), sticky="nsew")
cond_label = ctk.CTkLabel(
    cond_frame, text="CONDICIONES GENERALES", text_color="#333333"
)
cond_label.place(relx=0.5, rely=0.5, anchor="center")

btn_agregar = ctk.CTkButton(
    container,
    text="agregar otra cotizacion",
    height=28,
    fg_color="#2c5aa0",
    corner_radius=2,
)
btn_agregar.grid(row=6, column=0, columnspan=4, padx=40, pady=(0, 10), sticky="ew")

for col in range(4):
    container.grid_columnconfigure(col, weight=1)

container.grid_rowconfigure(4, weight=1)
container.grid_rowconfigure(5, weight=1)

app.mainloop()


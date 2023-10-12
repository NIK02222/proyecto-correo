import tkinter as tk
from tkinter import messagebox
import smtplib

def enviar_correo():
    # Configurar el servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Obtener los valores de entrada del usuario
    correo_destino = destino_entry.get()
    asunto = asunto_entry.get()
    mensaje = mensaje_text.get("1.0", "end-1c")  # Obtener el texto del Text widget

    # Obtener las credenciales (asegúrate de que tu cuenta de Gmail permita el acceso de aplicaciones menos seguras o utiliza OAuth 2.0)
    correo_emisor = "tucorreo@gmail.com"  # Cambia esto
    contrasena = "tucontraseña"  # Cambia esto

    try:
        # Iniciar la conexión SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(correo_emisor, contrasena)

        # Codificar el asunto y el cuerpo del mensaje en UTF-8
        asunto = asunto.encode("utf-8")
        mensaje = mensaje.encode("utf-8")

        # Crear el mensaje
        mensaje_correo = f"Subject: {asunto.decode('utf-8')}\n\n{mensaje.decode('utf-8')}"

        # Enviar el correo
        server.sendmail(correo_emisor, correo_destino, mensaje_correo)

        # Cerrar la conexión
        server.quit()

        messagebox.showinfo("Éxito", "Correo enviado exitosamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo: {str(e)}")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Enviar Correo")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Destinatario (Gmail):").pack()
destino_entry = tk.Entry(ventana)
destino_entry.pack()

tk.Label(ventana, text="Asunto:").pack()
asunto_entry = tk.Entry(ventana)
asunto_entry.pack()

tk.Label(ventana, text="Mensaje:").pack()
mensaje_text = tk.Text(ventana, height=5, width=30)
mensaje_text.pack()

# Botón para enviar el correo
enviar_button = tk.Button(ventana, text="Enviar Correo", command=enviar_correo)
enviar_button.pack()

ventana.mainloop()



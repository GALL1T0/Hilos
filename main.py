import tkinter as tk
import threading
from PIL import Image, ImageTk

class MoverImagen(threading.Thread):
    def __init__(self, canvas, imagen, x=2, y=0):
        threading.Thread.__init__(self)
        self.canvas = canvas
        self.imagen = imagen
        self.x = x
        self.y = y

    def run(self):
        while True:
            self.canvas.move(self.imagen, self.x, self.y)
            self.canvas.after(100)
            self.canvas.update()

def main():
    ventana = tk.Tk()
    canvas = tk.Canvas(ventana, width=500, height=500)
    canvas.pack()

    imagen1 = Image.open('miles.png')  # Asegúrate de tener esta imagen en tu directorio
    imagen1 = imagen1.resize((100, 100), Image.LANCZOS)  # Redimensiona la imagen a 50x50 píxeles
    imagen1 = ImageTk.PhotoImage(imagen1)

    imagen2 = Image.open('venom.png')  # Asegúrate de tener esta imagen en tu directorio
    imagen2 = imagen2.resize((100, 100), Image.LANCZOS)  # Redimensiona la imagen a 50x50 píxeles
    imagen2 = ImageTk.PhotoImage(imagen2)

    imagen1_id = canvas.create_image(0, 250, image=imagen1)
    imagen2_id = canvas.create_image(250, 0, image=imagen2)

    mover_imagen1 = MoverImagen(canvas, imagen1_id, x=2)
    mover_imagen2 = MoverImagen(canvas, imagen2_id, y=2)

    mover_imagen1.start()
    mover_imagen2.start()

    ventana.mainloop()

if __name__ == "__main__":
    main()

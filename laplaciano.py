import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def cargar_imagen():
    tipos_archivos = [('Imágenes', '*.png;*.jpg;*.jpeg;*.gif')]
    ruta_archivo = filedialog.askopenfilename(filetypes=tipos_archivos)
    if ruta_archivo:
        try:
            imagen_original = Image.open(ruta_archivo)

            kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)

            img1 = cv2.imread(ruta_archivo)
            img2 = cv2.filter2D(img1, -1, kernel=kernel)

            cv2.imwrite('laplace-imagen.png', img2)
            img_laplace = Image.open('laplace-imagen.png')

            imagen_original_tk = ImageTk.PhotoImage(imagen_original)
            img_laplace_tk = ImageTk.PhotoImage(img_laplace)

            ventana_resultado = tk.Toplevel(root)

            canvas = tk.Canvas(ventana_resultado, width=imagen_original.width * 2, height=imagen_original.height)
            canvas.pack()

            canvas.create_image(0, 0, anchor=tk.NW, image=imagen_original_tk)
            canvas.create_image(imagen_original.width, 0, anchor=tk.NW, image=img_laplace_tk)

            ventana_resultado.mainloop()

        except Exception as e:
            print("Error al procesar la imagen:", e)

root = tk.Tk()

boton_cargar = tk.Button(root, text="Cargar imagen", command=cargar_imagen)
boton_cargar.pack()

root.mainloop()

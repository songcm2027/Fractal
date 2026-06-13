import numpy as np
from PIL import Image

WIDTH, HEIGHT = 1200, 900
MAX_ITER = 256

X_MIN, X_MAX = -2.5, 1.0
Y_MIN, Y_MAX = -1.25, 1.25

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def ocean_color(n, max_iter):
    if n == max_iter:
        return (0, 0, 0)
    t = n / max_iter
    r = int(9 * (1 - t) * t**3 * 255)
    g = int(15 * (1 - t)**2 * t**2 * 255)
    b = int(8.5 * (1 - t)**3 * t * 255 + t * 200)
    return (
        min(255, max(0, r)),
        min(255, max(0, g + int(t * 100))),
        min(255, max(0, b))
    )

print("Generating Mandelbrot fractal... (this may take 30-60 seconds)")

pixels = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

for y in range(HEIGHT):
    for x in range(WIDTH):
        real = X_MIN + (X_MAX - X_MIN) * x / WIDTH
        imag = Y_MIN + (Y_MAX - Y_MIN) * y / HEIGHT
        c = complex(real, imag)
        n = mandelbrot(c, MAX_ITER)
        pixels[y, x] = ocean_color(n, MAX_ITER)

img = Image.fromarray(pixels, "RGB")
img.save("fractal.png")
print("Done! Saved as fractal.png")
print("Open it with: open fractal.png")
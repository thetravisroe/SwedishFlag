import tkinter as tk

WIDTH = 600
HEIGHT = 400

# Create window
root = tk.Tk()
root.title("Swedish Flag")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Draw blue background
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#006aa7", width=0)

# Draw yellow cross
# Vertical stripe
canvas.create_rectangle(WIDTH*0.30, 0, WIDTH*0.42, HEIGHT, fill="#fecc00", width=0)
# Horizontal stripe
canvas.create_rectangle(0, HEIGHT*0.40, WIDTH, HEIGHT*0.55, fill="#fecc00", width=0)

root.mainloop()

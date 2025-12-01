import tkinter as tk
import math

WIDTH = 600
HEIGHT = 400

class SwedishFlagApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Swedish Flag")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self._draw_flag()

        self.t = 0      # time / frame counter
        self.offset = 0 # last horizontal offset applied

        self.animate()

    def _draw_flag(self):
        
        blue = "#006aa7"
        yellow = "#fecc00"

        self.canvas.create_rectangle(
            0, 0, WIDTH, HEIGHT, fill=blue, width=0, tags="flag"
        )
        
        self.canvas.create_rectangle(
            WIDTH * 0.30, 0,
            WIDTH * 0.42, HEIGHT,
            fill=yellow, width=0, tags="flag"
        )

        self.canvas.create_rectangle(
            0, HEIGHT * 0.40,
            WIDTH, HEIGHT * 0.55,
            fill=yellow, width=0, tags="flag"
        )

        self.canvas.create_rectangle(
            WIDTH * 0.02, 0,
            WIDTH * 0.06, HEIGHT,
            fill="#aaaaaa", width=0
        )

    def animate(self):
        """
        Simple animation: gently sway the flag left and right
        using a sine wave on the whole flag group.
        """

        self.canvas.move("flag", -self.offset, 0)

        amplitude = 8  # how far it swings left/right in pixels
        speed = 0.08   # how fast it swings
        self.t += 1
        new_offset = amplitude * math.sin(self.t * speed)

        self.canvas.move("flag", new_offset, 0)
        self.offset = new_offset

        self.root.after(20, self.animate)  # ~50 FPS

if __name__ == "__main__":
    root = tk.Tk()
    app = SwedishFlagApp(root)
    root.mainloop()

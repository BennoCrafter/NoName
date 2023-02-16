import tkinter as tk
import json

# Define some constants for the pixel grid
PIXEL_SIZE = 20
PIXEL_ROWS = 30
PIXEL_COLS = 30

# Define some colors
to_num = {"white": 0, "blue": 1, "red": 2, "green": 3, "yellow": 4, "black": 5, "orange": 6}
BLUE = "blue"
RED = "red"
GREEN = "green"
YELLOW = "yellow"
BLACK = "black"
ORANGE = "orange"
WHITE = "white"

# Initialize a list to keep track of the current colors of each pixel
pixel_colors = [[0 for _ in range(PIXEL_COLS)] for _ in range(PIXEL_ROWS)]


def paint_pixel(event):
    # Get the row and column of the pixel that was clicked
    row = event.y // PIXEL_SIZE
    col = event.x // PIXEL_SIZE

    # Set the color of the pixel to the currently selected color
    pixel_colors[row][col] = to_num.get(current_color.get())

    # Draw the pixel in the canvas
    canvas.create_rectangle(
        col * PIXEL_SIZE, row * PIXEL_SIZE,
        (col + 1) * PIXEL_SIZE, (row + 1) * PIXEL_SIZE,
        fill=current_color.get()
    )


def save():
    print(pixel_colors)
    with open("painting.json", "w") as f:
        json.dump(pixel_colors, f)
    f.close()


def load_painting():
    global pixel_colors
    with open("painting.json", "r") as file:
        pixels = json.load(file)
    file.close()
    for row, all_row in enumerate(pixels):
        for z, colum in enumerate(all_row):
            keys = [k for k, v in to_num.items() if v == all_row[z]]
            canvas.create_rectangle(
                z * PIXEL_SIZE, row * PIXEL_SIZE,
                (z + 1) * PIXEL_SIZE, (row + 1) * PIXEL_SIZE,
                fill=keys[0]
            )
    print("loaded successfully!")
    pixel_colors = pixels


def print_colors():
    print(pixel_colors)

# Initialize the GUI
root = tk.Tk()
root.title("Pixel Raster Drawing")

# Create a frame for the color selection buttons
color_frame = tk.Frame(root)
color_frame.pack(side=tk.TOP)

# Create the color selection buttons
current_color = tk.StringVar()
current_color.set(BLUE)
tk.Radiobutton(color_frame, text="Blue", variable=current_color, value=BLUE).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="Red", variable=current_color, value=RED).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="Green", variable=current_color, value=GREEN).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="Yellow", variable=current_color, value=YELLOW).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="Black", variable=current_color, value=BLACK).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="Orange", variable=current_color, value=ORANGE).pack(side=tk.LEFT)
tk.Radiobutton(color_frame, text="White", variable=current_color, value=WHITE).pack(side=tk.LEFT)

# Create the canvas for the pixel grid
canvas = tk.Canvas(root, width=PIXEL_SIZE * PIXEL_COLS, height=PIXEL_SIZE * PIXEL_ROWS)
canvas.pack()

# Initialize the pixel grid
for row in range(PIXEL_ROWS):
    for col in range(PIXEL_COLS):
        canvas.create_rectangle(
            col * PIXEL_SIZE, row * PIXEL_SIZE,
            (col + 1) * PIXEL_SIZE, (row + 1) * PIXEL_SIZE,
            fill="white"
        )

# Bind the left mouse button to the paint_pixel function
canvas.bind("<Button-1>", paint_pixel)

# Create a button to print the colors of the placed pixels
print_button = tk.Button(root, text="Run", command=print_colors)
print_button.pack()
save_button = tk.Button(root, text="Save", command=save)
save_button.pack()
load_button = tk.Button(root, text="Load", command=load_painting)
load_button.pack()

# Start the GUI main loop
root.mainloop()

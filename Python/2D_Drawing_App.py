import tkinter as tk
from tkinter import colorchooser

# initialize the main window
root = tk.Tk()
root.title("2D Drawing App")
root.geometry("800x600")

# variables to hold current drawing settings
current_color = "black"
current_shape = "line"
line_width = 2
start_X, start_Y = None, None

# canvas where the drawing happens
canvas = tk.Canvas(root, bg="white", width=800, height=500)
canvas.pack()

# function to change the color
def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
        
# function to set shape
def set_shape(shape):
    global current_shape
    current_shape = shape
    
# function to set line width
def set_line_width(width):
    global line_width
    line_width = width
    
# mouse events
def on_mouse_down(event):
    global start_X, start_Y
    start_X, start_Y = event.x, event.y
    
def on_mouse_up(event):
    global start_X, start_Y
    end_x, end_y = event.x, event.y
    
    if current_shape == "line":
        canvas.create_line(start_X, start_Y, end_x, end_y, fill=current_color, width=line_width)
    elif current_shape == 'rectangle':
        canvas.create_rectangle(start_X, start_Y, end_x, end_y, outline=current_color, width=line_width)
    elif current_shape == "circle":
        radius = ((end_x - start_X)**2 + (end_y - start_Y)**2)**0.5
        canvas.create_oval(start_X - radius, start_Y - radius, start_X + radius, start_Y + radius, outline=current_color, width=line_width)
        
# clear canvas
def clear_canvas():
    canvas.delete("all")
    
# bind mouse events
canvas.bind("<ButtonPress-1>", on_mouse_down)
canvas.bind("<ButtonRelease-1>", on_mouse_up)

# buttons for color, shape, and line width
color_button = tk.Button(root, text="Choose Color", command=change_color)
color_button.pack(side="left", padx=5, pady=5)

line_button = tk.Button(root, text="Line", command=lambda: set_shape("line"))
line_button.pack(side="left", padx=5, pady=5)

rectangle_button = tk.Button(root, text="Rectangle", command=lambda: set_shape("rectangle"))
rectangle_button.pack(side="left", padx=5, pady=5)

circle_button = tk.Button(root, text="Circle", command=lambda: set_shape("circle"))
circle_button.pack(side="left", padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side="left", padx=5, pady=5)

# Line width options
line_width_label = tk.Label(root, text="Line Width:")
line_width_label.pack(side="left", padx=5, pady=5)

for width in [2, 5, 8]:
    width_button = tk.Button(root, text=str(width), command=lambda w=width: set_line_width(w))
    width_button.pack(side="left", padx=2, pady=5)
    
# Run the application
root.mainloop()
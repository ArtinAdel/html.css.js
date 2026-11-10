import tkinter as tk

# Create the window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#202124")


# Display
display = tk.Entry(
    root,
    font=("Arial", 30),
    bg="#303134",
    fg="white",
    justify="right",
    bd=0
)

display.pack(
    padx=20,
    pady=25,
    ipady=15,
    fill="x"
)


# Add button value to the display
def click(value):
    display.insert(tk.END, value)


# Clear the display
def clear():
    display.delete(0, tk.END)


# Calculate the result
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons frame
buttons_frame = tk.Frame(root, bg="#202124")
buttons_frame.pack()


# Buttons
buttons = [
    ("C", 0, 0),
    ("/", 0, 1),
    ("*", 0, 2),
    ("-", 0, 3),

    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("+", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("(", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    (")", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
]


# Create the buttons
for text, row, column in buttons:

    # Blue buttons
    if text in ["C", "/", "*", "-", "+", "(", ")", "="]:
        button_color = "#64B5F6"
        active_color = "#42A5F5"

    # Number buttons
    else:
        button_color = "#000000"
        active_color = "#333333"

    if text == "C":
        command = clear

    elif text == "=":
        command = calculate

    else:
        command = lambda x=text: click(x)

    button = tk.Button(
        buttons_frame,
        text=text,
        command=command,
        font=("Arial", 18, "bold"),
        width=7,
        height=2,
        bg=button_color,
        fg="white",
        activebackground=active_color,
        activeforeground="white",
        bd=0
    )

    button.grid(
        row=row,
        column=column,
        padx=6,
        pady=6
    )


# Run the program
root.mainloop()

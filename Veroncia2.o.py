import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageOps

def submit_input():
    user_input = entry.get()
    display_label.config(text=f"You entered: {user_input}")

def create_circular_image(image, size):
    # Create a circular mask
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
    # Apply the circular mask to the image
    image = image.resize(size)
    circular_image = ImageOps.fit(image, size, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    
    return circular_image

def on_focus_in(event):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
    entry.config(fg='white' if dark_mode else 'black')

def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='gray')

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        root.config(bg='black')
        main_frame.config(style='Dark.TFrame')
        profile_label.config(background='black')
        entry.config(bg='black', fg='white', insertbackground='white')
        dark_mode_button.config(text="Light")
    else:
        root.config(bg='white')
        main_frame.config(style='Light.TFrame')
        profile_label.config(background='white')
        entry.config(bg='white', fg='black', insertbackground='black')
        #submit_button.config(style='Light.TButton')
        #display_label.config(style='Light.TLabel')
        dark_mode_button.config(text="Dark")

# Create the main window
root = tk.Tk()
root.title("Aurora's Calendar")

# Load and resize the profile picture
image_path = "Aurora_Profile_Pic.png"  # Replace with your image file path
image = Image.open("DP.png")

# Define the desired size
desired_size = (150, 150)  # Width, Height
circular_image = create_circular_image(image, desired_size)

photo = ImageTk.PhotoImage(circular_image)

# Create a style for dark mode
style = ttk.Style()
style.configure('Dark.TFrame', background='black')
style.configure('Dark.TButton', background='gray', foreground='white')
style.configure('Dark.TLabel', foreground='white')
style.configure('Light.TFrame', background='white')
style.configure('Light.TButton', background='lightgray', foreground='black')
style.configure('Light.TLabel', foreground='black')

dark_mode = False  # Start in light mode

# Create a frame for the profile picture and input
main_frame = ttk.Frame(root, padding="10", style='Light.TFrame')
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Profile picture label with circular frame
profile_label = ttk.Label(main_frame, image=photo, background='white')
profile_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Input bar
placeholder = "Enter input here"
entry = tk.Entry(main_frame, width=30, fg='gray', bg='white')
entry.insert(0, placeholder)
entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Bind focus events to handle placeholder text
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)
entry.bind("<Return>", submit_input)  # Bind Enter key to submit_input

# Submit button
submit_button = ttk.Button(main_frame, text="Submit", command=submit_input, style='Light.TButton')
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display label for the result
display_label = ttk.Label(main_frame, text="", style='Light.TLabel')
display_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Dark mode button
dark_mode_button = ttk.Button(root, text="Dark", command=toggle_dark_mode)
dark_mode_button.place(x=desired_size[0] + 5, y=5, width=45, height=30)  # Position the button over the image

# Run the main loop
root.mainloop()




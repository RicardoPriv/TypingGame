try:
    import tkinter as tk
except ImportError:
    exit()

def gui(root: tk):
    root.title("Typing Game")

    root.geometry("720x480")
    root.resizable(True, True)

    # Create and pack a label widget
    label = tk.Label(root, text="Enter something:")
    label.pack(pady=10)

    # Create and pack an entry widget
    entry = tk.Entry(root, width=20)
    entry.pack(pady=10)

    # Create and pack a button widget
    #button = tk.Button(root, text="Update Label", command=update_label)
    #button.pack(pady=10)
    print("test")
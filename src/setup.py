try:
    import tkinter as tk
    import random
except ImportError:
    exit()


def main_screen(root: tk):
    root.title("Typing Game")

    root.geometry("720x480")
    root.resizable(True, True)

    # Create and pack a label widget
    root.correct_word = random.choice(root.words)
    label = tk.Label(root, text=root.correct_word)
    label.pack(pady=10)

    # Create and pack an entry widget
    entry = tk.Entry(root, width=20)
    entry.pack(pady=10)
    entry.focus_set()

    # Create and pack a button widget
    button = tk.Button(root, text="Submit", font=("Helvetica", 14))
    button.pack(pady=10)

    # Create a timer
    timer_label = tk.Label(root, text="00:00", font=("Helvetica", 14))
    timer_label.place(relx=1.0, rely=0.0, anchor='ne')
    root.timer_label = timer_label

    # Initialize the timer value
    root.timer_value = 0

    # Start the timer
    update_timer(root)

    # Store for access in other functions
    root.label = label
    root.entry = entry
    
    root.score = 0
    return

def update_timer(root):
    root.timer_value += 1

    seconds = (root.timer_value // 100) % 60
    hundredths = root.timer_value % 100
    
    time_string = f"{seconds:02}:{hundredths:02}"
    
    root.timer_label.config(text=time_string)
    root.after(10, update_timer, root)
    return
    
def on_return_press(event, root):
    entry_widget = event.widget
    if isinstance(entry_widget, tk.Entry):
        user_input = entry_widget.get()
        if user_input == root.correct_word:
            root.score += 1
            root.config(bg='green')
        else:
            root.config(bg='red')
    
        root.correct_word = random.choice(root.words)
        root.label.config(text=root.correct_word)
        root.entry.delete(0, tk.END)
    return

def on_escape_press(event, root):
    root.destroy()

def function_bindings(root: tk):
    root.bind("<Return>", lambda event: on_return_press(event, root))
    root.bind("<Escape>", lambda event: on_escape_press(event, root))
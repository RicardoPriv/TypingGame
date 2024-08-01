try:
    import tkinter as tk
    import random
except ImportError:
    exit()


def start_screen(root: tk):
    destroy_widgets(root)
    root.geometry("800x600")
    root.resizable(True, True)
    root.config(bg='lightblue')

    # Start Screen Title
    start_title = tk.Label(root, text="Welcome to Typing Game!", font=("Helvetica", 32, "bold"), bg='lightblue')
    start_title.pack(pady=100)

    # Start Screen Instructions
    instruction_label = tk.Label(root, text="Press 'S' to Start", font=("Helvetica", 20), bg='lightblue')
    instruction_label.pack(pady=20)

    # Additional Decorative Label (Optional)
    start_subtitle = tk.Label(root, text="Prepare your fingers for a typing challenge!", font=("Helvetica", 18), bg='lightblue')
    start_subtitle.pack(pady=20)
    

def main_screen(root: tk):
    root.title("Typing Game")
    root.geometry("800x600")
    root.resizable(True, True)
    root.config(bg='lightblue')

    # Title label
    title_label = tk.Label(root, text="Typing Game", font=("Helvetica", 24, "bold"), bg='lightblue')
    title_label.pack(pady=20)

    # Score, level, and lives frame
    root.info_frame = tk.Frame(root, bg='lightblue')
    root.info_frame.pack(pady=10)

    # Lives label
    root.lives_label = tk.Label(root.info_frame, text=f"Lives: {root.lives}", font=("Helvetica", 14), bg='lightblue')
    root.lives_label.pack(side="left", padx=20)

    # Score label
    root.score_label = tk.Label(root.info_frame, text=f"Score: {root.score}", font=("Helvetica", 14), bg='lightblue')
    root.score_label.pack(side="left", padx=20)

    # Level label
    root.level_label = tk.Label(root.info_frame, text=f"Level: {root.level}", font=("Helvetica", 14), bg='lightblue')
    root.level_label.pack(side="left", padx=20)

    # Correct word label
    root.label = tk.Label(root, text=root.correct_word, font=("Helvetica", 18), bg='lightblue')
    root.label.pack(pady=20)

    # Entry widget
    root.entry = tk.Entry(root, width=30, font=("Helvetica", 14))
    root.entry.pack(pady=10)
    root.entry.focus_set()

    # Submit button
    root.button = tk.Button(root, text="Submit", font=("Helvetica", 14))
    root.button.pack(pady=10)

    # Timer label
    root.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 14), bg='lightblue')
    root.timer_label.place(relx=1.0, rely=0.0, anchor='ne')

    

def game_over(root: tk):
    root.title("Game Over")
    root.geometry("800x600")
    root.config(bg='lightcoral')

    # Game Over message
    game_over_label = tk.Label(root, text="Game Over", font=("Helvetica", 32, "bold"), bg='lightcoral')
    game_over_label.pack(pady=100)

    # Display final score
    final_score_label = tk.Label(root, text=f"Your Score: {root.score}", font=("Helvetica", 24), bg='lightcoral')
    final_score_label.pack(pady=20)

    # Restart or Exit instructions
    restart_label = tk.Label(root, text="Press 's' to Restart or 'q' to Quit", font=("Helvetica", 20), bg='lightcoral')
    restart_label.pack(pady=20)

    root.game_running = False
    

def pause_screen(root: tk):
    root.title("Game Paused")
    root.geometry("800x600")
    root.resizable(True, True)
    root.config(bg='grey')

    pause_label = tk.Label(root, text="Game Paused", font=("Helvetica", 24, "bold"), bg='grey')
    pause_label.pack(pady=200)

    info_label = tk.Label(root, text="Press Tab to Resume", font=("Helvetica", 14), bg='grey')
    info_label.pack(pady=20)

def destroy_widgets(root: tk):
    for widget in root.winfo_children():
        widget.destroy()
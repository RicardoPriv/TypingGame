try:
    import tkinter as tk
    import random
    import threading
    import time
    from scraper import scrape_words
except ImportError:
    exit()

def start_game() -> tk:
    root = tk.Tk()

    game_variables(root)
    main_screen(root)
    update_timer(root)
    function_bindings(root)
    return root

def game_variables(root: tk):
    root.words = scrape_words(3)
    root.score = 0
    root.words_entered = 0
    root.level = 1
    root.lives = 3
    root.timer_value = 0
    root.updating_level = threading.Event()
    root.game_running = True
    return

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
    root.correct_word = random.choice(root.words)
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
    return

def new_level(root: tk.Tk):
    root.label.config(text="Loading next level...", font=("Helvetica", 18), bg='lightblue')
    root.update_idletasks()
    
    def update_words():
        time.sleep(2)  # Simulate a delay for loading words
        root.level += 1
        root.words = scrape_words(root.level + 2)
        root.correct_word = random.choice(root.words)
        root.after(0, complete_new_level, root)

    def complete_new_level(root: tk.Tk):
        root.label.config(text=root.correct_word)
        root.level_label.config(text=f"Level: {root.level}")
        root.updating_level.clear()  # Release the event

    root.updating_level.set()  # Set the event to indicate level update
    threading.Thread(target=update_words).start()

def game_over(root: tk):
    root.label.config(text="Game Over", font=("Helvetica", 18))
    root.config(bg='red')
    root.game_running = False
    return

def update_timer(root: tk.Tk):
    if not root.game_running:
        return False

    if not root.updating_level.is_set():
        root.timer_value += 1

    minutes = (root.timer_value // 6000) % 60
    seconds = (root.timer_value // 100) % 60
    hundredths = root.timer_value % 100

    time_string = f"{minutes:02}:{seconds:02}:{hundredths:02}"

    root.timer_label.config(text=time_string)
    root.after(10, update_timer, root)
    return
    
def on_return_press(event, root):
    if root.updating_level.is_set() or not root.game_running:
        return
    
    entry_widget = event.widget
    if isinstance(entry_widget, tk.Entry):
        user_input = entry_widget.get()
        if user_input == root.correct_word:
            root.score += len(root.correct_word)
            root.score_label.config(text=f"Score: {root.score}")
            root.config(bg='green')
        else:
            root.lives -= 1
            root.lives_label.config(text=f"Lives: {root.lives}")
            root.config(bg='orange')

        root.words_entered += 1

        if root.words_entered % 10 == 0 and root.level < 14 and root.words_entered != 0:
            new_level(root)
        else:        
            root.correct_word = random.choice(root.words)
            root.label.config(text=root.correct_word)
        
        root.entry.delete(0, tk.END)

        if root.lives == 0:
            game_over(root)
    return

def on_escape_press(event, root):
    root.destroy()

def function_bindings(root: tk):
    root.bind("<Return>", lambda event: on_return_press(event, root))
    root.bind("<Escape>", lambda event: on_escape_press(event, root))
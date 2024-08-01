try:
    import tkinter as tk
    import random
    import threading
    import time
    from scraper import scrape_words
    from screens import *
except ImportError:
    exit()

def start() -> tk:
    root = tk.Tk()
    root.game_running = False

    start_screen(root)
    function_bindings(root)
    return root

def game_variables(root: tk):
    root.words = scrape_words(3)
    root.correct_word = random.choice(root.words)
    root.score = 0
    root.words_entered = 0
    root.level = 1
    root.lives = 3
    root.timer_value = 0
    root.updating_level = threading.Event()
    root.game_running = True

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
    

def new_level(root: tk.Tk):
    root.label.config(text="Loading next level...", font=("Helvetica", 18), bg='lightblue')
    root.update_idletasks()
    
    def update_words():
        time.sleep(2)  # Simulate a delay for loading words
        root.level += 1
        root.lives += 1
        root.words = scrape_words(root.level + 2)
        root.correct_word = random.choice(root.words)
        root.after(0, complete_new_level, root)

    def complete_new_level(root: tk.Tk):
        root.label.config(text=root.correct_word)
        root.level_label.config(text=f"Level: {root.level}")
        root.lives_label.config(text=f"Lives: {root.lives}")
        root.updating_level.clear()  # Release the event

    root.updating_level.set()  # Set the event to indicate level update
    threading.Thread(target=update_words).start()
    
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
            destroy_widgets(root)
            game_over(root)
    

def on_escape_press(event, root):
    root.destroy()

def on_game_start(root: tk):
    if root.game_running:
        return
    
    game_variables(root)
    destroy_widgets(root)
    main_screen(root)
    update_timer(root)

def on_tab_pause(root: tk):
    if root.game_running or root.title() == "Game Paused":
        destroy_widgets(root)
        
        if root.game_running:
            pause_screen(root)
            root.game_running = False
        else:
            main_screen(root)
            root.game_running = True
            update_timer(root)

def function_bindings(root: tk):
    root.bind("<Return>", lambda event: on_return_press(event, root))
    root.bind("<Escape>", lambda event: on_escape_press(event, root))
    root.bind("<Key-s>", lambda event: on_game_start(root))
    root.bind("<Key-q>", lambda event: root.destroy())
    root.bind("<Key-Tab>", lambda event: on_tab_pause(root))
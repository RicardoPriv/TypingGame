try:
    import tkinter as tk
    import random
except ImportError:
    exit()
    
from setup import main_screen, function_bindings
from scraper import scrape_words

def start() -> tk:
    words = scrape_words(5)
    root = tk.Tk()
    root.words = words
    main_screen(root)
    function_bindings(root)
    return root

def main():
    root = start()
    root.mainloop()

if __name__ == "__main__":
    main()
try:
    import tkinter as tk
except ImportError:
    exit()
    
from setup import start_game
from scraper import scrape_words

def main():
    root = start_game()
    root.mainloop()

if __name__ == "__main__":
    main()

#Token password for pushing
# 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
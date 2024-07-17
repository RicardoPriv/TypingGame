try:
    import tkinter as tk
except ImportError:
    exit()
    
from gui import gui
from scraper import scrape_words

def main():
    words = scrape_words(5)
    print(words)
    #root = tk.Tk()
    #gui(root)
    #root.mainloop()

if __name__ == "__main__":
    main()
try:
    import time
    from setup import start
except ImportError:
    exit()

def main():
    root = start()
    root.mainloop()

if __name__ == "__main__":
    main()
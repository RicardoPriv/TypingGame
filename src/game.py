try:
    from setup import start
except ImportError:
    print("Error with loading packages - Please try again")
    exit(1)


def main():
    root = start()
    root.mainloop()

if __name__ == "__main__":
    main()
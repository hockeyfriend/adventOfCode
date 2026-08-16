import os

def main():
    p = os.path.join(os.path.dirname(__file__), "puzzle.txt")

    with open(p, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()


if __name__ == "__main__":
    main()

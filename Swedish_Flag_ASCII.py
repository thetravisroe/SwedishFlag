BLUE = "\033[44m"
YELLOW = "\033[43m"
RESET = "\033[0m"

# Flag dimensions
rows = 15
cols = 40

for r in range(rows):
    line = ""
    for c in range(cols):
        if r in range (6, 8): # Horizontal yellow stripe
            line += YELLOW + " " + RESET
        elif c in range(10, 13): # Vertical yellow stripe
            line += YELLOW + " " + RESET
        else:
            line += BLUE + " " + RESET
    print(line) 
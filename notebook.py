#!/usr/bin/env python3
import os
import sys
from datetime import datetime

LOG_FILE = "pentest_log.txt"
FOOTER_LINES = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_height():
    return os.get_terminal_size().lines

def render(lines):
    """Renderiza o buffer atual com ~ preenchendo o terminal."""
    clear()
    height = terminal_height()
    usable = height - FOOTER_LINES - 1  

    display = []
    for line in lines:
        display.append(line if line.strip() != "" else "~")

    remaining = usable - len(display)
    for _ in range(max(0, remaining)):
        display.append("~")

    display = display[-usable:]

    print("\n".join(display))

def save(lines):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        for line in lines:
            if line.strip() == "":
                continue
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"[{timestamp}] {line}\n")

def main():
    lines = []
    render(lines)

    try:
        while True:
            try:
                line = input()
                lines.append(line)
                render(lines)
            except EOFError:
                sys.exit(0)
    except KeyboardInterrupt:
        save(lines)

if __name__ == "__main__":
    main()

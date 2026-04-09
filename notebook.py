#!/usr/bin/env python3
import os
import sys
from datetime import datetime

FOOTER_LINES = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_height():
    return os.get_terminal_size().lines

def render(lines):
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

def save(lines, log_file):
    with open(log_file, "a", encoding="utf-8") as f:
        for line in lines:
            if line.strip() == "":
                continue
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"[{timestamp}] {line}\n")

def ask_filename():
    clear()
    print("Nome do arquivo de log (Enter para 'pentest_log.txt'): ", end="", flush=True)
    name = input().strip()
    if not name:
        name = "pentest_log.txt"
    if not name.endswith(".txt"):
        name += ".txt"
    return name

def main():
    log_file = ask_filename()
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
        save(lines, log_file)

if __name__ == "__main__":
    main()

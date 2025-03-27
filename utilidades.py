import os

def clear_screen():
    if os.name == 'posix':  # Para Linux o macOS
        os.system('clear')
    elif os.name == 'nt':   # Para Windows
        os.system('cls')

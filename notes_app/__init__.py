from lib import display, userinput, sdcard
import time
from font import vga1_8x16 as font  


WHITE = 0xFFFF
BLACK = 0x0000


DISPLAY = display.Display()
INPUT = userinput.UserInput()
SD = sdcard.SDCard()
SD.mount()

FILE_PATH = '/sd/notes.txt'



def save_note_to_file(note):
    try:
        with open(FILE_PATH, 'a') as f:
            f.write(note + '\n')
        return True
    except Exception as e:
        print("Error saving note:", e)
        return False

def load_notes_from_file():
    try:
        with open(FILE_PATH, 'r') as f:
            return f.readlines()
    except Exception as e:
        print("Error loading notes:", e)
        return []

def draw_text(x, y, text, color):
    cursor_x = x
    for char in text:
        if char == ' ':
            cursor_x += 8  
        else:
            DISPLAY.text(char, cursor_x, y, color, font=font)
            cursor_x += 8

def main_menu():
    DISPLAY.fill(BLACK)
    draw_text(10, 40, "1. Write Note", WHITE)
    draw_text(10, 60, "2. Read Notes", WHITE)
    DISPLAY.show()

def read_notes():
    notes = load_notes_from_file()
    screen_index = 0
    lines_per_page = 7  
    max_index = max(0, len(notes) - lines_per_page)  
    
    while True:
        DISPLAY.fill(BLACK)
        for i in range(lines_per_page):  
            if screen_index + i < len(notes):
                draw_text(5, i * 20, notes[screen_index + i].strip(), WHITE)
        DISPLAY.show()

        keys = INPUT.get_new_keys()
        if 'UP' in keys and screen_index > 0:
            screen_index -= 1
        elif 'DOWN' in keys and screen_index < max_index:
            screen_index += 1
        elif 'ESC' in keys:
            return


def write_note():
    current_note = ""
    while True:
        keys = INPUT.get_new_keys()
        if keys:
            for key in keys:
                if key == "ENT":
                    if current_note:
                        save_note_to_file(current_note)
                        return
                elif key == "BSPC":
                    current_note = current_note[:-1]
                elif key == "SPC":
                    current_note += " "
                elif len(key) == 1:
                    current_note += key

        DISPLAY.fill(BLACK)
        draw_text(5, 50, current_note, WHITE)
        DISPLAY.show()
        time.sleep_ms(100)

def main_loop():
    while True:
        main_menu()
        keys = INPUT.get_new_keys()
        if '1' in keys:
            write_note()
        elif '2' in keys:
            read_notes()


main_loop()

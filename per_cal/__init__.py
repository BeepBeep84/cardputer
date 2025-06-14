from lib import display, userinput
from lib.hydra import config
import time
from font import vga1_8x16 as font  


_MH_DISPLAY_HEIGHT = const(135)  
_MH_DISPLAY_WIDTH = const(240)   
_MAX_CHARS_PER_LINE = _MH_DISPLAY_WIDTH // 8  



DISPLAY = display.Display()

CONFIG = config.Config()

INPUT = userinput.UserInput()



def calculate_percentage(option, a, b):
    """Perform percentage calculations based on the selected option."""
    if option == 1:
        return a * (b / 100) 
    elif option == 2:
        return (a / b) * 100  
    elif option == 3:
        return ((b - a) / a) * 100 
    elif option == 4:
        return a / (b / 100)  
    elif option == 5:
        return abs(a - b) / ((a + b) / 2) * 100  
    else:
        return None

def wrap_text(text, max_chars_per_line):
    """Wrap text into multiple lines based on max characters per line."""
    lines = []
    while len(text) > max_chars_per_line:
        space_index = text.rfind(' ', 0, max_chars_per_line)  
        if space_index == -1:
            lines.append(text[:max_chars_per_line])
            text = text[max_chars_per_line:]
        else:
            lines.append(text[:space_index])
            text = text[space_index + 1:]  
    lines.append(text)  
    return lines

def display_wrapped_text(lines, x, y, color):
    """Display wrapped text on the display starting from position (x, y)."""
    line_height = 16  
    for i, line in enumerate(lines):
        DISPLAY.text(line, x, y + i * line_height, color, font=font)

def main_loop():
    input_number1 = ""
    input_number2 = ""
    result = ""
    display_mode = "menu"  
    option = None  

    while True:
        keys = INPUT.get_new_keys()

        if keys:
            if display_mode == "menu":
                if "1" in keys:
                    option = 1
                    display_mode = "input1"
                elif "2" in keys:
                    option = 2
                    display_mode = "input1"
                elif "3" in keys:
                    option = 3
                    display_mode = "input1"
                elif "4" in keys:
                    option = 4
                    display_mode = "input1"
                elif "5" in keys:
                    option = 5
                    display_mode = "input1"

            elif display_mode == "input1":
                if "ENT" in keys:
                    if input_number1:
                        display_mode = "input2"
                else:
                    for key in keys:
                        if key.isdigit() or key == ".":
                            input_number1 += key
                        elif key == "BSPC":
                            input_number1 = input_number1[:-1]
                        elif key == "CLR":
                            input_number1 = ""

            elif display_mode == "input2":
                if "ENT" in keys:
                    if input_number2:
                        a = float(input_number1)
                        b = float(input_number2)
                        result = calculate_percentage(option, a, b)
                        display_mode = "result"
                else:
                    for key in keys:
                        if key.isdigit() or key == ".":
                            input_number2 += key
                        elif key == "BSPC":
                            input_number2 = input_number2[:-1]
                        elif key == "CLR":
                            input_number2 = ""

            elif display_mode == "result":
                if "ENT" in keys:
                    input_number1 = ""
                    input_number2 = ""
                    result = ""
                    display_mode = "menu"

        DISPLAY.fill(CONFIG.palette[2])

        if display_mode == "menu":
            DISPLAY.text(
                text="1. What is X% of Y?",
                x=5, 
                y=10,  
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text="2. X is what % of Y?",
                x=5, 
                y=35,  
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text="3. % change from X to Y?",
                x=5, 
                y=60,  
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text="4. X is Y% of what?",
                x=5, 
                y=85,  
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text="5. % difference X and Y?",
                x=5, 
                y=110,  
                color=CONFIG.palette[8],
                font=font
            )
        elif display_mode == "input1":
            DISPLAY.text(
                text="Enter first number:",
                x=5, 
                y=30,
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text=input_number1,
                x=5,
                y=60,
                color=CONFIG.palette[8],
                font=font
            )
        elif display_mode == "input2":
            DISPLAY.text(
                text="Enter second number:",
                x=5, 
                y=30,
                color=CONFIG.palette[8],
                font=font
            )
            DISPLAY.text(
                text=input_number2,
                x=5,
                y=60,
                color=CONFIG.palette[8],
                font=font
            )
        elif display_mode == "result":
            result_text = {
                1: f"{input_number1}% of {input_number2} = {result}",
                2: f"{input_number1} is {result}% of {input_number2}",
                3: f"Change from {input_number1} to {input_number2} = {result}%",
                4: f"{input_number1} is {input_number2}% of {result}",
                5: f"Difference between {input_number1} and {input_number2} = {result}%"
            }[option]

            wrapped_lines = wrap_text(result_text, _MAX_CHARS_PER_LINE)
            display_wrapped_text(wrapped_lines, x=5, y=30, color=CONFIG.palette[8])

        DISPLAY.show()
        time.sleep_ms(10)

main_loop()

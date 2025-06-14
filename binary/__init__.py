from lib import display, userinput
from lib.hydra import config
import time
from font import vga1_8x16 as font  


_MH_DISPLAY_HEIGHT = const(135)
_MH_DISPLAY_WIDTH = const(240)
_DISPLAY_WIDTH_HALF = const(_MH_DISPLAY_WIDTH // 2)


DISPLAY = display.Display()


CONFIG = config.Config()

INPUT = userinput.UserInput()

def convert_to_binary(number):
    """Convert an integer to its binary representation as a string."""
    return bin(number)[2:]

def convert_to_number(binary_str):
    """Convert a binary string to its integer representation."""
    return int(binary_str, 2)

def main_loop():
    input_number = ""
    result = ""
    display_mode = "menu"  
    conversion_type = None  

    while True:
        keys = INPUT.get_new_keys()

        if keys:
            if display_mode == "menu":
                if "1" in keys:
                    conversion_type = "number_to_binary"
                    display_mode = "input"
                elif "2" in keys:
                    conversion_type = "binary_to_number"
                    display_mode = "input"

            elif display_mode == "input":
                if "ENT" in keys:  
                    if input_number:
                        if conversion_type == "number_to_binary":
                            result = convert_to_binary(int(input_number))
                        elif conversion_type == "binary_to_number":
                            result = str(convert_to_number(input_number))
                        display_mode = "result"
                else:
                    for key in keys:
                        if conversion_type == "number_to_binary":
                            if key.isdigit():
                                input_number += key
                        elif conversion_type == "binary_to_number":
                            if key in ['0', '1']:  
                                input_number += key
                        if key == "BACKSPACE" and len(input_number) > 0:
                            input_number = input_number[:-1]

            elif display_mode == "result":
                if "ENT" in keys:  
                    input_number = ""
                    result = ""
                    display_mode = "menu"

        DISPLAY.fill(CONFIG.palette[2])

        if display_mode == "menu":
            DISPLAY.text(
                text="1. Number to Binary",
                x=5, 
                y=30,
                color=CONFIG.palette[8],
                font=font  
            )
            DISPLAY.text(
                text="2. Binary to Number",
                x=5, 
                y=60,
                color=CONFIG.palette[8],
                font=font  
            )
        elif display_mode == "input":
            if conversion_type == "number_to_binary":
                prompt = "Enter a number: "
            elif conversion_type == "binary_to_number":
                prompt = "Enter binary: "
            DISPLAY.text(
                text=prompt + input_number,
                x=5, 
                y=50,
                color=CONFIG.palette[8],
                font=font  
            )
        elif display_mode == "result":
            if conversion_type == "number_to_binary":
                result_label = "Binary: "
            elif conversion_type == "binary_to_number":
                result_label = "Number: "
            DISPLAY.text(
                text=result_label + result,
                x=5, 
                y=50,
                color=CONFIG.palette[8],
                font=font  
            )

        DISPLAY.show()
        time.sleep_ms(10)

main_loop()

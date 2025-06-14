from lib.display import Display
display = Display()

import time
from lib.userinput import UserInput

WHITE = 0xFFFF
BLACK = 0x0000
HIGHLIGHT_COLOR = 0x07E0  # Green


input_device = UserInput()

plugboard_map = {}
rotor_positions = [0, 0, 0]

rotors_preset = [
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO",
    "ESOVPZJAYQUIRHXLNFTGKDCMWB",
    "VZBRGITYUPSDNHLXAWMJQOFECK"
]

reflectors_preset = [
    "EJMZALYXVBWFCRQUONTSPIKHGD",
    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    "MOWJYPUXNDSRAIBFVLKZGQCHET"
]

preset_plugboard = {
    "Preset I": "AT,BR,DY,EV,FS,IU,KM,LN,OP"
}

MAX_ITEMS_PER_PAGE = 5

def display_text(text):
    """Display text on the screen"""
    display.fill(0)
    display.text(text, 10, 10, WHITE)
    display.show()

def display_menu(title, options, highlight_index):
    """Display menu with highlight centered on the text."""
    display.fill(BLACK)
    display.text(title, 5, 5, WHITE)  
    y_pos = 30  
    box_height = 20  

    for i, option in enumerate(options):
        text_width = len(option) * 8  
        text_height = 8  
        x_text = 5  
        y_text = y_pos + (box_height - text_height) // 2  

        if i == highlight_index:
            display.fill_rect(0, y_pos, display.width, box_height, HIGHLIGHT_COLOR)
            display.text(option, x_text, y_text, BLACK)  
        else:
            display.text(option, x_text, y_pos + (box_height - text_height) // 2, WHITE)  

        y_pos += box_height  

    display.show()

def get_user_selection(title, options):
    """Allow user to select from a menu"""
    index = 0
    while True:
        display_menu(title, options, index)
        keys = input_device.get_new_keys()

        if "DOWN" in keys:
            index = (index + 1) % len(options)
        elif "UP" in keys:
            index = (index - 1) % len(options)
        elif "ENT" in keys:
            return options[index]  
        elif "ESC" in keys:
            return None  

def get_custom_input(prompt):
    """Allow user to enter a custom string"""
    text = ""
    while True:
        display_text(f"{prompt}\n{text}")
        keys = input_device.get_new_keys()
        if keys:
            for key in keys:
                if key == "ENT":
                    return text.upper()
                elif key == "BSPC":
                    text = text[:-1]
                elif key == "SPC":
                    text += " "
                elif len(key) == 1:
                    text += key.upper()
        if "ESC" in keys:
            return None  

def setup_enigma():
    """User selection of settings"""
    global plugboard_map, rotors, reflector

    choice = get_user_selection("Plugboard:", ["Preset I", "Custom"])
    if choice is None:
        return
    elif choice == "Preset I":
        plugboard_settings = preset_plugboard["Preset I"]
    else:
        plugboard_settings = get_custom_input("Enter Plugboard (e.g., AT,BR,DY):")

    plugboard_map = {}
    if plugboard_settings:
        for pair in plugboard_settings.split(","):
            if len(pair) == 2:
                plugboard_map[pair[0]] = pair[1]
                plugboard_map[pair[1]] = pair[0]

    # Rotor 1 Selection
    choice = get_user_selection("Rotor 1:", ["Preset", "Custom"])
    if choice is None:
        return
    elif choice == "Preset":
        rotor_1 = get_user_selection("Choose Rotor 1", rotors_preset)
    else:
        rotor_1 = get_custom_input("Enter Rotor 1:")

    # Rotor 2 Selection
    choice = get_user_selection("Rotor 2:", ["Preset", "Custom"])
    if choice is None:
        return
    elif choice == "Preset":
        rotor_2 = get_user_selection("Choose Rotor 2", rotors_preset)
    else:
        rotor_2 = get_custom_input("Enter Rotor 2:")

    # Rotor 3 Selection
    choice = get_user_selection("Rotor 3:", ["Preset", "Custom"])
    if choice is None:
        return
    elif choice == "Preset":
        rotor_3 = get_user_selection("Choose Rotor 3", rotors_preset)
    else:
        rotor_3 = get_custom_input("Enter Rotor 3:")

    rotors = [rotor_1, rotor_2, rotor_3]

    # Reflector Selection
    choice = get_user_selection("Reflector:", ["Preset", "Custom"])
    if choice is None:
        return
    elif choice == "Preset":
        reflector = get_user_selection("Choose Reflector", reflectors_preset)
    else:
        reflector = get_custom_input("Enter Reflector:")

def encrypt_message(message):
    """Encrypts a full message with debugging"""
    print(f"\nEncrypting Message: {message.upper()}")
    encrypted_text = "".join([encrypt_character(ch) if ch.isalpha() else ch for ch in message])
    print(f"Final Encrypted Output: {encrypted_text}\n")
    return encrypted_text

def step_rotors():
    """Handles rotor stepping logic"""
    global rotor_positions
    rotor_positions[2] = (rotor_positions[2] + 1) % 26
    if rotor_positions[2] == 0:
        rotor_positions[1] = (rotor_positions[1] + 1) % 26
        if rotor_positions[1] == 0:
            rotor_positions[0] = (rotor_positions[0] + 1) % 26
    print(f"Updated Rotor Positions: {rotor_positions}")



def pass_through_rotor(letter, wiring, offset):
    in_index = (ord(letter) - 65 + offset) % 26
    mapped_letter = wiring[in_index]
    mapped_index = (ord(mapped_letter) - 65 - offset + 26) % 26
    return chr(mapped_index + 65)


def pass_backward_through_rotor(letter, wiring, offset):
    """Pass a letter backward through a rotor with correct logic"""
    shifted_index = (ord(letter) - 65 + offset) % 26  # Shift letter forward by rotor offset
    letter_at = chr(shifted_index + 65)  # Find new character after offset shift

    found_index = wiring.index(letter_at)  # Locate this shifted character in the rotor wiring
    final_index = (found_index - offset + 26) % 26  # Reverse the offset to restore position

    return chr(final_index + 65)  # Convert back to A-Z


def reflect_letter(letter):
    """Reflect a letter through the reflector"""
    return reflector[ord(letter) - 65]


def encrypt_character(letter):
    """Encrypts a single character using the Enigma process"""
    step_rotors()  # Step rotors before encryption
    
    if letter in plugboard_map:
        letter = plugboard_map[letter]
    
    # Forward through rotors
    letter = pass_through_rotor(letter, rotors[2], rotor_positions[2])
    letter = pass_through_rotor(letter, rotors[1], rotor_positions[1])
    letter = pass_through_rotor(letter, rotors[0], rotor_positions[0])

    # Reflect
    letter = reflect_letter(letter)

    # Backward through rotors
    letter = pass_backward_through_rotor(letter, rotors[0], rotor_positions[0])
    letter = pass_backward_through_rotor(letter, rotors[1], rotor_positions[1])
    letter = pass_backward_through_rotor(letter, rotors[2], rotor_positions[2])

    if letter in plugboard_map:
        letter = plugboard_map[letter]
    
    return letter


def main():
    """Main function to run the Enigma Machine on the MicroHydra"""
    setup_enigma()  

    display.fill(0)
    display_text("Enigma Ready")
    time.sleep(2)

    message = ""
    while True:
        keys = input_device.get_new_keys()
        if keys:
            for key in keys:
                if key == "ENT":
                    encrypted_text = encrypt_message(message.upper())
                    display_text(encrypted_text)
                    message = ""
                elif key == "BSPC":
                    message = message[:-1]
                    display_text(message)
                elif key == "SPC":
                    message += " "
                    display_text(message)
                elif len(key) == 1:
                    message += key.upper()
                    display_text(message)


main()



# Enigma Machine (Cardputer)

This app is a working simulation of the **Enigma Machine**, created for the **M5Stack Cardputer** using the **MicroHydra** framework. It allows users to configure plugboard settings, rotors, and a reflector to encode or decode messages, just like the historical cipher device.

**[Read the blog post](https://randomboo.com/project/enigma_machine/)**

---

## Features

- **Menu-based navigation** for plugboard, rotors, and reflector setup
- **Rotor stepping mechanism** replicates the original Enigma behavior
- **Plugboard mapping** for extra encryption layers
- **Reflector logic** to mirror signals back through the rotors
- **Real-time input/output** display for live encryption
- Handles both preset and custom rotor/reflector configurations

---

## Encryption Process

1. **Menu Navigation** – Configure plugboard, rotors (3), and a reflector
2. **Plugboard** – Optional letter substitutions before and after encryption
3. **Rotors** – Each letter passes through 3 rotors; positions increment automatically
4. **Reflector** – Sends signals back through rotors, enabling reversible encryption
5. **Encryption** – Output shown as you type, press `ENT` to encrypt the full message

---

## Controls

- `UP` / `DOWN` – Navigate menus  
- `ENT` – Confirm selection or encrypt message  
- `ESC` – Cancel or go back  
- `BSPC` – Delete character  
- `SPC` – Insert space  
- A–Z – Input text (auto-uppercase)

---

## Installation

1. Install **MicroHydra** on your Cardputer.
2. Upload:
   - `__init__.py`
   - Dependencies: `display`, `userinput`
3. Run the script and follow the on-screen prompts to configure and encrypt.

---

## File Overview

- `__init__.py` – Handles full setup, encryption, UI rendering, and rotor logic
- Rotor and reflector presets are hardcoded and selectable in the app

---

## License

MIT License — crack codes, not laws.

# Binary Converter (Cardputer)

This is a simple binary conversion tool for the **M5Stack Cardputer**, built using the **MicroHydra** framework. It lets you convert between decimal numbers and binary strings through an easy-to-use menu interface.

**[Read the blog post](https://randomboo.com/project/binary_conversion_app/)**

---

## Features

- **Number to Binary** conversion
- **Binary to Number** conversion
- **Menu-based interface** to choose mode
- **Input validation** for binary-only digits
- Uses `display`, `userinput`, and `config` modules from MicroHydra

---

## Controls

- `1` – Convert decimal number to binary  
- `2` – Convert binary string to decimal  
- Type input using number keys  
- `ENT` – Perform conversion / continue  
- `BACKSPACE` – Delete last character

---

## Installation

1. Install **MicroHydra** on your Cardputer.
2. Copy app files including:
   - `__init__.py`
   - `font.py` with `vga1_8x16`
   - Dependencies: `display`, `userinput`, `hydra.config`
3. Run the app from your apps menu or directly.

---

## File Overview

- `__init__.py` – Full application logic
- Uses color palettes and display methods from MicroHydra modules

---

## License

MIT License – flip your bits freely.

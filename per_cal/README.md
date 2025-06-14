# Percentage Calculator (Cardputer)

This is a multi-purpose percentage calculator built for the **M5Stack Cardputer** using the **MicroHydra** framework. It helps with common math tasks involving percentages, such as finding percentage values, changes, and differences.

**[Read the blog post](https://randomboo.com/project/percentage-calculator-app/)**

---

## Features

- **Find X% of Y**
- **What % X is of Y**
- **Percentage change from X to Y**
- **X is Y% of what?**
- **Percentage difference between X and Y**
- **Text wrapping** for long results on a small display
- **MicroHydra modular design** using `display`, `userinput`, and `config` modules

---

## Controls

- `1–5` – Select calculation type  
- `ENT` – Submit a number / view result  
- `BSPC` – Delete last digit  
- `CLR` – Clear current input  
- Decimal point supported

---

## Installation

1. Install **MicroHydra** on your Cardputer.
2. Copy app files including:
   - `__init__.py`
   - `font.py` with `vga1_8x16`
   - Required modules: `display`, `userinput`, `hydra.config`
3. Run the app to begin calculating.

---

## File Overview

- `__init__.py` – App logic with wrapped display, number entry, and all calculations
- `font.py` – Font definition for display output
- Uses the standard MicroHydra color palette via `config`

---

## License

MIT License – math is hard, this makes it less so.

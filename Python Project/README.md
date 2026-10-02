# Library Management System

A desktop app built with Python + Tkinter.

## Requirements
- Python 3.8+
- numpy (`pip install numpy`)
- tkinter (usually bundled with Python; on Linux install with `sudo apt install python3-tk` if missing)

## Run it
```
python3 main.py
```

## What's inside
- **Welcome page** → Start/Explore button leads to the main menu.
- **Home** → browse all books, then **Buy** or **Borrow** any title.
  - Buy: enter a quantity. Totals over 1000 EGP get an automatic 20% discount.
    Totals over 500 EGP unlock a bonus guessing game — guess the secret book ID
    correctly (5 tries) to win the book for free.
  - Borrow: enter your name and ID card number, pick 24/48/72 hours, then watch
    a live countdown timer.
- **Add Book** → add a new title to the in-memory catalog (OOP `Book` objects).
- **Best Sellers** → ranks books by copies sold, using NumPy's `argsort`.
- **About** → info about the library's purpose and services.

## File handling
Every purchase and borrow is appended as a line to `sales_records.txt` and
`borrow_records.txt` (created next to `main.py` on first use). The book catalog
itself resets to the default set each time you restart the app, per the
project spec.

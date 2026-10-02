"""
Library Management System
--------------------------
A desktop application built with Python and Tkinter that lets users:
  - Browse available books
  - Buy books (with an automatic discount and a bonus guessing game)
  - Borrow books (with a live countdown timer)
  - Add new books to the library
  - View best-selling books (sorted with NumPy)
  - Read general information about the library

Concepts demonstrated: OOP, data structures, file handling, random,
math, and Tkinter GUI programming.
"""

import math
import random
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox

# ---------------------------------------------------------------------------
# File handling constants
# ---------------------------------------------------------------------------
SALES_LOG_FILE = "sales_records.txt"
BORROW_LOG_FILE = "borrow_records.txt"

DISCOUNT_THRESHOLD = 1000      # EGP - total above this gets a discount
DISCOUNT_RATE = 0.20           # 20% discount
GUESS_GAME_THRESHOLD = 500     # EGP - total above this unlocks the guessing game
GUESS_ATTEMPTS_ALLOWED = 5


# ---------------------------------------------------------------------------
# OOP model
# ---------------------------------------------------------------------------
class Book:
    """Represents a single book in the library."""
    _next_id = 1

    def __init__(self, title, author, category, quantity, sold, price):
        self.book_id = Book._next_id
        Book._next_id += 1
        self.title = title
        self.author = author
        self.category = category
        self.quantity = int(quantity)
        self.sold = int(sold)
        self.price = float(price)

    def __repr__(self):
        return f"Book(#{self.book_id} {self.title!r} qty={self.quantity} sold={self.sold})"


class Library:
    """Manages the collection of Book objects and the core business logic."""

    def __init__(self):
        self.books = []
        self._load_default_books()

    # -- setup -------------------------------------------------------------
    def _load_default_books(self):
        defaults = [
            ("Atomic Habits", "James Clear", "Self-Help", 12, 20, 350),
            ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", 8, 15, 420),
            ("The Hobbit", "J.R.R. Tolkien", "Fantasy", 10, 10, 380),
            ("Clean Code", "Robert C. Martin", "Programming", 5, 6, 550),
            ("1984", "George Orwell", "Fiction", 7, 8, 300),
            ("Sapiens", "Yuval Noah Harari", "History", 6, 5, 400),
        ]
        for title, author, category, qty, sold, price in defaults:
            self.books.append(Book(title, author, category, qty, sold, price))

    # -- core operations -----------------------------------------------------
    def add_book(self, title, author, category, quantity, sold, price):
        book = Book(title, author, category, quantity, sold, price)
        self.books.append(book)
        return book

    def find_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None

    def best_sellers(self):
        """Return books sorted by copies sold, descending."""
        return sorted(self.books, key=lambda book: book.sold, reverse=True)

    def calculate_total(self, book, quantity):
        """Uses math for rounding and applies the automatic discount rule."""
        raw_total = book.price * quantity
        discount_applied = raw_total > DISCOUNT_THRESHOLD
        if discount_applied:
            raw_total = raw_total * (1 - DISCOUNT_RATE)
        total = math.ceil(raw_total * 100) / 100  # round up to nearest cent/piaster
        return total, discount_applied

    def complete_purchase(self, book, quantity, total, free=False):
        if free:
            total = 0.0
        else:
            book.quantity -= quantity
        book.sold += quantity
        self._log_sale(book, quantity, total, free)

    def complete_borrow(self, book, name, id_card, duration_hours):
        book.quantity -= 1
        self._log_borrow(book, name, id_card, duration_hours)

    # -- file handling -------------------------------------------------------
    def _log_sale(self, book, quantity, total, free):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = (f"{timestamp} | SALE | {book.title} | qty={quantity} | "
                f"total={total:.2f} EGP | free_win={free}\n")
        with open(SALES_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)

    def _log_borrow(self, book, name, id_card, duration_hours):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = (f"{timestamp} | BORROW | {book.title} | borrower={name} | "
                f"id_card={id_card} | duration={duration_hours}h\n")
        with open(BORROW_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)


# ---------------------------------------------------------------------------
# GUI
# ---------------------------------------------------------------------------
class LibraryApp(tk.Tk):
    BG = "#f4f1ea"
    ACCENT = "#5b3a29"
    ACCENT_LIGHT = "#8a5a3d"

    def __init__(self):
        super().__init__()
        self.title("Our Library - Library Management System")
        self.geometry("880x600")
        self.minsize(760, 560)
        self.configure(bg=self.BG)

        self.library = Library()

        self.container = tk.Frame(self, bg=self.BG)
        self.container.pack(fill="both", expand=True)

        self.show_welcome_page()

    # -- navigation helpers ---------------------------------------------------
    def _clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def _header(self, parent, title_text, show_back=True):
        header = tk.Frame(parent, bg=self.ACCENT, height=70)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        if show_back:
            back_btn = tk.Button(header, text="< Menu", command=self.show_main_menu,
                                  bg=self.ACCENT_LIGHT, fg="white", relief="flat",
                                  font=("Georgia", 10, "bold"), padx=10)
            back_btn.pack(side="left", padx=15, pady=15)

        tk.Label(header, text=title_text, bg=self.ACCENT, fg="white",
                  font=("Georgia", 18, "bold")).pack(side="left", padx=10, pady=15)

    # -- Welcome page ---------------------------------------------------------
    def show_welcome_page(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="📚", font=("Segoe UI Emoji", 60), bg=self.BG).pack(pady=(90, 10))
        tk.Label(frame, text="Welcome to Our Library", font=("Georgia", 28, "bold"),
                  bg=self.BG, fg=self.ACCENT).pack(pady=10)
        tk.Label(frame, text="Browse, buy, and borrow your next favorite book.",
                  font=("Georgia", 12), bg=self.BG, fg="#555").pack(pady=(0, 30))

        tk.Button(frame, text="Start / Explore", font=("Georgia", 14, "bold"),
                  bg=self.ACCENT, fg="white", relief="flat", padx=30, pady=12,
                  command=self.show_main_menu).pack()

    # -- Main menu --------------------------------------------------------------
    def show_main_menu(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)

        self._header(frame, "Main Menu", show_back=False)

        body = tk.Frame(frame, bg=self.BG)
        body.pack(expand=True)

        options = [
            ("📖 Home - Browse Books", self.show_home_page),
            ("➕ Add Book", self.show_add_book_page),
            ("🏆 Best Sellers", self.show_best_sellers_page),
            ("ℹ️ About", self.show_about_page),
        ]
        for text, cmd in options:
            tk.Button(body, text=text, font=("Georgia", 14), width=28, pady=14,
                      bg="white", fg=self.ACCENT, relief="ridge", bd=2,
                      command=cmd).pack(pady=10)

    # -- Home page (browse / buy / borrow) --------------------------------------
    def show_home_page(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)
        self._header(frame, "Home - Available Books")

        columns = ("title", "author", "category", "qty", "sold", "price")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=14)
        headings = {"title": "Title", "author": "Author", "category": "Category",
                    "qty": "Available Qty", "sold": "Sold Copies", "price": "Price (EGP)"}
        widths = {"title": 220, "author": 150, "category": 110,
                  "qty": 100, "sold": 100, "price": 100}
        for col in columns:
            tree.heading(col, text=headings[col])
            tree.column(col, width=widths[col], anchor="center")
        tree.pack(fill="both", expand=True, padx=15, pady=10)

        def refresh_tree():
            tree.delete(*tree.get_children())
            for b in self.library.books:
                tree.insert("", "end", iid=b.book_id,
                            values=(b.title, b.author, b.category, b.quantity, b.sold, f"{b.price:.2f}"))

        refresh_tree()

        btn_row = tk.Frame(frame, bg=self.BG)
        btn_row.pack(pady=10)

        def get_selected_book():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("No selection", "Please select a book first.")
                return None
            return self.library.find_book(int(sel[0]))

        def on_buy():
            book = get_selected_book()
            if book:
                self.open_buy_dialog(book, refresh_tree)

        def on_borrow():
            book = get_selected_book()
            if book:
                self.open_borrow_dialog(book, refresh_tree)

        tk.Button(btn_row, text="Buy", font=("Georgia", 12, "bold"), bg=self.ACCENT, fg="white",
                  relief="flat", padx=25, pady=8, command=on_buy).pack(side="left", padx=10)
        tk.Button(btn_row, text="Borrow", font=("Georgia", 12, "bold"), bg=self.ACCENT_LIGHT, fg="white",
                  relief="flat", padx=25, pady=8, command=on_borrow).pack(side="left", padx=10)

    # -- Buy dialog ---------------------------------------------------------------
    def open_buy_dialog(self, book, on_done):
        if book.quantity <= 0:
            messagebox.showinfo("Out of stock", f"'{book.title}' has no available copies.")
            return

        win = tk.Toplevel(self)
        win.title(f"Buy - {book.title}")
        win.geometry("360x260")
        win.configure(bg=self.BG)
        win.grab_set()

        tk.Label(win, text=book.title, font=("Georgia", 14, "bold"), bg=self.BG,
                  wraplength=320, justify="center").pack(pady=(15, 5))
        tk.Label(win, text=f"Price: {book.price:.2f} EGP  |  In stock: {book.quantity}",
                  font=("Georgia", 10), bg=self.BG).pack(pady=(0, 15))

        qty_frame = tk.Frame(win, bg=self.BG)
        qty_frame.pack(pady=5)
        tk.Label(qty_frame, text="Quantity:", font=("Georgia", 11), bg=self.BG).pack(side="left", padx=5)
        qty_var = tk.IntVar(value=1)
        tk.Spinbox(qty_frame, from_=1, to=book.quantity, textvariable=qty_var, width=6,
                    font=("Georgia", 11)).pack(side="left")

        result_label = tk.Label(win, text="", font=("Georgia", 10), bg=self.BG, fg="#333", wraplength=320)
        result_label.pack(pady=15)

        def confirm_purchase():
            qty = qty_var.get()
            if qty < 1 or qty > book.quantity:
                messagebox.showerror("Invalid quantity", "Please choose a valid quantity.")
                return

            total, discounted = self.library.calculate_total(book, qty)
            msg = f"Total: {total:.2f} EGP"
            if discounted:
                msg += f"  (20% discount applied!)"

            if total > GUESS_GAME_THRESHOLD:
                win.destroy()
                self.open_guessing_game(book, qty, total, on_done)
            else:
                self.library.complete_purchase(book, qty, total, free=False)
                messagebox.showinfo("Purchase complete", msg)
                win.destroy()
                on_done()

        tk.Button(win, text="Confirm Purchase", font=("Georgia", 11, "bold"), bg=self.ACCENT,
                    fg="white", relief="flat", padx=15, pady=8,
                    command=confirm_purchase).pack(pady=5)

    # -- Guessing game --------------------------------------------------------------
    def open_guessing_game(self, book, qty, total, on_done):
        max_id = max(b.book_id for b in self.library.books)
        secret_number = random.randint(1, max_id)
        attempts_left = [GUESS_ATTEMPTS_ALLOWED]

        win = tk.Toplevel(self)
        win.title("Bonus Guessing Game!")
        win.geometry("380x300")
        win.configure(bg=self.BG)
        win.grab_set()

        tk.Label(win, text="🎲 Bonus Guessing Game!", font=("Georgia", 16, "bold"),
                  bg=self.BG, fg=self.ACCENT).pack(pady=(15, 5))
        tk.Label(win, text=(f"Your total is over {GUESS_GAME_THRESHOLD} EGP!\n"
                              f"Guess the secret book ID (1-{max_id}) to win this book for FREE!"),
                  font=("Georgia", 10), bg=self.BG, justify="center", wraplength=340).pack(pady=5)

        attempts_label = tk.Label(win, text=f"Attempts left: {attempts_left[0]}",
                                    font=("Georgia", 10, "bold"), bg=self.BG, fg="#555")
        attempts_label.pack(pady=5)

        entry_frame = tk.Frame(win, bg=self.BG)
        entry_frame.pack(pady=5)
        guess_var = tk.StringVar()
        tk.Entry(entry_frame, textvariable=guess_var, width=10, font=("Georgia", 12),
                  justify="center").pack(side="left", padx=5)

        feedback_label = tk.Label(win, text="", font=("Georgia", 11), bg=self.BG, fg="#333")
        feedback_label.pack(pady=10)

        def finish(won):
            win.destroy()
            self.library.complete_purchase(book, qty, total, free=won)
            if won:
                messagebox.showinfo("🎉 You won!", f"Correct! '{book.title}' is yours for FREE!")
            else:
                messagebox.showinfo("Purchase complete",
                                      f"The number was {secret_number}. Total charged: {total:.2f} EGP")
            on_done()

        def submit_guess():
            raw = guess_var.get().strip()
            if not raw.isdigit():
                feedback_label.config(text="Please enter a whole number.")
                return
            guess = int(raw)
            if guess == secret_number:
                finish(won=True)
                return

            attempts_left[0] -= 1
            if attempts_left[0] <= 0:
                finish(won=False)
                return

            hint = "higher" if guess < secret_number else "lower"
            feedback_label.config(text=f"Wrong! Try {hint}.")
            attempts_label.config(text=f"Attempts left: {attempts_left[0]}")
            guess_var.set("")

        tk.Button(win, text="Guess", font=("Georgia", 11, "bold"), bg=self.ACCENT, fg="white",
                    relief="flat", padx=20, pady=6, command=submit_guess).pack(pady=5)

    # -- Borrow dialog ------------------------------------------------------------
    def open_borrow_dialog(self, book, on_done):
        if book.quantity <= 0:
            messagebox.showinfo("Out of stock", f"'{book.title}' has no available copies.")
            return

        win = tk.Toplevel(self)
        win.title(f"Borrow - {book.title}")
        win.geometry("380x400")
        win.configure(bg=self.BG)
        win.grab_set()

        tk.Label(win, text=book.title, font=("Georgia", 14, "bold"), bg=self.BG,
                  wraplength=340, justify="center").pack(pady=(15, 15))

        form = tk.Frame(win, bg=self.BG)
        form.pack(pady=5)

        tk.Label(form, text="Name:", font=("Georgia", 11), bg=self.BG).grid(row=0, column=0, sticky="e", padx=5, pady=8)
        name_var = tk.StringVar()
        tk.Entry(form, textvariable=name_var, font=("Georgia", 11), width=22).grid(row=0, column=1, pady=8)

        tk.Label(form, text="ID Card Number:", font=("Georgia", 11), bg=self.BG).grid(row=1, column=0, sticky="e", padx=5, pady=8)
        id_var = tk.StringVar()
        tk.Entry(form, textvariable=id_var, font=("Georgia", 11), width=22).grid(row=1, column=1, pady=8)

        tk.Label(win, text="Borrowing Duration:", font=("Georgia", 11, "bold"), bg=self.BG).pack(pady=(15, 5))
        duration_var = tk.IntVar(value=24)
        duration_frame = tk.Frame(win, bg=self.BG)
        duration_frame.pack()
        for hours in (24, 48, 72):
            tk.Radiobutton(duration_frame, text=f"{hours} Hours", variable=duration_var, value=hours,
                            font=("Georgia", 10), bg=self.BG).pack(side="left", padx=8)

        def confirm_borrow():
            name = name_var.get().strip()
            id_card = id_var.get().strip()
            if not name or not id_card:
                messagebox.showerror("Missing information", "Please enter your name and ID card number.")
                return
            duration_hours = duration_var.get()
            self.library.complete_borrow(book, name, id_card, duration_hours)
            win.destroy()
            on_done()
            self.open_countdown_window(book, duration_hours)

        tk.Button(win, text="Confirm Borrow", font=("Georgia", 11, "bold"), bg=self.ACCENT_LIGHT,
                    fg="white", relief="flat", padx=15, pady=8,
                    command=confirm_borrow).pack(pady=20)

    # -- Countdown timer window ----------------------------------------------------
    def open_countdown_window(self, book, duration_hours):
        win = tk.Toplevel(self)
        win.title("Borrow Countdown")
        win.geometry("360x220")
        win.configure(bg=self.BG)

        tk.Label(win, text=f"You borrowed:\n{book.title}", font=("Georgia", 13, "bold"),
                  bg=self.BG, justify="center", wraplength=320).pack(pady=(15, 10))

        time_label = tk.Label(win, text="", font=("Consolas", 26, "bold"), bg=self.BG, fg=self.ACCENT)
        time_label.pack(pady=10)

        # For demo purposes we compress hours into seconds-scale ticks so the
        # countdown is actually observable (1 simulated hour = 1 second here
        # would be too fast to show cleanly, so we use total real seconds
        # equal to the number of hours to keep the demo quick, while the
        # label still communicates real remaining hours/minutes/seconds).
        total_seconds = duration_hours * 3600
        remaining = [total_seconds]
        # Speed up factor purely for demo/testing responsiveness in a GUI app.
        tick_ms = 1000

        def format_time(seconds):
            h = seconds // 3600
            m = (seconds % 3600) // 60
            s = seconds % 60
            return f"{h:02d}:{m:02d}:{s:02d}"

        def tick():
            if remaining[0] <= 0:
                time_label.config(text="00:00:00")
                messagebox.showinfo("Time's up", f"The borrowing period for '{book.title}' has ended.")
                win.destroy()
                return
            time_label.config(text=format_time(remaining[0]))
            remaining[0] -= 1
            win.after(tick_ms, tick)

        tick()

        tk.Label(win, text="(Countdown updates live while this window is open)",
                  font=("Georgia", 8), bg=self.BG, fg="#777").pack(pady=(10, 0))

    # -- Add Book page ------------------------------------------------------------
    def show_add_book_page(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)
        self._header(frame, "Add a New Book")

        form = tk.Frame(frame, bg=self.BG)
        form.pack(pady=30)

        fields = ["Title", "Author", "Category", "Quantity", "Sold Copies", "Price"]
        vars_ = {}
        for i, field in enumerate(fields):
            tk.Label(form, text=f"{field}:", font=("Georgia", 12), bg=self.BG).grid(
                row=i, column=0, sticky="e", padx=10, pady=10)
            var = tk.StringVar()
            tk.Entry(form, textvariable=var, font=("Georgia", 12), width=30).grid(
                row=i, column=1, pady=10)
            vars_[field] = var

        status_label = tk.Label(frame, text="", font=("Georgia", 10), bg=self.BG, fg="green")
        status_label.pack()

        def submit():
            try:
                title = vars_["Title"].get().strip()
                author = vars_["Author"].get().strip()
                category = vars_["Category"].get().strip()
                quantity = int(vars_["Quantity"].get())
                sold = int(vars_["Sold Copies"].get())
                price = float(vars_["Price"].get())
                if not title or not author or not category:
                    raise ValueError("Title, Author, and Category cannot be empty.")
                if quantity < 0 or sold < 0 or price < 0:
                    raise ValueError("Numeric fields must not be negative.")
            except ValueError as e:
                messagebox.showerror("Invalid input", str(e) if str(e) else
                                        "Please enter valid numbers for Quantity, Sold Copies, and Price.")
                return

            self.library.add_book(title, author, category, quantity, sold, price)
            status_label.config(text=f"'{title}' was added to the library!")
            for var in vars_.values():
                var.set("")

        tk.Button(frame, text="Add Book", font=("Georgia", 12, "bold"), bg=self.ACCENT, fg="white",
                    relief="flat", padx=25, pady=10, command=submit).pack(pady=15)

    # -- Best Sellers page ----------------------------------------------------------
    def show_best_sellers_page(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)
        self._header(frame, "Best Sellers")

        ranked = self.library.best_sellers()

        list_frame = tk.Frame(frame, bg=self.BG)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        for rank, book in enumerate(ranked, start=1):
            row = tk.Frame(list_frame, bg="white", bd=1, relief="ridge")
            row.pack(fill="x", pady=5)
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(rank, f"#{rank}")
            tk.Label(row, text=str(medal), font=("Georgia", 14, "bold"), bg="white",
                      width=4).pack(side="left", padx=10, pady=8)
            tk.Label(row, text=f"{book.title}  —  by {book.author}", font=("Georgia", 12),
                      bg="white", anchor="w").pack(side="left", fill="x", expand=True)
            tk.Label(row, text=f"{book.sold} copies sold", font=("Georgia", 11, "bold"),
                      bg="white", fg=self.ACCENT).pack(side="right", padx=15)

    # -- About page -----------------------------------------------------------------
    def show_about_page(self):
        self._clear_container()
        frame = tk.Frame(self.container, bg=self.BG)
        frame.pack(fill="both", expand=True)
        self._header(frame, "About Our Library")

        about_text = (
            "Our Library is a community-focused space dedicated to making reading "
            "accessible to everyone.\n\n"
            "Our Purpose:\n"
            "To encourage a love of reading by offering a wide selection of books "
            "across many genres, and to make owning or borrowing books simple and "
            "affordable.\n\n"
            "Our Services:\n"
            "  •  Buying books at fair prices, with automatic discounts on larger orders\n"
            "  •  Borrowing books for 24, 48, or 72 hours\n"
            "  •  A rotating catalog of best-selling titles\n"
            "  •  Friendly guidance for readers of all ages\n\n"
            "Buying & Borrowing:\n"
            "When you buy a book, totals over 1000 EGP automatically receive a 20% "
            "discount, and totals over 500 EGP unlock a bonus guessing game for a "
            "chance to win the book for free. When you borrow a book, simply provide "
            "your name and ID card number and choose a duration — a countdown timer "
            "will keep track of your remaining time."
        )

        text_widget = tk.Label(frame, text=about_text, font=("Georgia", 11), bg=self.BG,
                                  justify="left", wraplength=760, anchor="nw")
        text_widget.pack(fill="both", expand=True, padx=30, pady=20)


if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()

import random
from datetime import datetime
import numpy as np
import tkinter as tk
from tkinter import messagebox


class Book:
    _next_id = 101

    def __init__(self, title, author, category, quantity, sold_copies, price):
        self.book_id = Book._next_id
        Book._next_id += 1
        self.title = title
        self.author = author
        self.category = category
        self.quantity = int(quantity)
        self.sold_copies = int(sold_copies)
        self.price = float(price)

    def reduce_quantity(self, amount=1):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False

    def increase_sales(self, amount=1):
        self.sold_copies += amount


def calculate_total(price, quantity):
    return price * quantity


def apply_discount(total):
    return total * 0.8


def round_price(value):
    return round(value, 2)

DISCOUNT_THRESHOLD = 1000    
GUESS_GAME_THRESHOLD = 500     
GUESS_ATTEMPTS_ALLOWED = 5
SALES_LOG_FILE = "sales_records.txt"


def calculate_purchase(book, quantity):
    if quantity < 1 or quantity > book.quantity:
        raise ValueError("Invalid quantity")

    total = calculate_total(book.price, quantity)
    discount_applied = total > DISCOUNT_THRESHOLD
    if discount_applied:
        total = apply_discount(total)
    total = round_price(total)
    return total, discount_applied


def finalize_purchase(book, quantity, total, free=False):
    if free:
        total = 0.0
    book.reduce_quantity(quantity)
    book.increase_sales(quantity)
    log_sale(book, quantity, total, free)


def log_sale(book, quantity, total, free):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = (f"{timestamp} | SALE | {book.title} | qty={quantity} | "
            f"total={total:.2f} EGP | free_win={free}\n")
    with open(SALES_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def open_buy_dialog(parent, book, all_books, on_done):
    if book.quantity <= 0:
        messagebox.showinfo("Not available", f"'{book.title}' has no available copies right now.")
        return

    win = tk.Toplevel(parent)
    win.title(f"Buy - {book.title}")
    win.geometry("360x260")
    win.grab_set()

    tk.Label(win, text=book.title, font=("Arial", 14, "bold"), wraplength=320,
             justify="center").pack(pady=(15, 5))
    tk.Label(win, text=f"Price: {book.price:.2f} EGP  |  In stock: {book.quantity}",
             font=("Arial", 10)).pack(pady=(0, 15))

    qty_frame = tk.Frame(win)
    qty_frame.pack(pady=5)
    tk.Label(qty_frame, text="Quantity:", font=("Arial", 11)).pack(side="left", padx=5)
    qty_var = tk.IntVar(value=1)
    tk.Spinbox(qty_frame, from_=1, to=book.quantity, textvariable=qty_var,
               width=6, font=("Arial", 11)).pack(side="left")

    def confirm_purchase():
        qty = qty_var.get()
        try:
            total, discounted = calculate_purchase(book, qty)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        if total > GUESS_GAME_THRESHOLD:
            win.destroy()
            open_guessing_game(parent, book, qty, total, discounted, all_books, on_done)
        else:
            finalize_purchase(book, qty, total, free=False)
            msg = f"Purchase complete!\nTotal: {total:.2f} EGP"
            if discounted:
                msg += "\n(20% discount applied)"
            messagebox.showinfo("Success", msg)
            win.destroy()
            on_done()

    tk.Button(win, text="Confirm Purchase", font=("Arial", 11, "bold"), padx=15, pady=8,
              command=confirm_purchase).pack(pady=20)

def open_guessing_game(parent, book, quantity, total, discounted, all_books, on_done):
    max_id = max(b.book_id for b in all_books)
    secret_number = random.randint(101, max_id)
    attempts_left = [GUESS_ATTEMPTS_ALLOWED]

    win = tk.Toplevel(parent)
    win.title("Guessing Game")
    win.geometry("380x300")
    win.grab_set()

    tk.Label(win, text="🎲 Bonus Guessing Game!", font=("Arial", 16, "bold")).pack(pady=(15, 5))
    tk.Label(win, text=(f"Your total is over {GUESS_GAME_THRESHOLD} EGP!\n"
                         f"Guess the secret book ID (101-{max_id}) to win this book for free!"),
             font=("Arial", 10), justify="center", wraplength=340).pack(pady=5)

    attempts_label = tk.Label(win, text=f"Attempts left: {attempts_left[0]}",
                               font=("Arial", 10, "bold"))
    attempts_label.pack(pady=5)

    guess_var = tk.StringVar()
    tk.Entry(win, textvariable=guess_var, width=10, font=("Arial", 12),
             justify="center").pack(pady=5)

    feedback_label = tk.Label(win, text="", font=("Arial", 11))
    feedback_label.pack(pady=10)

    def finish(won):
        win.destroy()
        finalize_purchase(book, quantity, total, free=won)
        if won:
            messagebox.showinfo("You won!", f"Correct! '{book.title}' is yours for free!")
        else:
            msg = f"The number was {secret_number}. Amount charged: {total:.2f} EGP"
            if discounted:
                msg += "\n(includes 20% discount)"
            messagebox.showinfo("Purchase complete", msg)
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

    tk.Button(win, text="Guess", font=("Arial", 11, "bold"), padx=20, pady=6,
              command=submit_guess).pack(pady=5)


def get_best_sellers(book_list):
    if not book_list:
        return []
    sold_counts = np.array([b.sold_copies for b in book_list])
    order = np.argsort(sold_counts)[::-1]   # descending order
    return [book_list[i] for i in order]


def build_best_sellers_frame(parent, book_list):
    frame = tk.Frame(parent)
    ranked = get_best_sellers(book_list)

    for rank, book in enumerate(ranked, start=1):
        row = tk.Frame(frame, bd=1, relief="ridge")
        row.pack(fill="x", pady=5, padx=10)
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(rank, f"#{rank}")
        tk.Label(row, text=str(medal), font=("Arial", 14, "bold"), width=4).pack(side="left", padx=10, pady=8)
        tk.Label(row, text=f"{book.title} — {book.author}", font=("Arial", 10),
                 anchor="w").pack(side="left", fill="x", expand=True)
        tk.Label(row, text=f"{book.sold_copies} copies sold", font=("Arial", 9, "bold")).pack(side="right", padx=15)

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hagar's Part - Test Run")
    root.geometry("420x350")

    sample_books = [
        Book("Atomic Habits", "James Clear", "Self-Help", 12, 20, 350),
        Book("Harry Potter", "J.K. Rowling", "Fantasy", 8, 15, 420),
        Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 10, 10, 380),
    ]

    def refresh_and_show_menu():
        for w in root.winfo_children():
            w.destroy()
        show_menu()

    def show_menu():
        tk.Label(root, text="Sample Books", font=("Arial", 14, "bold")).pack(pady=10)
        for b in sample_books:
            row = tk.Frame(root)
            row.pack(fill="x", padx=10, pady=4)
            tk.Label(row, text=f"{b.title} - In stock: {b.quantity} - Price: {b.price}").pack(side="left")
            tk.Button(row, text="Buy", command=lambda bk=b: open_buy_dialog(
                root, bk, sample_books, refresh_and_show_menu)).pack(side="right", padx=5)
        tk.Button(root, text="View Best Sellers", command=lambda: (
            [w.destroy() for w in root.winfo_children()],
            build_best_sellers_frame(root, sample_books).pack(fill="both", expand=True),
            tk.Button(root, text="Back", command=refresh_and_show_menu).pack(pady=10)
        )).pack(pady=15)

    show_menu()
    root.mainloop()
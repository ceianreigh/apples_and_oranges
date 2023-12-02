# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output

import tkinter as tk
from tkinter import PhotoImage, messagebox


# calculating the number of apple user can buy and their remaining money
def calculate(money_entry, apple_price_entry):
    # function to show an error if money or apple_price is blank or not a number
    try:
        money = float(money_entry.get())
        apple_price = float(apple_price_entry.get())
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid AMOUNT of your money and PRICE of apple.",
        )
        return

    # calculate the number of apple and remaining money
    num_apples = int(money // apple_price)
    remaining_money = money % apple_price

    # display receipt
    messagebox.showinfo(
        "Receipt",
        f"Thank you for your purchase!\n\n Your money: {money}\n Price of Apple: {apple_price}\n\n Number of Apples You Can Buy: {num_apples}\n Your remaining money: {remaining_money}",
    )
    window.destroy()


# function to start transaction
def start_order(background_image):
    order_window = tk.Toplevel()
    order_window.title("Apple Store")
    order_window.geometry("500x300")
    background_label = tk.Label(order_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # title
    buy = tk.Label(
        order_window,
        text="The Apple Store",
        font=("Georgia Bold", 40),
        fg="#DDF7E3",
        bg="#DF2E38",
    )
    buy.pack(pady=30)

    # money
    money_frame = tk.Frame(order_window, bg="#DF2E38")
    money_frame.pack(side=tk.LEFT, padx=40, pady=10)

    money_icon_label = tk.Label(
        money_frame,
        text="💰",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#5D9C59",
    )
    money_icon_label.pack(side=tk.TOP)
    money_label = tk.Label(
        money_frame,
        text="Your Money:",
        font=("Garamond", 16),
        fg="#FFFFFF",
        bg="#DF2E38",
    )
    money_label.pack(side=tk.TOP)
    money_entry = tk.Entry(money_frame)
    money_entry.pack(side=tk.TOP)

    # apple price
    apples_frame = tk.Frame(order_window, bg="#5D9C59")
    apples_frame.pack(side=tk.RIGHT, padx=40, pady=10)

    apple_icon_label = tk.Label(
        apples_frame,
        text="🍎",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#DF2E38",
    )
    apple_icon_label.pack(side=tk.TOP)
    apple_price_label = tk.Label(
        apples_frame,
        text="Price of Apple:",
        font=("Garamond", 16),
        fg="#FFFFFF",
        bg="#5D9C59",
    )
    apple_price_label.pack(side=tk.TOP)
    apple_price_entry = tk.Entry(apples_frame)
    apple_price_entry.pack(side=tk.TOP)

    # order button
    order_button = tk.Button(
        order_window,
        text="Check Out",
        font=("Verdana Bold", 11),
        fg="#FFFFFF",
        bg="#DF2E38",
        command=lambda: calculate(money_entry, apple_price_entry),
    )
    order_button.pack(side=tk.BOTTOM, pady=5)


def cancel_order():
    window.destroy()


window = tk.Tk()
window.title("Apple Store")
window.geometry("500x300")
background_image = PhotoImage(file=r"D:\Downloads\apple_bg.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# heading
heading = tk.Label(
    window,
    text="The Apple Store",
    font=("Georgia Bold", 40),
    fg="#DDF7E3",
    bg="#DF2E38",
)
heading.pack(pady=10)

# subheading
subheading = tk.Label(
    window,
    text="The Fruits, Not the Phone",
    font=("Verdana Bold Italic", 16),
    fg="#DF2E38",
    bg="#DDF7E3",
)
subheading.pack()

# start_button
start_button = tk.Button(
    window,
    text="🛒 Buy Now",
    font=("Georgia", 14),
    fg="#DDF7E3",
    bg="#5D9C59",
    command=lambda: start_order(background_image),
)
start_button.pack(side=tk.LEFT, padx=60)

# cancel_button
cancel_button = tk.Button(
    window,
    text="❌ Buy Later",
    font=("Georgia", 14),
    fg="#DDF7E3",
    bg="#5D9C59",
    command=cancel_order,
)
cancel_button.pack(side=tk.RIGHT, padx=60)

window.mainloop()

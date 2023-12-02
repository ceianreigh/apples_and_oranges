# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output

import tkinter as tk
from tkinter import PhotoImage, messagebox


# function to get the address
def get_address(apples_entry, oranges_entry, background_image):
    # function to show error if the user entered invalid number of apples and oranges
    try:
        num_apples = int(apples_entry.get())
        num_oranges = int(oranges_entry.get())
    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid NUMBERS of apples and oranges.",
        )
        return

    # contact information
    contact_window = tk.Toplevel()
    contact_window.title("Get Contact Information")
    contact_window.geometry("500x300")
    background_label = tk.Label(contact_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    orders = tk.Label(
        contact_window,
        text="Fruites Options",
        font=("Cooper Black", 40),
        fg="#028A0F",
        bg="#E9E186",
    )
    orders.pack(pady=10)

    # address
    address_frame = tk.Frame(contact_window, bg="#00B7BD")
    address_frame.pack(side=tk.LEFT, padx=40, pady=20)

    address_icon_label = tk.Label(
        address_frame,
        text="🏡",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#00B7BD",
    )
    address_icon_label.pack(side=tk.TOP)

    address = tk.Label(
        address_frame,
        text="Address",
        font=("Arial Bold Italic", 12),
        fg="#FFFFFF",
        bg="#00B7BD",
    )
    address.pack(side=tk.TOP)
    address_entry = tk.Entry(address_frame)
    address_entry.pack(side=tk.TOP)

    # phone number
    phone_frame = tk.Frame(contact_window, bg="#00B7BD")
    phone_frame.pack(side=tk.RIGHT, padx=40, pady=20)

    phone_icon_label = tk.Label(
        phone_frame,
        text="📞",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#00B7BD",
    )
    phone_icon_label.pack(side=tk.TOP)
    phone_label = tk.Label(
        phone_frame,
        text="Phone Number",
        font=("Arial Bold Italic", 12),
        fg="#FFFFFF",
        bg="#00B7BD",
    )
    phone_label.pack(side=tk.TOP)
    phone_entry = tk.Entry(phone_frame)
    phone_entry.pack(side=tk.TOP)

    # function to show error if the user entered no address or phone number
    def submit_orders_wrapper():
        if not address_entry.get():
            messagebox.showerror(
                "Input Error",
                "Please enter your address to where we can deliver your order.",
            )
        elif not phone_entry.get():
            messagebox.showerror(
                "Input Error",
                "Please enter your phone number for easy transaction on delivery day.",
            )
        else:
            submit_orders(num_apples, num_oranges, address_entry, phone_entry)

    # done order
    done_button = tk.Button(
        contact_window,
        text="Check Out",
        font=("Arial Narrow Bold", 11),
        fg="#FFFFFF",
        bg="#F68D2E",
        command=submit_orders_wrapper,
    )
    done_button.pack(side=tk.BOTTOM, pady=5)


# function to calculate and show receipt
def submit_orders(num_apples, num_oranges, address_entry, phone_entry):
    apple_price = 20
    orange_price = 25

    total_number = num_apples + num_oranges
    total_amount = (num_apples * apple_price) + (num_oranges * orange_price)

    address = address_entry.get()
    phone = phone_entry.get()

    if total_number <= 10:
        messagebox.showinfo(
            "Receipt",
            f"Amount to Pay: {total_amount} pesos\n\n Number of Apples: {num_apples}\n Number of Oranges: {num_oranges}\n Address: {address}\n Phone Number: {phone}\n\n Please expect delivery within the day.",
        )
        window.destroy()
    elif 10 < total_number <= 30:
        messagebox.showinfo(
            "Receipt",
            f"Amount to Pay: {total_amount} pesos\n\n Number of Apples: {num_apples}\n Number of Oranges: {num_oranges}\n Address: {address}\n Phone Number: {phone}\n\n Please expect delivery after one day.",
        )
        window.destroy()
    elif total_number > 30:
        messagebox.showinfo(
            "Receipt",
            f"Amount to Pay: {total_amount} pesos\n\n Number of Apples: {num_apples}\n Number of Oranges: {num_oranges}\n\n Address: {address}\n Phone Number: {phone}\n\n Please expect delivery after two days.",
        )
        window.destroy()


# function to start the transaction
def start_order(background_image):
    order_window = tk.Toplevel()
    order_window.title("Start Order")
    order_window.geometry("500x300")
    background_label = tk.Label(order_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # title
    orders = tk.Label(
        order_window,
        text="Fruites Options",
        font=("Cooper Black", 40),
        fg="#028A0F",
        bg="#E9E186",
    )
    orders.pack(pady=10)

    # apple
    apples_frame = tk.Frame(order_window, bg="#B7DD79")
    apples_frame.pack(side=tk.LEFT, padx=20, pady=20)

    apple_icon_label = tk.Label(
        apples_frame,
        text="🍎",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#F65275",
    )
    apple_icon_label.pack(side=tk.TOP)
    apples_label = tk.Label(
        apples_frame,
        text="Number of Apples\n Price: 20",
        font=("Arial Bold Italic", 12),
        bg="#B7DD79",
    )
    apples_label.pack(side=tk.TOP)
    apples_entry = tk.Entry(apples_frame)
    apples_entry.pack(side=tk.TOP)

    # orange
    oranges_frame = tk.Frame(order_window, bg="#B7DD79")
    oranges_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    orange_icon_label = tk.Label(
        oranges_frame,
        text="🍊",
        font=("Arial", 50),
        fg="#FFFFFF",
        bg="#F68D2E",
    )
    orange_icon_label.pack(side=tk.TOP)
    oranges_label = tk.Label(
        oranges_frame,
        text="Number of Oranges\n Price: 25",
        font=("Arial Bold Italic", 12),
        bg="#B7DD79",
    )
    oranges_label.pack(side=tk.TOP)
    oranges_entry = tk.Entry(oranges_frame)
    oranges_entry.pack(side=tk.TOP)

    # order button
    order_button = tk.Button(
        order_window,
        text="Add to Cart",
        font=("Arial Narrow Bold", 11),
        fg="#FFFFFF",
        bg="#F68D2E",
        command=lambda: get_address(apples_entry, oranges_entry, background_image),
    )
    order_button.pack(side=tk.BOTTOM, pady=5)


def cancel_order():
    window.destroy()


window = tk.Tk()
window.title("Fruites Options")
window.geometry("500x300")
background_image = PhotoImage(file="D:\Downloads\PLD BG.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# heading
heading = tk.Label(
    window,
    text="Fruites Options",
    font=("Cooper Black", 40),
    fg="#028A0F",
    bg="#E9E186",
)
heading.pack(pady=20)

# subheading
subheading = tk.Label(
    window,
    text="Your One-Call-Away Fruit Store",
    font=("Arial Narrow Bold Italic", 16),
    fg="#E9E186",
    bg="#028A0F",
)
subheading.pack()

# start_button
start_button = tk.Button(
    window,
    text="🛒 Buy Now",
    font=("Rockwell", 14),
    fg="#FFFFFF",
    bg="#F68D2E",
    command=lambda: start_order(background_image),
)
start_button.pack(side=tk.LEFT, padx=60)

# cancel_button
cancel_button = tk.Button(
    window,
    text="❌ Buy Later",
    font=("Rockwell", 14),
    fg="#FFFFFF",
    bg="#F68D2E",
    command=cancel_order,
)
cancel_button.pack(side=tk.RIGHT, padx=60)

window.mainloop()

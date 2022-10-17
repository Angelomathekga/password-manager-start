import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    new_password = "".join(password_list)
    pass_entry.delete(0, "end")

    pass_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# function that gets the 3 entry fields and saves them to a text

def add():
    web = web_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_data = {web: {
        "email": email,
        "password": password}
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please dont leave any of the fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except :
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)


        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    with open("data.json", mode="r") as data_file:
        data = json.load(data_file)

    try:
        web_dict = data[website]

    except KeyError:
        messagebox.showinfo(title="Error", message="Oops, no information exists for this website!")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found!")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Your Details for this website are:\n"
                                                        f"Email: {web_dict['email']}\n"
                                                        f"Password: {web_dict['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_entry = Entry(width=33)
web_entry.focus()
web_entry.grid(column=1, row=1, sticky="W")

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, sticky="W")

user_entry = Entry(width=51)
user_entry.insert(0, "angelomathekga@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky="W")

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="W")

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

window.mainloop()

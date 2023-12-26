from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pwd_input.delete(0,END)
    pwd_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    w = website_input.get()
    e = email_input.get()
    p = pwd_input.get()

    if len(w)==0 or len(p)==0:
        messagebox.showinfo(title="oops", message="please fill up all fields")
    else:
        is_ok = messagebox.askokcancel(title=w, message=f"email: {e}\npassword: {p}\nis it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as save_file:
                save_file.write(f"{w} | {e} | {p}\n")

            website_input.delete(0, END)
            pwd_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password_manager")
window.config(padx=50, pady=50)


img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website: ")
website.grid(row=1, column=0)
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)
pwd = Label(text="Password: ")
pwd.grid(row=3, column=0)


# Entry

website_input = Entry(width=39)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=39)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0,"coderef@gmail.com")
pwd_input = Entry(width=21)
pwd_input.grid(row=3, column=1)

# buttons

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=add_data)
add_btn.grid(row=4, column=1, columnspan=2)









window.mainloop()
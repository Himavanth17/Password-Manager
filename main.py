from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    new_letters = [random.choice(letters) for _ in range(nr_letters)]
    new_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    new_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password = new_letters+new_symbols+new_numbers
    random.shuffle(password)
    password = "".join(password)
    input2.insert(0, tkinter.END)
    input2.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    x = input.get()
    y = input1.get()
    z = input2.get()

    if len(x)==0 and len(z)==0:
        is_z_empty = messagebox.askokcancel(title="incomplete", message=f"web and password is empty : \n{x} ,\n{z}")
    elif len(x) == 0:
        is_x_empty = messagebox.askokcancel(title = "incomplete", message=f"website is empty : {x}")
    elif len(z) == 0:
        is_z_empty = messagebox.askokcancel(title="incomplete", message=f"password is empty : {x}")
    else:
        is_ok = messagebox.askokcancel(title=x, message=f"your information \nEmail: {x}, \nGmail: {y}, \nPassword: {z}")
        if is_ok:
            with open(r"C:\Users\Himavanth Reddy\Desktop\project\password.txt",mode = "a") as file:
                file.write(f" \n website: {x} | username: {y} | password : {z}")
                input.delete(0, tkinter.END)
                input2.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
import tkinter

window = tkinter.Tk()
window.title("Password Manager")
window.geometry("750x500")

#Image
canvas = tkinter.Canvas(width=750,height=500)
lock = tkinter.PhotoImage(file="logo.png")
canvas.create_image(375,150,image = lock)
canvas.grid(column=1,row=1)


#label

label = tkinter.Label()
label.config(text="Website: ",font=("Arial",10))
label.place(x=200,y=250)


label1 = tkinter.Label()
label1.config(text="Email/Username: ",font=("Arial",10))
label1.place(x=150,y=280)

label2 = tkinter.Label()
label2.config(text="Password: ",font=("Arial",10))
label2.place(x=190,y=310)

#input
input = tkinter.Entry(width=40)
input.focus()
input.place(x=280,y=250)


input1 = tkinter.Entry(width=40)
input1.place(x=280,y=280)
input1.insert(0,"x@gmailcom")


input2 = tkinter.Entry(width=30)
input2.place(x=280,y=310)


#Button
button = tkinter.Button()
button.config(text="Generate Password",command=generate)
button.place(x=500,y=305)

button1 = tkinter.Button()
button1.config(text="Add",width=34,command=add_details)
button1.place(x=280,y=350)






















window.mainloop()
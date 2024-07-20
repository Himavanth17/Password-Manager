from tkinter import messagebox
import random
import json
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

 #--------------------------------find passoword-----------------------------------------#

def find_password():
    get_name = input.get()
    try:
        with open("password.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error",message="no website was found")
    else:
        if get_name in data:
            email = data[get_name]["y"]
            password = data[get_name]["z"]
            messagebox.showinfo(title = get_name,message=f"webiste: {email} \n password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"no details for {get_name}")





# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    x = input.get()
    y = input1.get()
    z = input2.get()
    new_data = {
        x:{
            "y":y,
            "z":z
        }
    }

    if len(x)==0 and len(z)==0:
        is_z_empty = messagebox.askokcancel(title="incomplete", message=f"web and password is empty : \n{x} ,\n{z}")
    elif len(x) == 0:
        is_x_empty = messagebox.askokcancel(title = "incomplete", message=f"website is empty : {x}")
    elif len(z) == 0:
        is_z_empty = messagebox.askokcancel(title="incomplete", message=f"password is empty : {x}")
    else:
        try:
            with open(r"password.json",mode = "r") as file:
                #reading the old data
                data = json.load(file)
                #updating the old data with new data
        except FileNotFoundError:
            with open("password.json","w") as file:
                #saving updated data
                json.dump(new_data,file,indent=4)
        else:
            data.update(new_data)
            with open("password.json","w") as file:
                #saving updated data
                json.dump(data,file,indent=4)
        finally:
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
input = tkinter.Entry(width=30)
input.focus()
input.place(x=280,y=250)


input1 = tkinter.Entry(width=40)
input1.place(x=280,y=280)
input1.insert(0,"hi.22@gmailcom")


input2 = tkinter.Entry(width=30)
input2.place(x=280,y=310)


#Button
button = tkinter.Button()
button.config(text="Generate Password",width = 20,command=generate)
button.place(x=480,y=305)

button1 = tkinter.Button()
button1.config(text="Add",width=34,command=add_details)
button1.place(x=280,y=350)

button2 = tkinter.Button()
button2.config(text="Search",width=20,command=find_password)
button2.place(x=480,y=245)






















window.mainloop()
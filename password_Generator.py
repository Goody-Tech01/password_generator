from customtkinter import *
import string
import random
from tkinter import messagebox



root=CTk()
root.title("Password Generator")
root.geometry("900x600+100+50")
root.resizable(True,True)


def generate_password():
    length = int(length_slider.get())

    character= ""
    if upper_var.get():
        character += string.ascii_uppercase
    if lower_var.get():
        character += string.ascii_lowercase
    if digit_var.get():
        character += string.digits
    if symbol_var.get():
        character += string.punctuation
    if not character:
        messagebox.showwarning("Warning", "Select at least one option!!")
        return

    password = ''.join(random.choice(character) for _ in range(length))
    display_password(password)


def display_password(password):
    gen_entry.delete(0, "end")
    gen_entry.insert(0, password)

    update_strength(password)


def check_strength(password):
    length = len(password)

    upper  = any(i.isupper() for i in password)
    lower  = any(i.islower() for i in password)
    digit  = any(i.isdigit() for i in password)
    symbol = any(i in string.punctuation for i in password)
    score = sum([upper,lower,digit,symbol])

    if length >= 12 and score == 4:
        return 1.0, "Strong"
    elif length >= 8 and score >= 3:
        return 0.6, "Medium"
    else:
        return 0.3, "Weak"


def update_strength(password):
    value, text = check_strength(password)

    strength_bar.set(value)
    strength_label.configure(text=text)

    if value == 1.0:
        color = "#22c55e"
    elif value == 0.6:
        color = "yellow"
    else:
        color = "red"
    strength_bar.configure(progress_color=color)

def update_length(value):
    length_label.configure(text=str(int(value)))


def copy_password():
    text = gen_entry.get()
    if text:
      root.clipboard_clear()
      root.clipboard_append(text)
      messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Warning","No password to copy.")



pass_frame= CTkFrame(root,fg_color="#0a2540",width=800,height=500,corner_radius=15)
pass_frame.place(relx=0.5,rely=0.5,anchor="center")

CTkLabel(pass_frame,text="🔒",font=("Arial",60),text_color="white").place(x=5,y=8)
CTkLabel(pass_frame,text="Password Generator",font=("Arial",25),text_color="white").place(x=70,y=25)
CTkLabel(pass_frame,text="Create strong passwords to keep your account safe.",font=("Arial",15),
         text_color="white").place(x=70,y=50)

pass_length=CTkFrame(pass_frame,fg_color="#0a2540",width=790,height=130,
                     corner_radius=15,border_width=2,border_color="#163a5f")
pass_length.place(relx=0.5,rely=0.33,anchor="center")
CTkLabel(pass_length,text="Password Length",font=("Arial",18),text_color="white").place(x=10,y=10)

length_slider = CTkSlider(pass_length, from_=6, to=12, number_of_steps=6, width=700)
length_slider.set(12)
length_slider.place(relx=0.01, rely=0.3)
length_slider.configure(command=update_length)

length_label = CTkLabel(pass_length, text="12", width=40, height=30,
                        fg_color="#071a2f", corner_radius=8)
length_label.place(relx=0.92, rely=0.25)

# Checkboxes
upper_var = BooleanVar(value=True)
lower_var = BooleanVar(value=True)
digit_var = BooleanVar(value=True)
symbol_var = BooleanVar(value=True)

CTkCheckBox(pass_length, text="Include Uppercase (A-Z)", variable=upper_var).place(relx=0.1, rely=0.6, anchor="w")
CTkCheckBox(pass_length, text="Include Lowercase (a-z)", variable=lower_var).place(relx=0.1, rely=0.82, anchor="w")
CTkCheckBox(pass_length, text="Include Numbers (0-9)", variable=digit_var).place(relx=0.45, rely=0.62, anchor="w")
CTkCheckBox(pass_length, text="Include Symbols (!@#$%)", variable=symbol_var).place(relx=0.45, rely=0.83, anchor="w")


gen_pass=CTkFrame(pass_frame,fg_color="#0a2540",width=790,height=100,
                     corner_radius=15,border_width=2,border_color="#163a5f")
gen_pass.place(relx=0.5,rely=0.59,anchor="center")
CTkLabel(gen_pass,text="Generated Password",font=("Arial",18),text_color="white").place(x=10,y=10)

gen_entry=CTkEntry(gen_pass,font=("Arial",18),width=670,height=40,fg_color="#071a2f",
                   border_color="#2a5d85",text_color="white",justify="center")
gen_entry.place(relx=0.01,rely=0.5)

copy_btn = CTkButton(gen_pass,text="⧉ Copy",width=80,height=40,corner_radius=10,fg_color="#2a5d85",
    hover_color="#3b7ca8",command=copy_password)
copy_btn.place(relx=0.88, rely=0.7, anchor="w")


strength=CTkFrame(pass_frame,fg_color="#0a2540",width=790,height=70,
                     corner_radius=15,border_width=2,border_color="#163a5f")
strength.place(relx=0.5,rely=0.79,anchor="center")
CTkLabel(strength,text="Strength",font=("Arial",18),text_color="white").place(x=10,y=10)

strength_bar = CTkProgressBar(strength,progress_color="#22c55e",width=700,height=10,corner_radius=10)
strength_bar.place(relx=0.5, rely=0.6, anchor="center")
strength_bar.set(0)

strength_label = CTkLabel(strength, text="", text_color="white")
strength_label.place(relx=0.95, rely=0.2, anchor="e")


gen_code = CTkButton(pass_frame,text="Generate Password",width=600,height=40,corner_radius=10,
                     fg_color="#2a5d85",hover_color="#3b7ca8",command=generate_password)
gen_code.place(relx=0.5, rely=0.93, anchor="center")


root.mainloop()
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from Password_Manager import *

window = Tk()
window.title("Password Manager")
window.geometry("160x200")


def button_color(event, button, color):
    button.config(bg=color)


def loop_check_password(password, password_entry, image_list):
    if password_entry.winfo_ismapped():
        if password == password_entry.get():
            pass
        else:
            password = password_entry.get()
            result = check_password(password)
            for i in range(5):
                image = check if result[i] else x
                image_list[i].configure(image=image)
        window.after(
            100,
            lambda password=password, password_entry=password_entry, image_list=image_list: loop_check_password(
                password, password_entry, image_list
            ),
        )


def go_to_create():
    account_page.pack_forget()
    login_page.pack_forget()
    window.geometry("350x200")
    create_page.pack()
    window.update()
    loop_check_password("", password_box_create, requirement_images_create)


def go_to_login():
    account_page.pack_forget()
    create_page.pack_forget()
    window.geometry("160x200")
    login_page.pack()


def logged_in():
    create_page.pack_forget()
    login_page.pack_forget()
    username_button.configure(text=get_account("yes"))
    frame.pack()


def account_management_dropdown():
    if not account_dropdown.winfo_ismapped():
        add_password_page.pack_forget()
        get_password_canvas.pack_forget()
        edit_password_canvas.pack_forget()
        account_details_button.place(x=4, y=4)
        change_username_button.place(x=4, y=34)
        change_password_button.place(x=4, y=64)
        account_dropdown.place(x=380, y=40)
    else:
        account_info.place_forget()
        account_dropdown.place_forget()
        change_username_label.place_forget()
        change_username_entry.place_forget()
        change_username_submit.place_forget()
        change_password_label.place_forget()
        change_password_entry.place_forget()
        change_password_submit.place_forget()


def get_account_1():
    account_details_button.place_forget()
    change_username_button.place_forget()
    change_password_button.place_forget()
    account_info.configure(text=get_account())
    account_info.place(x=0, y=10)


def go_change_1():
    change_username_entry.delete(0, "end")
    account_details_button.place_forget()
    change_username_button.place_forget()
    change_password_button.place_forget()
    change_username_label.place(x=4, y=10)
    change_username_entry.place(x=10, y=30)
    change_username_submit.place(x=4, y=60)


def go_change_2():
    change_password_entry.delete(0, "end")
    account_details_button.place_forget()
    change_username_button.place_forget()
    change_password_button.place_forget()
    change_password_label.place(x=4, y=10)
    change_password_entry.place(x=10, y=30)
    change_password_submit.place(x=4, y=60)


def go_add():
    if not add_password_page.winfo_ismapped():
        account_dropdown.place_forget()
        get_password_canvas.pack_forget()
        edit_password_canvas.pack_forget()
        add_password_page.pack()
        window.update()
        loop_check_password("", pass_entry, requirement_images_add)
    else:
        add_password_page.pack_forget()


def change_username_1():
    change_username(change_username_entry.get())
    username_button.configure(text=change_username_entry.get())
    account_management_dropdown()


def change_password_1():
    change_password(change_password_entry.get())
    account_management_dropdown()


def create_account_1():
    result = create_account(username_box_create.get(), password_box_create.get())
    if result == "Succes":
        window.geometry("500x300")
        logged_in()
    elif result == "There is already an account created":
        error_label_1.configure(text="There is already \nan account \ncreated")
        error_button_1.configure(command=go_to_login)
        error_page_1.place(x=20, y=60)
    elif result == "Weak password":

        def clear_label():
            error_page_1.place_forget()

        error_label_1.configure(
            text="You need to meet \n all of the password \nrequirements",
            font=("arial", 9),
        )
        error_button_1.configure(command=clear_label)
        error_page_1.place(x=20, y=60)


def login_1():
    result = login(username_box_login.get(), password_box_login.get())
    if result == "Succes":
        window.geometry("500x300")
        logged_in()
    elif result == "You need to create an account":
        error_label_2.configure(text="You need to \ncreate an account")
        error_button_2.configure(command=go_to_create)
        error_page_2.place(x=20, y=60)
    elif result == "Username or password is incorrect":
        error_label_2.configure(
            text="The Username or \npassword you \nentered is \nincorrect"
        )

        def error_forget():
            error_page_2.place_forget()
            username_box_login.delete(0, "end")
            password_box_login.delete(0, "end")

        error_button_2.configure(command=error_forget)
        error_page_2.place(x=20, y=60)


def add_password():
    result = generate_login(website_entry.get(), user_entry.get(), pass_entry.get())
    if result == "Succes":
        website_entry.delete(0, "end")
        user_entry.delete(0, "end")
        pass_entry.delete(0, "end")
    elif result == "A login already exist for the website":
        error_page = Frame(add_password_page, width=125, heigh=120, bg="#243f57")

        def ok_click():
            error_page.place_forget()
            entries = [website_entry, user_entry, pass_entry]
            for entry in entries:
                entry.delete(0, "end")

        error_page = Frame(add_password_page, width=125, heigh=120, bg="#243f57")
        error_label = Label(
            error_page,
            text="A password \nalready exist \nfor this website",
            bg="#243f57",
            foreground="#f74949",
            font=("Arial", 11),
        )
        error_label.place(x=11, y=10)
        error_button = Button(
            error_page,
            text="Ok",
            relief=FLAT,
            width=11,
            bg="#243f57",
            foreground="white",
            command=ok_click,
            font=button_font_1,
        )
        error_button.configure(activebackground="#3d5569", activeforeground="white")
        error_button.bind(
            "<Enter>", lambda event: button_color(event, error_button, "#3d5569")
        )
        error_button.bind(
            "<Leave>", lambda event: button_color(event, error_button, "#243f57")
        )
        error_button.place(x=8, y=80)
        error_page.place(x=90, y=50)


def generate_password_1():
    length = password_len.get()
    if length.isdigit():
        if int(password_len.get()) >= 12 and int(password_len.get()) <= 36:
            password = generate_password(int(password_len.get()))
        else:
            if int(password_len.get()) <= 12:
                password = "Use a number greater than 12"
            if int(password_len.get()) >= 36:
                password = "Use a number less than 36"
    else:
        password = "Use Number"
    generated_password.configure(text=password)
    generated_password.place(x=155, y=235)


def get_visible_y_values(canvas):
    top_normalized, bottom_normalized = canvas.yview()
    canvas_height = canvas.winfo_height()
    scrollable_height = canvas_height - canvas_height / (
        bottom_normalized - top_normalized
    )

    top_pixel = -scrollable_height * top_normalized
    bottom_pixel = -scrollable_height * bottom_normalized + canvas_height

    return top_pixel, bottom_pixel


def get_password_1():
    if not get_password_canvas.winfo_ismapped():
        add_password_page.pack_forget()
        edit_password_canvas.pack_forget()
        account_dropdown.place_forget()
        websites = get_websites()
        y = 25
        buttons = []
        frames = []

        def on_scroll(event):
            get_password_canvas.yview_scroll(-1 * (event.delta // 120), "units")

        def get_password(website):
            login_info = get_login(website)
            top_pixel, bottom_pixel = get_visible_y_values(get_password_canvas)
            place_y = ((top_pixel + bottom_pixel) / 2) - 55
            login_info_frame = Frame(
                get_password_canvas, width=130, height=100, bg="#243f57"
            )
            login_info_label = Label(
                login_info_frame,
                text=login_info,
                font=("arial", 10),
                bg="#243f57",
                foreground="white",
            )
            login_info_label.place(x=5, y=0)

            def ok_button_click():
                get_password_canvas.delete(id)

            ok_button = Button(
                login_info_frame,
                text="Ok",
                relief=FLAT,
                width=10,
                bg="#243f57",
                foreground="white",
                command=ok_button_click,
                font=button_font_1,
                activebackground="#3d5569",
                activeforeground="white",
            )
            ok_button.bind(
                "<Enter>",
                lambda event: button_color(event, ok_button, "#3d5569"),
            )
            ok_button.bind(
                "<Leave>",
                lambda event: button_color(event, ok_button, "#243f57"),
            )
            ok_button.place(x=10, y=70)
            id = get_password_canvas.create_window(
                185, place_y, window=login_info_frame
            )

        for website in websites:
            i = websites.index(website)
            website_frame = Frame(
                get_password_canvas, width=330, height=35, bg="#0c2a44"
            )
            frames.append(website_frame)
            website_label = Label(
                frames[i],
                text=website,
                font=button_font_1,
                bg="#0c2a44",
                foreground="white",
            )
            website_label.place(x=5, y=5)
            get_password_button = Button(
                website_frame,
                text="Get Password",
                relief=FLAT,
                width=13,
                height=1,
                bg="#0c2a44",
                foreground="white",
                command=lambda website=website: get_password(website[0]),
                font=button_font_1,
                activebackground="#243f57",
                activeforeground="white",
            )
            buttons.append(get_password_button)
            buttons[i].bind(
                "<Enter>",
                lambda event, i=i: button_color(event, buttons[i], "#243f57"),
            )
            buttons[i].bind(
                "<Leave>",
                lambda event, i=i: button_color(event, buttons[i], "#0c2a44"),
            )
            buttons[i].place(x=200, y=1)
            get_password_canvas.create_window(185, y, window=frames[i])
            y += 50
        get_password_canvas.update_idletasks()
        y -= 20
        get_password_canvas.after_idle(
            lambda: get_password_canvas.config(scrollregion=(0, 0, 330, y))
        )
        get_password_canvas.bind_all("<MouseWheel>", on_scroll)
        get_password_canvas.pack()
    else:
        get_password_canvas.pack_forget()


def edit_password_1():
    if not edit_password_canvas.winfo_ismapped():
        add_password_page.pack_forget()
        get_password_canvas.pack_forget()
        account_dropdown.place_forget()
        websites = get_websites()
        y = 25
        buttons = []
        frames = []

        def on_scroll(event):
            edit_password_canvas.yview_scroll(-1 * (event.delta // 120), "units")

        def edit_password(website):
            top_pixel, bottom_pixel = get_visible_y_values(edit_password_canvas)
            place_y = ((top_pixel + bottom_pixel) / 2) - 75
            login_info_frame = Frame(
                edit_password_canvas, width=120, height=130, bg="#243f57"
            )

            def change_button_click():
                edit_login(website, new_username_entry.get(), new_password_entry.get())
                edit_password_canvas.delete(id)

            new_username_label = Label(
                login_info_frame,
                text="New Username",
                font=("arial", 11),
                bg="#243f57",
                foreground="white",
            )
            new_username_label.place(x=8, y=0)
            new_username_entry = Entry(login_info_frame, width=16)
            new_username_entry.place(x=10, y=25)
            new_password_label = Label(
                login_info_frame,
                text="New Password",
                font=("arial", 11),
                bg="#243f57",
                foreground="white",
            )
            new_password_label.place(x=8, y=45)
            new_password_entry = Entry(login_info_frame, width=16)
            new_password_entry.place(x=10, y=70)
            change_button = Button(
                login_info_frame,
                text="Change",
                relief=FLAT,
                width=10,
                bg="#243f57",
                foreground="white",
                command=change_button_click,
                font=button_font_1,
                activebackground="#3d5569",
                activeforeground="white",
            )
            change_button.bind(
                "<Enter>",
                lambda event: button_color(event, change_button, "#3d5569"),
            )
            change_button.bind(
                "<Leave>",
                lambda event: button_color(event, change_button, "#243f57"),
            )
            change_button.place(x=10, y=95)
            id = edit_password_canvas.create_window(
                185, place_y, window=login_info_frame
            )

        for website in websites:
            i = websites.index(website)
            website_frame = Frame(
                edit_password_canvas, width=330, height=35, bg="#0c2a44"
            )
            frames.append(website_frame)
            website_label = Label(
                frames[i],
                text=website,
                font=button_font_1,
                bg="#0c2a44",
                foreground="white",
            )
            website_label.place(x=5, y=5)
            get_password_button = Button(
                website_frame,
                text="Edit Password",
                relief=FLAT,
                width=13,
                height=1,
                bg="#0c2a44",
                foreground="white",
                command=lambda website=website: edit_password(website[0]),
                font=button_font_1,
                activebackground="#243f57",
                activeforeground="white",
            )
            buttons.append(get_password_button)
            buttons[i].bind(
                "<Enter>",
                lambda event, i=i: button_color(event, buttons[i], "#243f57"),
            )
            buttons[i].bind(
                "<Leave>",
                lambda event, i=i: button_color(event, buttons[i], "#0c2a44"),
            )
            buttons[i].place(x=200, y=1)
            edit_password_canvas.create_window(185, y, window=frames[i])
            y += 50
        edit_password_canvas.update_idletasks()
        y -= 20
        edit_password_canvas.after_idle(
            lambda: edit_password_canvas.config(scrollregion=(0, 0, 330, y))
        )
        edit_password_canvas.bind_all("<MouseWheel>", on_scroll)
        edit_password_canvas.pack()
    else:
        edit_password_canvas.pack_forget()


button_font_1 = ("Arial", 12)
label_font_1 = ("Arial", 10)
logo = ImageTk.PhotoImage(Image.open("Assets/Logo.png"))
logo_1 = ImageTk.PhotoImage(Image.open("Assets/Logo_1.png"))
check = ImageTk.PhotoImage(Image.open("Assets/Check.png"))
x = ImageTk.PhotoImage(Image.open("Assets/X.png"))
password_requirements = [
    "Have at least 12 characters",
    "Have at least 1 number",
    "Have at least 1 lowercase \nletter",
    "Have at least 1 uppercase \nletter",
    "Have at least 1 special \ncharacter",
]

account_page = Frame(window, width=160, height=200, bg="#0c2a44")
logo_label_1 = Label(account_page, image=logo)
logo_label_1.place(x=20, y=20)
create_account_button = Button(
    account_page,
    text="Create Account",
    relief=FLAT,
    width=15,
    bg="#0c2a44",
    foreground="white",
    command=go_to_create,
    font=button_font_1,
)
create_account_button.configure(activebackground="#243f57", activeforeground="white")
create_account_button.bind(
    "<Enter>", lambda event: button_color(event, create_account_button, "#243f57")
)
create_account_button.bind(
    "<Leave>", lambda event: button_color(event, create_account_button, "#0c2a44")
)
create_account_button.place(x=8, y=93)
login_button = Button(
    account_page,
    text="Login",
    relief=FLAT,
    width=15,
    bg="#0c2a44",
    foreground="white",
    command=go_to_login,
    font=button_font_1,
)
login_button.configure(activebackground="#243f57", activeforeground="white")
login_button.bind("<Enter>", lambda event: button_color(event, login_button, "#243f57"))
login_button.bind("<Leave>", lambda event: button_color(event, login_button, "#0c2a44"))
login_button.place(x=8, y=133)
account_page.pack()

create_page = Frame(window, width=350, height=200, bg="#0c2a44")
logo_label_2 = Label(create_page, image=logo)
logo_label_2.place(x=20, y=20)
username_label = Label(
    create_page, text="Username", bg="#0c2a44", foreground="white", font=label_font_1
)
username_label.place(x=18, y=65)
username_box_create = Entry(create_page)
username_box_create.place(x=20, y=85)
password_label = Label(
    create_page, text="Password", bg="#0c2a44", foreground="white", font=label_font_1
)
password_label.place(x=18, y=110)
password_box_create = Entry(create_page)
password_box_create.place(x=20, y=130)
create_account_submit = Button(
    create_page,
    text="Create Account",
    relief=FLAT,
    width=15,
    bg="#0c2a44",
    foreground="white",
    command=create_account_1,
    font=button_font_1,
)
create_account_submit.configure(activebackground="#243f57", activeforeground="white")
create_account_submit.bind(
    "<Enter>", lambda event: button_color(event, create_account_submit, "#243f57")
)
create_account_submit.bind(
    "<Leave>", lambda event: button_color(event, create_account_submit, "#0c2a44")
)
create_account_submit.place(x=8, y=160)

password_requirements_label = Label(
    create_page,
    text="Password Requirements",
    bg="#0c2a44",
    foreground="white",
    font=("Arial", 11),
)
password_requirements_label.place(x=150, y=8)
x_1, y_1, run = 175, 30, 0
for password_requirement in password_requirements:
    requirement_label = Label(
        create_page,
        text=password_requirement,
        bg="#0c2a44",
        foreground="white",
        font=("Arial", 10),
    )
    requirement_label.place(x=x_1, y=y_1)
    if run < 2:
        y_1 += 20
    else:
        y_1 += 40
    run += 1

requirement_images_create = [
    Label(create_page, image=x, bg="#0c2a44"),
    Label(create_page, image=x, bg="#0c2a44"),
    Label(create_page, image=x, bg="#0c2a44"),
    Label(create_page, image=x, bg="#0c2a44"),
    Label(create_page, image=x, bg="#0c2a44"),
]
requirement_images_create[0].place(x=157, y=34)
requirement_images_create[1].place(x=157, y=54)
requirement_images_create[2].place(x=157, y=74)
requirement_images_create[3].place(x=157, y=114)
requirement_images_create[4].place(x=157, y=154)

error_page_1 = Frame(create_page, width=125, height=120, bg="#243f57")
error_label_1 = Label(
    error_page_1, text="", bg="#243f57", foreground="#f74949", font=("Arial", 11)
)
error_label_1.place(x=3, y=10)
error_button_1 = Button(
    error_page_1,
    text="Ok",
    relief=FLAT,
    width=11,
    bg="#243f57",
    foreground="white",
    font=button_font_1,
)
error_button_1.configure(activebackground="#3d5569", activeforeground="white")
error_button_1.bind(
    "<Enter>", lambda event: button_color(event, error_button_1, "#3d5569")
)
error_button_1.bind(
    "<Leave>", lambda event: button_color(event, error_button_1, "#243f57")
)
error_button_1.place(x=8, y=80)

login_page = Frame(window, width=160, height=200, bg="#0c2a44")
logo_label_3 = Label(login_page, image=logo)
logo_label_3.place(x=20, y=20)
username_label = Label(
    login_page, text="Username", bg="#0c2a44", foreground="white", font=label_font_1
)
username_label.place(x=18, y=65)
username_box_login = Entry(login_page)
username_box_login.place(x=20, y=85)
password_label = Label(
    login_page, text="Password", bg="#0c2a44", foreground="white", font=label_font_1
)
password_label.place(x=18, y=110)
password_box_login = Entry(login_page)
password_box_login.place(x=20, y=130)
login_submit = Button(
    login_page,
    text="Login",
    relief=FLAT,
    width=15,
    bg="#0c2a44",
    foreground="white",
    command=login_1,
    font=button_font_1,
)
login_submit.configure(activebackground="#243f57", activeforeground="white")
login_submit.bind("<Enter>", lambda event: button_color(event, login_submit, "#243f57"))
login_submit.bind("<Leave>", lambda event: button_color(event, login_submit, "#0c2a44"))
login_submit.place(x=8, y=160)

error_page_2 = Frame(login_page, width=125, height=120, bg="#243f57")
error_label_2 = Label(
    error_page_2, text="", bg="#243f57", foreground="#f74949", font=("Arial", 11)
)
error_label_2.place(x=3, y=10)
error_button_2 = Button(
    error_page_2,
    text="Ok",
    relief=FLAT,
    width=11,
    bg="#243f57",
    foreground="white",
    font=button_font_1,
)
error_button_2.configure(activebackground="#3d5569", activeforeground="white")
error_button_2.bind(
    "<Enter>", lambda event: button_color(event, error_button_2, "#3d5569")
)
error_button_2.bind(
    "<Leave>", lambda event: button_color(event, error_button_2, "#243f57")
)
error_button_2.place(x=8, y=80)

frame = Frame(window, width=500, height=300, bg="#3d5569")

top_bar = Frame(frame, width=500, height=35, bg="#0a2236")
logo_label_4 = Label(top_bar, image=logo_1, bg="#0a2236")
logo_label_4.place(x=5, y=1)
username_button = Button(
    top_bar,
    text="",
    relief=FLAT,
    width=10,
    bg="#0a2236",
    foreground="white",
    command=account_management_dropdown,
    font=("Arial", 10),
)
username_button.configure(activebackground="#243f57", activeforeground="white")
username_button.bind(
    "<Enter>", lambda event: button_color(event, username_button, "#243f57")
)
username_button.bind(
    "<Leave>", lambda event: button_color(event, username_button, "#0a2236")
)
username_button.place(x=400, y=3)
top_bar.pack()

account_dropdown = Frame(frame, width=115, height=97, bg="#0a2236")
account_details_button = Button(
    account_dropdown,
    text="Account Details",
    relief=FLAT,
    width=14,
    bg="#0a2236",
    foreground="white",
    command=get_account_1,
    font=("Arial", 9),
)
account_details_button.configure(activebackground="#243f57", activeforeground="white")
account_details_button.bind(
    "<Enter>", lambda event: button_color(event, account_details_button, "#243f57")
)
account_details_button.bind(
    "<Leave>", lambda event: button_color(event, account_details_button, "#0a2236")
)
change_username_button = Button(
    account_dropdown,
    text="Change Username",
    relief=FLAT,
    width=14,
    bg="#0a2236",
    foreground="white",
    command=go_change_1,
    font=("Arial", 9),
)
change_username_button.configure(activebackground="#243f57", activeforeground="white")
change_username_button.bind(
    "<Enter>", lambda event: button_color(event, change_username_button, "#243f57")
)
change_username_button.bind(
    "<Leave>", lambda event: button_color(event, change_username_button, "#0a2236")
)
change_password_button = Button(
    account_dropdown,
    text="Change Password",
    relief=FLAT,
    width=14,
    bg="#0a2236",
    foreground="white",
    command=go_change_2,
    font=("Arial", 9),
)
change_password_button.configure(activebackground="#243f57", activeforeground="white")
change_password_button.bind(
    "<Enter>", lambda event: button_color(event, change_password_button, "#243f57")
)
change_password_button.bind(
    "<Leave>", lambda event: button_color(event, change_password_button, "#0a2236")
)
account_info = Label(
    account_dropdown, text="", bg="#0a2236", foreground="white", font=("Arial", 11)
)
change_username_label = Label(
    account_dropdown,
    text="New Username",
    bg="#0a2236",
    foreground="white",
    font=("Arial", 11),
)
change_username_entry = Entry(account_dropdown, width=15)
change_username_submit = Button(
    account_dropdown,
    text="Change Username",
    relief=FLAT,
    width=14,
    bg="#0a2236",
    foreground="white",
    command=change_username_1,
    font=("Arial", 9),
)
change_username_submit.configure(activebackground="#243f57", activeforeground="white")
change_username_submit.bind(
    "<Enter>", lambda event: button_color(event, change_username_submit, "#243f57")
)
change_username_submit.bind(
    "<Leave>", lambda event: button_color(event, change_username_submit, "#0a2236")
)
change_password_label = Label(
    account_dropdown,
    text="New Password",
    bg="#0a2236",
    foreground="white",
    font=("Arial", 11),
)
change_password_entry = Entry(account_dropdown, width=15)
change_password_submit = Button(
    account_dropdown,
    text="Change Password",
    relief=FLAT,
    width=14,
    bg="#0a2236",
    foreground="white",
    command=change_password_1,
    font=("Arial", 9),
)
change_password_submit.configure(activebackground="#243f57", activeforeground="white")
change_password_submit.bind(
    "<Enter>", lambda event: button_color(event, change_password_submit, "#243f57")
)
change_password_submit.bind(
    "<Leave>", lambda event: button_color(event, change_password_submit, "#0a2236")
)

side_bar = Frame(frame, width=135, height=265, bg="#243f57")
add_password_button = Button(
    side_bar,
    text="Add Password",
    relief=FLAT,
    width=12,
    bg="#243f57",
    foreground="white",
    command=go_add,
    font=button_font_1,
)
add_password_button.configure(activebackground="#3d5569", activeforeground="white")
add_password_button.bind(
    "<Enter>", lambda event: button_color(event, add_password_button, "#3d5569")
)
add_password_button.bind(
    "<Leave>", lambda event: button_color(event, add_password_button, "#243f57")
)
add_password_button.place(x=9, y=5)
get_login_button = Button(
    side_bar,
    text="Get Password",
    relief=FLAT,
    width=12,
    bg="#243f57",
    foreground="white",
    command=get_password_1,
    font=button_font_1,
)
get_login_button.configure(activebackground="#3d5569", activeforeground="white")
get_login_button.bind(
    "<Enter>", lambda event: button_color(event, get_login_button, "#3d5569")
)
get_login_button.bind(
    "<Leave>", lambda event: button_color(event, get_login_button, "#243f57")
)
get_login_button.place(x=9, y=55)
edit_login_button = Button(
    side_bar,
    text="Edit Password",
    relief=FLAT,
    width=12,
    bg="#243f57",
    foreground="white",
    command=edit_password_1,
    font=button_font_1,
)
edit_login_button.configure(activebackground="#3d5569", activeforeground="white")
edit_login_button.bind(
    "<Enter>", lambda event: button_color(event, edit_login_button, "#3d5569")
)
edit_login_button.bind(
    "<Leave>", lambda event: button_color(event, edit_login_button, "#243f57")
)
edit_login_button.place(x=9, y=105)
side_bar.pack(side=LEFT)

add_password_page = Frame(frame, width=365, height=265, bg="#3d5569")
website_label = Label(
    add_password_page,
    text="Website",
    bg="#3d5569",
    foreground="white",
    font=("arial", 11),
)
website_label.place(x=10, y=19)
website_entry = Entry(add_password_page)
website_entry.place(x=10, y=40)
user_label = Label(
    add_password_page,
    text="Username",
    bg="#3d5569",
    foreground="white",
    font=("arial", 11),
)
user_label.place(x=10, y=74)
user_entry = Entry(add_password_page)
user_entry.place(x=10, y=95)
pass_label = Label(
    add_password_page,
    text="Password",
    bg="#3d5569",
    foreground="white",
    font=("arial", 11),
)
pass_label.place(x=10, y=129)
pass_entry = Entry(add_password_page)
pass_entry.place(x=10, y=150)
new_pass_submit = Button(
    add_password_page,
    text="Add Password",
    relief=FLAT,
    width=12,
    bg="#3d5569",
    foreground="white",
    command=add_password,
    font=button_font_1,
)
new_pass_submit.configure(activebackground="#506579", activeforeground="white")
new_pass_submit.bind(
    "<Enter>", lambda event: button_color(event, new_pass_submit, "#506579")
)
new_pass_submit.bind(
    "<Leave>", lambda event: button_color(event, new_pass_submit, "#3d5569")
)
new_pass_submit.place(x=10, y=185)
password_recommendations = Label(
    add_password_page,
    text="Password Requirements",
    bg="#3d5569",
    foreground="white",
)
password_recommendations.configure(
    font=font.Font(family="arial", size=10, weight="bold")
)
password_recommendations.place(x=150, y=10)
requirement_images_add = [
    Label(add_password_page, image=x, bg="#3d5569"),
    Label(add_password_page, image=x, bg="#3d5569"),
    Label(add_password_page, image=x, bg="#3d5569"),
    Label(add_password_page, image=x, bg="#3d5569"),
    Label(add_password_page, image=x, bg="#3d5569"),
]
x_1, y_1, run = 170, 27, 0
for password_requirement in password_requirements:
    requirement_label = Label(
        add_password_page,
        text=password_requirement,
        bg="#3d5569",
        foreground="white",
        font=("Arial", 8),
    )
    requirement_label.place(x=x_1, y=y_1)
    requirement_images_add[password_requirements.index(password_requirement)].place(
        x=(x_1 - 15), y=y_1
    )
    if run < 2:
        y_1 += 15
    else:
        y_1 += 28
    run += 1

password_generator_label = Label(
    add_password_page,
    text="Password Generator",
    font=("arial", 12),
    bg="#3d5569",
    foreground="white",
)
password_generator_label.place(x=150, y=145)
password_len_label = Label(
    add_password_page,
    text="Password length:",
    font=("arial", 10),
    bg="#3d5569",
    foreground="white",
)
password_len_label.place(x=155, y=172)
password_len = Entry(add_password_page, width=3)
password_len.place(x=265, y=174)
gen_password = Button(
    add_password_page,
    text="Generate Password",
    relief=FLAT,
    width=14,
    bg="#3d5569",
    foreground="white",
    command=generate_password_1,
    font=("arial", 10),
)
gen_password.configure(activebackground="#506579", activeforeground="white")
gen_password.bind("<Enter>", lambda event: button_color(event, gen_password, "#506579"))
gen_password.bind("<Leave>", lambda event: button_color(event, gen_password, "#3d5569"))
gen_password.place(x=160, y=200)
generated_password = Label(
    add_password_page,
    text="",
    bg="#3d5569",
    foreground="white",
    font=("arial", 10),
)

get_password_canvas = Canvas(
    frame,
    width=365,
    height=265,
    bg="#3d5569",
    borderwidth=0,
    highlightthickness=0,
)

edit_password_canvas = Canvas(
    frame,
    width=365,
    height=265,
    bg="#3d5569",
    borderwidth=0,
    highlightthickness=0,
)

window.mainloop()

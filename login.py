from libraries import customtkinter, ImageTk, Image, tkinter
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd


def sigInWindow():
    userData = pd.read_csv('data/database.csv')
    df = pd.DataFrame(userData)

    def verificationMail():
        text = sig_entry1.get()
        if '@' in text and text not in df['email'].values:
            return True

        elif '@' in text:
            return False
        else:
            return False

    def sigInButtonAction():
        # verificar contraseña y correo
        if same_password_verification(0) and verificationMail():
            email = sig_entry1.get()
            password = sig_entry2.get()
            name = sig_entry4.get()
            name = name.capitalize()
            lastname = sig_entry5.get()
            lastname = lastname.capitalize()
            # encriptar contraseña
            password = generate_password_hash(password)
            # crear usuario
            userData = {'email': email, 'password': password,
                        'name': name, 'lastname': lastname}
            df = pd.DataFrame(userData, index=[0])
            df.to_csv('data/database.csv', mode='a', header=False, index=False)
            # destruir ventana de registro
            sigInw.destroy()
            # crear ventana de login
            logInWindow()

    def sigIn_mail_restiction(event):
        sig_entry1.configure(border_color='#565b5e')
        text = sig_entry1.get()
        # verificar que el mail no este en uso
        df = pd.DataFrame(userData)
        if '@' in text and text not in df['email'].values:
            sig_entry1.configure(border_color='#565b5e')
            return True

        elif '@' in text:
            l4.configure(text='correo en uso', text_color='red')
            sig_entry1.configure(border_color='red')
            return False
        else:
            l4.configure(text='correo invalido', text_color='red')
            sig_entry1.configure(border_color='red')
            return False

    def focus_next_widget(event, nomral_entry):
        nomral_entry.configure(border_color='#565b5e')
        event.widget.tk_focusNext().focus()
        return ("break")

    def same_password_verification(event):
        sig_entry4.focus()
        pas1 = sig_entry2.get()
        pas2 = sig_entry3.get()
        if pas1 == pas2:
            sig_entry2.configure(border_color='#565b5e')
            sig_entry3.configure(border_color='#565b5e')
            l4.configure(text='')
            return True
        else:
            l4.configure(text='Las contraseñas no coinciden',
                         text_color='red')
            sig_entry2.configure(border_color='red')
            sig_entry3.configure(border_color='red')
            return False
    # creating custom tkinter window
    sigInw = customtkinter.CTk()
    sigInw.geometry('500x530')
    sigInw.resizable(False, False)
    sigInw.title('Sign in')
    sigInw.focus()
    img1 = ImageTk.PhotoImage(Image.open(
        "images/pattern.png"))  # creating image object
    l1Sig = customtkinter.CTkLabel(
        master=sigInw, image=img1)  # creating custom label
    l1Sig.pack()  # placing label

    sigframe = customtkinter.CTkFrame(
        master=l1Sig, width=310, height=385, bg_color="#2b2b2b")
    sigframe.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(
        master=sigframe, text="Crear Cuenta", font=('Century Gothic', 30, 'bold'))
    l2.place(x=50, y=0)

    l4 = customtkinter.CTkLabel(master=sigframe, text="", text_color='red')
    l4.place(x=50, y=32)

    sig_entry1 = customtkinter.CTkEntry(
        master=sigframe, width=220, height=40, placeholder_text='Correo electrónico', border_color='#565b5e')
    sig_entry1.place(x=50, y=60)
    sig_entry1.bind("<FocusOut>", sigIn_mail_restiction)
    sig_entry1.bind("<Return>", lambda e: focus_next_widget(e, sig_entry2))
    sig_entry1.bind(
        "<FocusIn>", lambda e: sig_entry1.configure(border_color='white'))
    sig_entry1.bind("<Key>", lambda e: l4.configure(text_color='#2b2b2b'))

    sig_entry2 = customtkinter.CTkEntry(
        master=sigframe, width=220, height=40, placeholder_text='Contraseña', show='*')
    sig_entry2.place(x=50, y=110)
    sig_entry2.bind("<Return>", lambda e: focus_next_widget(e, sig_entry3))
    sig_entry2.bind(
        "<FocusIn>", lambda e: sig_entry2.configure(border_color='white'))
    sig_entry2.bind("<Key>", lambda e: l4.configure(text_color='#2b2b2b'))
    sig_entry2.bind("<FocusOut>", lambda e: sig_entry2.configure(
        border_color='#565b5e'))

    sig_entry3 = customtkinter.CTkEntry(
        master=sigframe, width=220, height=40, placeholder_text='Confirmar contraseña', show='*')
    sig_entry3.place(x=50, y=160)
    sig_entry3.bind("<Return>", lambda e: focus_next_widget(e, sig_entry4))
    sig_entry3.bind(
        "<FocusIn>", lambda e: sig_entry3.configure(border_color='white'))
    sig_entry3.bind("<Key>", lambda e: l4.configure(text_color='#2b2b2b'))
    sig_entry3.bind("<FocusOut>", same_password_verification)

    sig_entry4 = customtkinter.CTkEntry(
        master=sigframe, width=220, height=40, placeholder_text='Nombre')
    sig_entry4.place(x=50, y=210)
    sig_entry4.bind("<Return>", lambda e: focus_next_widget(e, sig_entry5))
    sig_entry4.bind(
        "<FocusIn>", lambda e: sig_entry4.configure(border_color='white'))
    sig_entry4.bind(
        "<FocusOut>", lambda e: sig_entry4.configure(border_color='#565b5e'))

    sig_entry5 = customtkinter.CTkEntry(
        master=sigframe, width=220, height=40, placeholder_text='Apellido')
    sig_entry5.place(x=50, y=260)
    sig_entry5.bind(
        "<Return>", sigInButtonAction())
    sig_entry5.bind(
        "<FocusIn>", lambda e: sig_entry5.configure(border_color='white'))
    sig_entry5.bind(
        "<FocusOut>", lambda e: sig_entry5.configure(border_color='#565b5e'))
    # Create custom button for login
    sigInbutton = customtkinter.CTkButton(
        master=sigframe, width=220, height=38, text="Crear cuenta", command=sigInButtonAction, corner_radius=8)
    sigInbutton.place(x=50, y=320)
    sigInw.mainloop()  # running mainloop


def logInWindow():
    userData = pd.read_csv('data/database.csv')
    df = pd.DataFrame(userData)

    def login():
        correo = entry1.get()
        pasw = entry2.get()
        # identificar si el usuario existe
        if correo in df['email'].values:
            # verificar si la contraseña del usuario encontrado es correcta
            if check_password_hash(df.loc[df['email'] == correo, 'password'].values[0], pasw):
                return True
            else:
                # contraseña incorrecta
                if pasw == '':
                    l4.configure(text='Por favor ingrese su contraseña',
                                 text_color='red')
                    entry2.configure(border_color='red')

                else:
                    l4.configure(text='contraseña incorrecta',
                                 text_color='red')
                    entry2.delete(0, 'end')
                    entry2.configure(border_color='red')
                return False
        else:
            # usuario no existe
            if correo == '' and pasw == '':
                l4.configure(text='Por favor ingrese su correo y contraseña',
                             text_color='red')

            elif correo == '':
                l4.configure(text='Por favor ingrese su correo',
                             text_color='red')
                entry1.configure(border_color='red')

            elif pasw == '':
                l4.configure(text='Por favor ingrese su contraseña',
                             text_color='red')
                entry2.configure(border_color='red')
            else:
                l4.configure(text='usuario no encontrado',
                             text_color='red')
                entry2.delete(0, 'end')
            return False

    def button_function():
        if login():
            print('Login successful')
            # destroying login window
            app.destroy()
            # creating custom tkinter window
            w = customtkinter.CTk()
            w.resizable(False, False)
            w.geometry('1080x620')
            w.eval('tk::PlaceWindow . center')
            w.title('Welcome')
            l1 = customtkinter.CTkLabel(
                master=w, text="Home Page", font=('Century Gothic', 60))  # creating custom label
            # placing label
            l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
            w.mainloop()  # running mainloop
        else:
            pass

    def on_entry1_return(event):
        entry2.focus()

    def on_entry2_return(event):
        button_function()

    def out_entry1(event):
        entry1.configure(border_color='#565b5e')
        text = entry1.get()
        if '@' in text:
            entry1.configure(border_color='#565b5e')
        else:
            l4.configure(text='correo invalido', text_color='red')
            entry1.configure(border_color='red')

    def sigButtonAction():
        app.destroy()
        sigInWindow()

    app = customtkinter.CTk()  # creating cutstom tkinter window
    app.geometry("500x530")  # setting window size
    app.title('Login')  # setting window title
    app.resizable(False, False)  # making window non-resizable
    app.eval('tk::PlaceWindow . center')  # placing window in center of screen
    img1 = ImageTk.PhotoImage(Image.open(
        "images/pattern.png"))  # creating image object
    l1 = customtkinter.CTkLabel(
        master=app, image=img1)  # creating custom label
    l1.pack()  # placing label

    # creating custom frame
    frame = customtkinter.CTkFrame(
        master=l1, width=310, height=385, bg_color="#2b2b2b")  # setting frame size and background color
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)  # placing frame

    # creating custom label
    l2 = customtkinter.CTkLabel(
        master=frame, text="Iniciar Sesión", font=('Century Gothic', 30, 'bold'))
    l2.place(x=50, y=45)

    # creating custom entry
    entry1 = customtkinter.CTkEntry(
        master=frame, width=220, height=42, placeholder_text='Correo electrónico', border_color='#565b5e')
    entry1.place(x=50, y=120)
    entry1.bind("<Return>", on_entry1_return)
    entry1.bind("<Key>", lambda e: l4.configure(text_color='#2b2b2b'))
    entry1.bind("<FocusIn>", lambda e: entry1.configure(border_color='white'))
    entry1.bind("<FocusOut>", out_entry1)

    # creating custom entry2
    entry2 = customtkinter.CTkEntry(
        master=frame, width=220, height=42, placeholder_text='Contraseña', show="*")
    entry2.place(x=50, y=175)
    entry2.bind("<Return>", on_entry2_return)
    entry2.bind("<Key>", lambda e: l4.configure(text_color='#2b2b2b'))
    entry2.bind("<FocusIn>", lambda e: entry2.configure(border_color='white'))
    entry2.bind("<FocusOut>", lambda e: entry2.configure(
        border_color='#565b5e'))

    # creating custom label for forgot password
    l3 = customtkinter.CTkLabel(
        master=frame, text="¿Olvidaste tu contraseña?", font=('Century Gothic', 12))
    l3.place(x=105, y=220)

    # Create custom button for login
    button1 = customtkinter.CTkButton(
        master=frame, width=220, height=38, text="Iniciar Sesión", command=button_function, corner_radius=8, )
    button1.place(x=50, y=255)

    # creating custom label for invalid credentials
    l4 = customtkinter.CTkLabel(
        master=frame, text="", font=('Century Gothic', 12), text_color='red')
    l4.place(x=70, y=90)

    button4 = customtkinter.CTkButton(master=frame, text="¿No tienes una cuenta?", command=sigButtonAction, width=220,
                                      height=38, compound="left", fg_color='#2b831a', text_color='white', hover_color='#15420b')
    button4.place(x=50, y=320)
    app.mainloop()  # running mainloop

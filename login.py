from libraries import customtkinter, ImageTk, Image, tkinter, pd


def login():
    userData = pd.read_csv('data/data.csv')
    df = pd.DataFrame(userData)
    email = df['correo']
    password = df['contraseña']
    user = entry1.get()
    pasw = entry2.get()
    matching_creds = (
        len(df[(df.correo == user) & (df.contraseña == pasw)]) > 0)
    if matching_creds:
        return True
    else:
        l4.configure(text_color='red')
        entry1.delete(0, 'end')
        entry1.focus()
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
        l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)  # placing label
        w.mainloop()  # running mainloop
    else:
        pass


app = customtkinter.CTk()  # creating cutstom tkinter window
app.geometry("500x530")
app.title('Login')
app.resizable(False, False)
app.eval('tk::PlaceWindow . center')
img1 = ImageTk.PhotoImage(Image.open(
    "images/pattern.png"))  # creating image object
l1 = customtkinter.CTkLabel(
    master=app, image=img1)  # creating custom label
l1.pack()  # placing label

# creating custom frame
frame = customtkinter.CTkFrame(
    master=l1, width=310, height=385, bg_color="#2b2b2b")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(
    master=frame, text="Sign Up", font=('Century Gothic', 30, 'bold'))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(
    master=frame, width=220, height=42, placeholder_text='Correo electrónico')
entry1.place(x=50, y=120)

entry2 = customtkinter.CTkEntry(
    master=frame, width=220, height=42, placeholder_text='Contraseña', show="*")
entry2.place(x=50, y=175)

l3 = customtkinter.CTkLabel(
    master=frame, text="¿Olvidaste tu contraseña?", font=('Century Gothic', 12))
l3.place(x=105, y=220)

# Create custom button
button1 = customtkinter.CTkButton(
    master=frame, width=220, height=38, text="Login", command=button_function, corner_radius=8, )
button1.place(x=50, y=255)

img2 = customtkinter.CTkImage(Image.open(
    "images/Google__G__Logo.svg.webp").resize((20, 20), Image.LANCZOS))
img3 = customtkinter.CTkImage(Image.open(
    "images/124010.png").resize((20, 20), Image.LANCZOS))
button2 = customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100,
                                  height=20, compound="left", fg_color='#252525', text_color='white', hover_color='#181a1b')
button2.place(x=50, y=320)

button3 = customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100,
                                  height=20, compound="left", fg_color='#252525', text_color='white', hover_color='#181a1b')
button3.place(x=170, y=320)
l4 = customtkinter.CTkLabel(
    master=frame, text="contraseña/correo invalido", font=('Century Gothic', 12), text_color='#2b2b2b')
l4.place(x=70, y=90)

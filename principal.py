from tkinter import messagebox
from tkinter.ttk import Combobox
from libraries import customtkinter,ImageTk, Image, tkinter
import pandas as pd
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
import random
import login

def homePage():
    w=customtkinter.CTk()
    w.geometry('1100x600')
    w.configure(bg='#262626')#12c4c0')
    w.resizable(0,0)
    w.title('Toggle Menu')

    def consejosverdes():
        consejos = ["Repara las fugas: una pequeña fuga en el grifo puede perder hasta 20 litros de agua al día. Asegúrate de reparar cualquier fuga lo antes posible.", "Cierra el grifo: mientras te lavas los dientes, te enjabonas o te afeitas, cierra el grifo. Esto puede ahorrar hasta 20 litros de agua por minuto.", "Dúchate en lugar de bañarte: tomar una ducha en lugar de un baño puede ahorrar hasta 80 litros de agua.", "Reutiliza el agua: el agua que usas para lavar la ropa o los platos puede reutilizarse para regar las plantas o para limpiar el suelo.", "Lava solo cargas completas: utiliza la lavadora y el lavavajillas solo cuando estén completamente llenos. Esto reduce la cantidad de ciclos que tienes que hacer y ahorra agua.", "Instala dispositivos de ahorro de agua: hay varios dispositivos que puedes instalar en tu hogar, como cabezales de ducha de bajo flujo, inodoros de doble descarga y grifos con aireadores que reducen el flujo de agua.", "Riega tus plantas temprano en la mañana o tarde en la noche: esto reduce la cantidad de agua que se evapora durante el día y asegura que las plantas absorban más agua.", "Usa una escoba en lugar de manguera para limpiar el patio o la entrada de tu casa.","No uses el inodoro como papelera: evita tirar objetos como toallitas húmedas, pañales o algodones en el inodoro, ya que esto aumenta el consumo de agua.", "Instala un tanque de agua de lluvia: recolecta agua de lluvia para regar tus plantas y lavar el coche.", "Usa plantas autóctonas en el jardín: las plantas autóctonas necesitan menos agua y son más resistentes al clima local.", "Usa agua de la piscina para regar el jardín: si tienes una piscina, usa el agua para regar las plantas cuando necesiten ser regadas.", "Lava tu coche con una cubeta: en lugar de utilizar una manguera, llena una cubeta con agua y utiliza una esponja para lavar tu coche.", "Instala un sistema de riego eficiente: utiliza sistemas de riego que sean eficientes y dirijan el agua directamente a las raíces de las plantas.", "Lava la ropa con agua fría: no solo ahorrarás agua, sino también energía al no tener que calentar el agua.", "Usa un vaso para cepillarte los dientes: en lugar de dejar el grifo abierto mientras te cepillas los dientes, utiliza un vaso para enjuagar tu boca.", "Educa a los niños: enséñales a los niños sobre la importancia de ahorrar agua y dale un buen ejemplo a seguir en casa"]
        consejo_aleatorio = random.choice(consejos)
        return consejo_aleatorio

    def default_home():
        f2=Frame(w,width=1100,height=600,bg='#262626')
        f2.place(x=50,y=0)
        df = pd.read_csv('data/database.csv')
        df = df.loc[df['email'] == login.user]
        l2=Label(f2,text='Consejos: ',fg='white',bg='#262626')
        l2.config(font=('',16))
        l2.place(x=60,y=10)

        lbienvenida = Label(f2,text='Bienvenido '+df['name'].values[0]+' '+df['lastname'].values[0],fg='white',bg='#262626')
        lbienvenida.config(font=('',16))
        lbienvenida.place(x=60,y=400)
        #funcion que reemplace el texto aleatorio del label
        def nuevo_consejo():
            lConsej.config(text=consejosverdes())
            

        #label que muestre el texto aleatorio
        lConsej = Label(f2, text=consejosverdes(), wraplength=300, justify=LEFT, fg='white',bg='#303030')
        lConsej.place(x=60,y=100)
        lConsej.config(font=('',12))

        l5 = Label(f2,text='Consumo de electricidad por KWH',fg='white',bg='#262626')
        l5.config(font=('',16))
        l5.place(x=400,y=10)
        
        #mostrar todos los KWHMonth
        t = Text(f2, height=20, width=30,bg='#303030',fg='white',font=('',12))
        t.config(wrap=WORD)
        #depositar los datos en el text
        for i in df.columns:
            if 'KWH' in i:
                t.insert(END, i+': '+str(df[i].values[0])+'\n')
  
        t.place(x=400,y=50)
        t.config(state=DISABLED)
        
        #boton que genere un texto aleatorio
        boton = Button(f2, text="Nuevo Consejo", command=lambda:nuevo_consejo())
        boton.place(x=60,y=50)
        
        l6 = Label(f2,text='Premios',fg='white',bg='#262626')
        l6.config(font=('',16))
        l6.place(x=800,y=10)
        
        texto = '''Estamos emocionados de anunciar nuestro nuevo programa de descuentos por consumo eléctrico. Ahora, al gastar una determinada cantidad de electricidad en kilovatios hora (kWh), podrás disfrutar de un descuento especial en tu factura. Cuanto más consumas, mayor será tu descuento.
            Nuestro programa de descuentos se divide en tres niveles, con sus respectivos umbrales y porcentajes de descuento:

            Nivel Bronce:
            Consumo mínimo requerido: 500 kWh
            Descuento: 5% de descuento en tu factura mensual.

            Nivel Plata:
            Consumo mínimo requerido: 1,000 kWh
            Descuento: 10% de descuento en tu factura mensual.

            Nivel Oro:
            Consumo mínimo requerido: 2,000 kWh
            Descuento: 15% de descuento en tu factura mensual.'''

        l7 = Label(f2,text=texto,wraplength=200,justify=LEFT,fg='white',bg='#262626')
        l7.config(font=('',10))
        l7.place(x=800,y=50)

    
    def home():
        f1.destroy()
        f2=Frame(w,width=1100,height=600,bg='#262626')
        f2.place(x=50,y=0)
        df = pd.read_csv('data/database.csv')
        df = df.loc[df['email'] == login.user]
        l2=Label(f2,text='Consejos: ',fg='white',bg='#262626')
        l2.config(font=('',16))
        l2.place(x=60,y=10)

        lbienvenida = Label(f2,text='Bienvenido '+df['name'].values[0]+' '+df['lastname'].values[0],fg='white',bg='#262626')
        lbienvenida.config(font=('',16))
        lbienvenida.place(x=60,y=400)
        #funcion que reemplace el texto aleatorio del label
        def nuevo_consejo():
            lConsej.config(text=consejosverdes())
            

        #label que muestre el texto aleatorio
        lConsej = Label(f2, text=consejosverdes(), wraplength=300, justify=LEFT, fg='white',bg='#303030')
        lConsej.place(x=60,y=100)
        lConsej.config(font=('',12))

        l5 = Label(f2,text='Consumo de electricidad por KWH',fg='white',bg='#262626')
        l5.config(font=('',16))
        l5.place(x=400,y=10)
        
        #mostrar todos los KWHMonth
        t = Text(f2, height=20, width=30,bg='#303030',fg='white',font=('',12))
        t.config(wrap=WORD)
        #depositar los datos en el text
        for i in df.columns:
            if 'KWH' in i:
                t.insert(END, i+': '+str(df[i].values[0])+'\n')
  
        t.place(x=400,y=50)
        t.config(state=DISABLED)
        
        #boton que genere un texto aleatorio
        boton = Button(f2, text="Nuevo Consejo", command=lambda:nuevo_consejo())
        boton.place(x=60,y=50)
        
        l6 = Label(f2,text='Premios',fg='white',bg='#262626')
        l6.config(font=('',16))
        l6.place(x=800,y=10)
        
        texto = '''Estamos emocionados de anunciar nuestro nuevo programa de descuentos por consumo eléctrico. Ahora, al gastar una determinada cantidad de electricidad en kilovatios hora (kWh), podrás disfrutar de un descuento especial en tu factura. Cuanto más consumas, mayor será tu descuento.
            Nuestro programa de descuentos se divide en tres niveles, con sus respectivos umbrales y porcentajes de descuento:

            Nivel Bronce:
            Consumo mínimo requerido: 500 kWh
            Descuento: 5% de descuento en tu factura mensual.

            Nivel Plata:
            Consumo mínimo requerido: 1,000 kWh
            Descuento: 10% de descuento en tu factura mensual.

            Nivel Oro:
            Consumo mínimo requerido: 2,000 kWh
            Descuento: 15% de descuento en tu factura mensual.'''

        l7 = Label(f2,text=texto,wraplength=200,justify=LEFT,fg='white',bg='#262626')
        l7.config(font=('',10))
        l7.place(x=800,y=50)

        toggle_win()

    def dashboard():
        f1.destroy()
        f2=Frame(w,width=1000,height=600,bg='#262626')
        f2.place(x=50,y=0)
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

        df = pd.read_csv('data/database.csv')
        # encontrar usuario según email
        df = df.loc[df['email'] == login.user]
        # filtrar los datos que la cabecera empieza por KWH
        df = df.filter(regex='^KWH', axis=1)\
            # Obtener los nombres de columna sin el prefijo "KWH"
        column_names = df.columns.str.replace('KWH', '')
        # Convertir los nombres de columna a formato de mes
        column_names = pd.to_datetime(column_names, format='%B', errors='coerce').strftime('%B')

        # Crear una figura y un eje
        fig1, ax1 = plt.subplots(figsize=(11, 5), dpi=100)
        ax1.plot(column_names, df.values[0])


        charts_frame = Frame(f2)
        charts_frame.pack()
        upper_frame = (charts_frame)
        upper_frame.pack(fill="both", expand=True)
        canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)
        toggle_win()
    
    def ingresar():
        
        #agreagar KWHMonth depnediendo dle mes seleccionado en el combobox 
        def agregar():
            df = pd.read_csv('data/database.csv')
            df = df.loc[df['email'] == login.user]
            df['KWH'+n.get()] = int(kwh.get())
            #no agregar el mes solo el dato
            df.to_csv('data/database.csv',index=False)
            messagebox.showinfo(message='KWH agregado con exito', title='Exito')
        

            toggle_win()

        f1.destroy()
        f2 = Frame(w, width=1100, height=600, bg='#262626')
        f2.place(x=50,y=0)
        
        df = pd.read_csv('data/database.csv')
        df = df.loc[df['email'] == login.user]
        
        n = StringVar()
        monthchoosen = Combobox(f2, width = 27, textvariable = n)
        
        # Adding combobox drop down list
        monthchoosen['values'] = ('January', 
                                'February',
                                'March',
                                'April',
                                'May',
                                'June',
                                'July',
                                'August',
                                'September',
                                'October',
                                'November',
                                'December')
        
        monthchoosen.grid(column = 1, row = 5)
        monthchoosen.current()
        monthchoosen.place(x=400, y=50)
        
        l2 = Label(f2, text='Mes: ', fg='white', bg='#262626')
        l2.config(font=('', 12))
        l2.place(x=400, y=20)
        
        l3 = Label(f2, text='KWH: ', fg='white', bg='#262626')
        l3.config(font=('', 12))
        l3.place(x=400, y=80)

        kwh = Entry(f2, width=30)
        kwh.place(x=400, y=100)

        submitButton = Button(f2, text='Agregar', command=agregar)
        submitButton.place(x=400, y=130)



        toggle_win()


    def verpefil():
        f1.destroy()
        f2=Frame(w,width=1100,height=600,bg='#262626')
        f2.place(x=50,y=0)
        df = pd.read_csv('data/database.csv')
        df = df.loc[df['email'] == login.user]
        l2 = Label(f2,text='Nombre: '+df['name'].values[0],fg='white',bg='#262626')
        l2.config(font=('',12))
        l2.place(x=400,y=50)
        l3 = Label(f2,text='Apellido: '+df['lastname'].values[0],fg='white',bg='#262626')
        l3.config(font=('',12))
        l3.place(x=400,y=70)
        l4 = Label(f2,text='Email: '+df['email'].values[0],fg='white',bg='#262626')
        l4.config(font=('',12))
        l4.place(x=400,y=90)
        l5 = Label(f2,text='Consumo de electricidad por KWH',fg='white',bg='#262626')
        l5.config(font=('',12))
        l5.place(x=400,y=120)
        #mostrar todos los KWHMonth
        t = Text(f2, height=20, width=30,bg='#303030',fg='white',font=('',12))
        t.config(wrap=WORD)
        #depositar los datos en el text
        for i in df.columns:
            if 'KWH' in i:
                t.insert(END, i+': '+str(df[i].values[0])+'\n')
  
        t.place(x=400,y=150)
        t.config(state=DISABLED)
    

        toggle_win()   
        

    def toggle_win():
        global f1
        f1=Frame(w,width=300,height=600,bg='#12c4c0')
        f1.place(x=0,y=0)
        
        #buttons
        def bttn(x,y,text,bcolor,fcolor,cmd):
        
            def on_entera(e):
                myButton1['background'] = bcolor #ffcc66
                myButton1['foreground']= '#262626'  #000d33

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground']= '#262626'

            myButton1 = Button(f1,text=text,
                        width=42,
                        height=2,
                        fg='#262626',
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,            
                            command=cmd)
                        
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x,y=y)

        bttn(0,80,'H O M E','#0f9d9a','#12c4c0',home)
        bttn(0,117,'D A S H B O A R D','#0f9d9a','#12c4c0',dashboard)
        bttn(0,154,'I N G R E S A R   D A T O S','#0f9d9a','#12c4c0',ingresar)
        bttn(0,191,'P E R F I L','#0f9d9a','#12c4c0',verpefil)

        #
        def dele():
            f1.destroy()
            b2=Button(w,image=img1,
                command=toggle_win,
                border=0,
                bg='#262626',
                activebackground='#262626')
            b2.place(x=5,y=8)

        global img2
        img2 = Image.open("images/close.png")
        img2 = img2.resize((40,40),Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        Button(f1,
            image=img2,
            border=0,
            command=dele,
            bg='#12c4c0',
            activebackground='#12c4c0').place(x=5,y=10)



    default_home()
    img1 = Image.open("images/open.png")
    img1 = img1.resize((40,40),Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)

    global b2
    b2=Button(w,image=img1,
        command=toggle_win,
        border=0,
        bg='#262626',
        activebackground='#262626')
    b2.place(x=5,y=8)


    w.mainloop()


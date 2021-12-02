from tkinter import*
from PIL import Image, ImageTk
import api
import pip._vendor.requests


class MYWeatherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WEATHER DETECTION  GUI APP")
        self.root.geometry("350x350+550+250")
        self.root.config(bg="white")

        # ====SEARCH ICON====

        self.search_icon = Image.open("icons/searchimage.png")
        self.search_icon = self.search_icon.resize((30, 30), Image.ANTIALIAS)
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        # ====SEARCH VARIABLE====

        self.var_search = StringVar()

        title = Label(self.root, text="WEATHER APP", font=("Sigorta", 25, "bold"), bg="black", fg="red").place(x=0, y=0, relwidth=1, height=60)
        lbl_city = Label(self.root, text="City Name", font=("Al Nile", 15), bg="green",fg="white", anchor="w", padx=5).place(x=0, y=60, relwidth=1, height=40)
        lbl_city = Entry(self.root, textvariable=self.var_search, font=("Al Nile", 15), bg="lightyellow", fg="#262626").place(x=100, y=68, width=200, height=25)
        btn_search = Button(self.root, cursor="hand2", image=self.search_icon, activebackground="red",command=self.get_weather).place(x=310, y=65, width=30, height=30)

        self.lbl_city = Label(self.root,font=("Al Nile", 13), bg="white", fg="green")
        self.lbl_city.place(x=0, y=111, relwidth=1, height=30)

        self.lbl_icons = Label(self.root,font=("Al Nile", 13), bg="white", fg="blue")
        self.lbl_icons.place(x=0, y=135, relwidth=1, height=100)

        self.lbl_temperature = Label(self.root,font=("Al Nile", 13), bg="white", fg="brown")
        self.lbl_temperature.place(x=0, y=220, relwidth=1, height=20)

        self.lbl_description = Label(self.root,font=("Al Nile", 13), bg="white", fg="black")
        self.lbl_description.place(x=0, y=250, relwidth=1, height=20)

        self.lbl_error = Label(self.root,font=("Al Nile", 12), bg="white", fg="dark green")
        self.lbl_error.place(x=0, y=270, relwidth=1, height=40)

        # ====FOOTER====
        lbl_footer = Label(self.root, text="HAVE A GREAT DAY", font=("Sigorta", 12), bg="blue", fg="white", pady=5).pack(side=BOTTOM, fill=X)

    def get_weather(self):

        api_key = api.api_key
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        # CITY NAME,COUNTRY NAME,ICONS,TEMPERATURE(C),TEMPERATURE(F),WIND
        if self.var_search.get() == "":
            self.lbl_city.config(text="")
            self.lbl_icons.config(image="")
            self.lbl_temperature.config(text="")
            self.lbl_description.config(text="")
            self.lbl_error.config(text="CITY NAME REQUIRED")
        
        else:
            result = pip._vendor.requests.get(complete_url)
            if result:
                json = result.json()
                city_name = json["name"]
                country_name = json["sys"]["country"]
                json = result.json()
                city_name = json["name"]
                country_name = json["sys"]["country"]
                icons = json["weather"][0]["icon"]
                temp_c = json["main"]["temp"]-273.15
                temp_f = (json["main"]["temp"]-273.15)*9/5+32
                description = json["weather"][0]["main"]

                self.lbl_city.config(text=city_name+" , "+country_name)

            # ====NEW ICONS====

                self.search_icon2 = Image.open(f"icons/{icons}.png")
                self.search_icon2 = self.search_icon2.resize((100, 100), Image.ANTIALIAS)
                self.search_icon2 = ImageTk.PhotoImage(self.search_icon2)

                self.lbl_icons.config(image=self.search_icon2)

                deg = u"\N{DEGREE SIGN}"
                self.lbl_temperature.config(text=str(round(temp_c,2))+deg+"C | "+str(round(temp_f,2))+deg+" F")
                self.lbl_description.config(text=description)

                self.lbl_error.config(text="")

            else:
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temperature.config(text="")
                self.lbl_description.config(text="")
                self.lbl_error.config(text="INVALID CITY NAME")

    


root = Tk()
obj = MYWeatherGUI(root)
root.mainloop()

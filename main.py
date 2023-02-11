import bleak
import asyncio
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import asyncio
from bleak import BleakScanner
import sqlite3

async def scan():
    async with BleakScanner() as scanner:
        devices = await scanner.discover()
        return devices

asyncio.run(scan())
Window.size = (360, 580)
database = sqlite3.connect("database.db")
cr = database.cursor()

global dirction
dirction = {
    "left": "images/left-arrow.png",
    "right": "images/right-arrow.png",
    "up": "images/up-arrow.png",
    "down": "images/down-arrow.png"
}
global cs_dirction
cs_dirction = {
    "cs_1": "left",
    "cs_2": "right"
}

class MainApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        self.title = 'IPS ArRass college'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        screen_manager.add_widget(Builder.load_file("track.kv"))
        screen_manager.add_widget(Builder.load_file("welcome_page.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        # screen_manager.add_widget(Builder.load_file("track.kv"))
        screen_manager.add_widget(Builder.load_file("map.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("main_guest.kv"))
        screen_manager.add_widget(Builder.load_string("MDScreen:
    name: 'faculty_page'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDLabel:
            text: "Departments"
            font_size: "26sp"
            pos_hint: {"center_x": 0.75, "center_y": .95}
            color: rgba(0, 0, 0, 255)
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "main"

        MDFloatLayout:
            size_hint: .9, .07
            pos_hint: {"center_x": .48, "center_y": .73}
            MDLabel:
                text: "Computer Department"
                font_size: "16sp"
                pos_hint: {"center_x": 0.48, "center_y": .85}
                color: rgba(0, 0, 0, 255)
            MDIconButton:
                icon: "arrow-down"
                theme_icon_color: "Custom"
                pos_hint: {"center_x": 0.86, "center_y": .85}
                user_font_size: "30sp"
                text_color: rgba(26, 24, 58, 255)

            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)

        MDFloatLayout:
            size_hint: .9, .07
            pos_hint: {"center_x": .48, "center_y": .63}
            MDLabel:
                text: "Physics Department"
                font_size: "16sp"
                pos_hint: {"center_x": 0.48, "center_y": .85}
                color: rgba(0, 0, 0, 255)
            MDIconButton:
                icon: "arrow-down"
                theme_icon_color: "Custom"
                pos_hint: {"center_x": 0.86, "center_y": .85}
                user_font_size: "30sp"
                text_color: rgba(26, 24, 58, 255)

            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)

        MDFloatLayout:
            size_hint: .9, .07
            pos_hint: {"center_x": .48, "center_y": .53}
            MDLabel:
                text: "Chemistry Department"
                font_size: "16sp"
                pos_hint: {"center_x": 0.48, "center_y": .85}
                color: rgba(0, 0, 0, 255)
            MDIconButton:
                icon: "arrow-down"
                theme_icon_color: "Custom"
                pos_hint: {"center_x": 0.86, "center_y": .85}
                user_font_size: "30sp"
                text_color: rgba(26, 24, 58, 255)

            MDFloatLayout:
                pos_hint: {"center_x": .45, "center_y": 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)

<MagicButton@MagicBehavior+Button>:
    text:root.text
    size_hint: .5, .065
    pos_hint: {"center_x": .5, "center_y": .34}
    background_color: 0, 0, 0, 0
    on_press:
        root.on_press
    canvas.before:
        Color:
            rgb: rgba(52, 0, 231, 255)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [5]


"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("information.kv"))
        return screen_manager

    def signup_data(self):
        signup_email = self.root.get_screen("signup").ids.signup_email.text
        signup_password = self.root.get_screen("signup").ids.signup_password.text
        signup_confirm_password = self.root.get_screen("signup").ids.signup_confirm_password.text
        if signup_password == signup_confirm_password:
            cr.execute(f"INSERT INTO users(email, password) values('{signup_email}', '{signup_password}')")
            database.commit()

    def login_data(self):
        login_email = self.root.get_screen("login").ids.login_email.text
        login_password = self.root.get_screen("login").ids.login_password.text
        print(login_email)
        print(login_password)
        self.log = login_email

    def edit_data(self):

        office_hours = self.root.get_screen("information").ids.office_hours.text
        office_location = self.root.get_screen("information").ids.office_location.text
        department = self.root.get_screen("information").ids.department.text
        cr.execute(f"UPDATE users set office_hours = '{office_hours}' WHERE email = '{self.log}'")
        cr.execute(f"UPDATE users set office_location = '{office_location}' WHERE email = '{self.log}'")
        database.commit()

    # async def scan(self, beacon):
    #     while True:
    #         scanned_devices = await bleak.BleakScanner.discover(1)
    #         for device in scanned_devices:
    #             if device.name == beacon:
    #                 return beacon
    #
    # def tracking(self):
    #     for i in range(90):
    #         if i % 2 == 0:
    #             self.root.get_screen("track").ids.source = dirction["up"]
    #         else:
    #             self.root.get_screen("track").ids.source = dirction["down"]


if __name__ == "__main__":
    MainApp().run()
    database.close()


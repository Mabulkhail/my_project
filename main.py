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
        screen_manager.add_widget(Builder.load_file("faculty_page.kv"))
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


import imp
import os

from kivy.lang import Builder

from kivymd.uix.screen import MDScreen

#Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "callscreen", "uix", "screens", "kv", "callscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen(MDScreen):
    pass
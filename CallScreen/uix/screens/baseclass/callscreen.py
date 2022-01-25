import imp
import os
from turtle import title
import kivy

from kivy.lang import Builder

from kivymd.uix.screen import MDScreen

from kivy.animation import Animation

from kivy.properties import NumericProperty

#Читаем и загружаем KV файл
with open(os.path.join(os.getcwd(), "uix", "screens", "kv", "callscreen.kv"), encoding="utf-8") as KV:
    Builder.load_string(KV.read())


class CallScreen(MDScreen):
    blur_value = NumericProperty(0)

    open_call_box = False

    def animation_title_image(self, title_image):
        """
        :type title_image: <kivymd.utils.fitimage.FitImage object>
        """

        if not self.open_call_box:
            Animation(size_hint_y=1, d=0.6, t="in_out_quad").start(title_image)
        else:
            Animation(size_hint_y=0.45, d=0.6, t="in_out_quad").start(title_image)

    def animation_blur_value(self):
        if not self.open_call_box:
            Animation(blur_value=15, d=0.6, t="in_out_quad").start(self)
        else:
            Animation(blur_value=0, d=0.6, t="in_out_quad").start(self)
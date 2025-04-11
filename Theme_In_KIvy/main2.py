from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ColorProperty
from kivy.event import EventDispatcher


# --------------------------
# Theme Class
# --------------------------

class Theme(EventDispatcher):
    primary_color = ColorProperty([1, 1, 1, 1])
    secondary_color = ColorProperty([0.5, 0.5, 0.5, 1])
    background_color = ColorProperty([0, 0, 0, 1])
    text_color = ColorProperty([1, 1, 1, 1])
    accent_color = ColorProperty([1, 0.5, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_light_theme(self):
        self.primary_color = [1, 1, 1, 1]
        self.secondary_color = [0.9, 0.9, 0.9, 1]
        self.background_color = [1, 1, 1, 1]
        self.text_color = [0, 0, 0, 1]
        self.accent_color = [0.2, 0.6, 0.86, 1]

    def set_dark_theme(self):
        self.primary_color = [0.1, 0.1, 0.1, 1]
        self.secondary_color = [0.2, 0.2, 0.2, 1]
        self.background_color = [0.05, 0.05, 0.05, 1]
        self.text_color = [1, 1, 1, 1]
        self.accent_color = [0.9, 0.3, 0.1, 1]


# --------------------------
# Themed Widget Inheriting Theme
# --------------------------

class ThemedBox(BoxLayout, Theme):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.label = Label(text="Hello Theme!", font_size=24)
        self.button = Button(text="Toggle Theme", size_hint_y=None, height=50)

        self.add_widget(self.label)
        self.add_widget(self.button)

        self.button.bind(on_press=self.toggle_theme)

        self.bind(
            primary_color=self.update_theme,
            text_color=self.update_theme,
            background_color=self.update_theme,
            accent_color=self.update_theme,
        )

        self.set_light_theme()
        self.update_theme()

    def update_theme(self, *args):
        self.label.color = self.text_color
        self.button.background_color = self.accent_color
        self.button.color = self.text_color

        self.canvas.before.clear()
        with self.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*self.background_color)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        if hasattr(self, 'bg_rect'):
            self.bg_rect.pos = self.pos
            self.bg_rect.size = self.size

    def toggle_theme(self, *args):
        if self.background_color[0] > 0.5:
            self.set_dark_theme()
        else:
            self.set_light_theme()


# --------------------------
# App
# --------------------------

class ThemeApp(App):
    def build(self):
        return ThemedBox()

if __name__ == "__main__":
    ThemeApp().run()

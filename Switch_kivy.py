from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ColorProperty
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.animation import Animation
from kivy.metrics import dp


class CustomSwitch(ToggleButtonBehavior, Widget):
    thumb_color = ColorProperty([1, 1, 1, 1])
    on_color = ColorProperty([0.3, 0.8, 0.4, 1])
    off_color = ColorProperty([0.6, 0.6, 0.6, 1])
    bg_color = ColorProperty([0.6, 0.6, 0.6, 1])

    def __init__(self, **kwargs):
        self.register_event_type('on_active')  # Register custom event
        super().__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (dp(60), dp(32))
        self.thumb_size = dp(26)

        with self.canvas:
            # Background track
            self.bg_color_instr = Color(rgba=self.bg_color)
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(16)])

            # Thumb
            self.thumb_color_instr = Color(rgba=self.thumb_color)
            self.thumb = Ellipse(size=(self.thumb_size, self.thumb_size), pos=self._thumb_off())

        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.bind(state=self.on_state)

    def _thumb_off(self):
        return (self.x + dp(3), self.y + (self.height - self.thumb_size) / 2)

    def _thumb_on(self):
        return (self.right - self.thumb_size - dp(3), self.y + (self.height - self.thumb_size) / 2)

    def on_state(self, instance, value):
        is_on = value == 'down'

        # Animate thumb and color
        Animation(pos=self._thumb_on() if is_on else self._thumb_off(), duration=0.2).start(self.thumb)
        self.bg_color = self.on_color if is_on else self.off_color
        self.bg_color_instr.rgba = self.bg_color

        # Fire the custom event
        self.dispatch('on_active', is_on)

    def update_graphics(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.thumb.pos = self._thumb_on() if self.state == 'down' else self._thumb_off()

    def on_active(self, active_state):
        """Event that can be bound from outside. `active_state` is True or False."""
        pass


class TestApp(App):
    def build(self):
        root = FloatLayout()
        switch = CustomSwitch(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        switch.bind(on_active=self.on_switch_change)
        root.add_widget(switch)
        return root

    def on_switch_change(self, instance, value):
        print(" Switch is ON" if value else "Switch is OFF")


if __name__ == "__main__":
    TestApp().run()

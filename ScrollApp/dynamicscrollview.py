#from kivy.config import Config
#Config.set('graphics', 'show_fps', '1')
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DynamicScrollView(ScrollView):
    def __init__(self, create_widget_fn, item_count, item_height=dp(80), buffer=5, spacing=dp(5), **kwargs):
        super().__init__(**kwargs)
        self.create_widget_fn = create_widget_fn
        self.item_count = item_count
        self.item_height = item_height
        self.buffer = buffer
        self.spacing = spacing
        self.step = self.item_height + self.spacing

        self.visible_indices = set()
        self.widget_pool = {}     # index -> widget
        self.free_pool = []       # recycled widgets

        # Inner layout
        self.container = FloatLayout(size_hint_y=None)
        self.container.height = self.item_count * self.step
        self.add_widget(self.container)

        self.bind(scroll_y=self.update_visible)
        self.bind(size=self.update_visible)
        self.bind(width=self.resize_items)

    def update_visible(self, *args):
        scroll_height = self.height
        content_height = self.container.height
        scroll_y = self.scroll_y

        bottom = (1 - scroll_y) * (content_height - scroll_height)
        top = bottom + scroll_height

        first = max(int(bottom // self.step) - self.buffer, 0)
        last = min(int(top // self.step) + self.buffer, self.item_count - 1)

        new_indices = set(range(first, last + 1))

        # Recycle old ones
        for i in self.visible_indices - new_indices:
            widget = self.widget_pool.pop(i, None)
            if widget:
                self.container.remove_widget(widget)
                self.free_pool.append(widget)

        inner_width = self.width

        # Show new ones
        for i in new_indices - self.visible_indices:
            if i in self.widget_pool:
                continue

            if self.free_pool:
                widget = self.free_pool.pop()
                widget.text = f"Item {i}"
            else:
                widget = self.create_widget_fn(i)

            widget.size_hint = (None, None)
            widget.height = self.item_height
            widget.width = inner_width
            y = content_height - (i + 1) * self.step
            widget.pos = (0, y)

            self.container.add_widget(widget)
            self.widget_pool[i] = widget

        self.visible_indices = new_indices

    def resize_items(self, *args):
        for widget in self.widget_pool.values():
            widget.width = self.width


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        def make_widget(index):
            return Button(
                text=f"Item {index}",
                font_size=20,
                color=(0, 1, 0, 1),
                halign='left',
                valign='middle',
            )

        self.scroll = DynamicScrollView(
            create_widget_fn=make_widget,
            item_count=5000,
            item_height=dp(60),
            spacing=dp(5),
            buffer=5
        )
        self.add_widget(self.scroll)


class ScrollApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    ScrollApp().run()

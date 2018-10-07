from kivy.uix.button import Button
from random import random
from kivy.app import App
from kivy.graphics import Color, Ellipse,Line
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1, 1)  # 设置圆形颜色
        with self.canvas:
            Color(*color, mode='hsv')
            d = 1 # 设置圆形直径
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            print(touch.ud['line'].points)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self,obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()

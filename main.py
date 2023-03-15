import random
import threading

import pyglet


class App(pyglet.window.Window):
    def __init__(self):
        super(App, self).__init__(500, 500)
        self.batch = pyglet.graphics.Batch()
        self.blue = pyglet.shapes.Rectangle(0, 0, 250, 250, batch=self.batch, color=(0, 0, 255, 255))
        self.bluet = pyglet.text.Label()
        self.yellow = pyglet.shapes.Rectangle(250, 0, 250, 250, batch=self.batch, color=(255, 255, 0, 255))
        self.red = pyglet.shapes.Rectangle(250, 250, 250, 250, batch=self.batch, color=(255, 0, 0, 255))
        self.green = pyglet.shapes.Rectangle(0, 250, 250, 250, batch=self.batch, color=(0, 255, 0, 255))
        self.audioThread: threading.Thread = None
        self.elapsed = 15
        self.freq = 0
        self.guess = 0

    def render(self, dt):
        self.batch.draw()
        if self.elapsed >= 15:
            self.freq = random.choice([400, 1000, 5000, 15000])
            if random.random() < 0.5:
                self.freq = random.random() * 14800 + 200

            pyglet.media.synthesis.Sine(15, self.freq).play()
            self.elapsed = 0
        self.elapsed += dt

    def on_mouse_press(self, x, y, button, modifiers):
        if x < 250:
            if y < 250:
                self.bluep()
            else:
                self.greenp()
        else:
            if y < 250:
                self.yellowp()
            else:
                self.redp()
        if self.guess == self.freq:
            print('Correct')
        else:
            print(f"Incorrect: {self.freq}")
        self.elapsed = 10

    def on_mouse_release(self, x, y, button, modifiers):
        self.blue.color = (0, 0, 255, 255)
        self.red.color = (255, 0, 0, 255)
        self.yellow.color = (255, 255, 0, 255)
        self.green.color = (0, 255, 0, 255)

    def greenp(self):
        self.green.color = (0, 100, 0, 255)
        self.guess = 400

    def redp(self):
        self.red.color = (100, 0, 0, 255)
        self.guess = 1000

    def bluep(self):
        self.blue.color = (0, 0, 100, 255)
        self.guess = 5000

    def yellowp(self):
        self.yellow.color = (100, 100, 0, 255)
        self.guess = 15000


if __name__ == '__main__':
    app = App()
    pyglet.clock.schedule(app.render)
    pyglet.app.run()

# 75% chance of known

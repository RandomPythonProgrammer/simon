import random
import threading

import pyglet


class App(pyglet.window.Window):
    def __init__(self):
        super(App, self).__init__(500, 500)
        self.batch = pyglet.graphics.Batch()

        self.green = pyglet.shapes.Rectangle(0, 250, 250, 250, batch=self.batch, color=(0, 255, 0, 255))
        self.greent = pyglet.text.Label(text='400', x=0, y=250, batch=self.batch, color=(0, 0, 0, 255))

        self.red = pyglet.shapes.Rectangle(250, 250, 250, 250, batch=self.batch, color=(255, 0, 0, 255))
        self.redt = pyglet.text.Label(text='1000', x=250, y=250, batch=self.batch, color=(0, 0, 0, 255))

        self.blue = pyglet.shapes.Rectangle(0, 0, 250, 250, batch=self.batch, color=(0, 0, 255, 255))
        self.bluet = pyglet.text.Label(text='5000', x=0, y=0, batch=self.batch, color=(0, 0, 0, 255))

        self.yellow = pyglet.shapes.Rectangle(250, 0, 250, 250, batch=self.batch, color=(255, 255, 0, 255))
        self.yellowt = pyglet.text.Label(text='10000', x=250, y=0, batch=self.batch, color=(0, 0, 0, 255))

        self.audioThread: threading.Thread = None
        self.elapsed = 15
        self.freq = None
        self.guess = None

        self.player = pyglet.media.player.Player()

    def render(self, dt):
        self.batch.draw()
        if self.elapsed >= 7:
            if self.guess is None and self.freq is not None and self.freq not in [400, 1000, 5000, 10000]:
                print(f"Correct (Not in set): {self.freq}")
            elif self.guess is None and self.freq in [400, 1000, 5000, 10000]:
                print(f"Incorrect (In set): {self.freq}")
            self.guess = None
            self.freq = random.choice([400, 1000, 5000, 10000])
            if random.random() < 0.25:
                self.freq = random.choice(range(0, 10000, 500))

            self.player.queue(pyglet.media.synthesis.Sine(3, self.freq))
            self.player.play()
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
        self.elapsed = 5

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
        self.guess = 10000


if __name__ == '__main__':
    app = App()
    pyglet.clock.schedule(app.render)
    pyglet.app.run()

# 75% chance of known

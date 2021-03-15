import random
import tkinter as tk


class ColorGame:
    def __init__(self):
        # Create widgets
        self.root = tk.Tk()
        self.score = 0
        self.timer = 10
        self.color = ''
        self.label_condition = tk.Label(self.root, text='Type in the colour of the word,'
                                                        ' and not of the word text.',
                                        font=10)
        self.label_enter = tk.Label(text='Press the "Start" to start the game.')

        self.label_score = tk.Label(text='Score: ' + str(self.score))

        self.label_time = tk.Label(self.root, text='Time left: ' + str(self.timer))

        self.message = tk.Label()

        self.text_entry = tk.Entry(self.root)

        self.show_widgets()

    def show_widgets(self):
        self.label_condition.pack()
        self.label_enter.pack()
        self.label_score.pack()
        self.label_time.pack()
        self.message.pack()
        self.text_entry.pack()
        self.root.bind('<Return>', self.enter_click)
        self.text_entry.focus_set()

    def random_color(self):
        colors = ['red',
                  'green',
                  'black',
                  'orange',
                  'purple',
                  'yellow',
                  'pink']
        random_color = random.choice(colors)
        if self.timer != 0:
            self.message.config(fg=random_color,
                                text=random.choice(colors),
                                font=15)
            self.color = random_color
        else:
            pass

    def next_color(self):
        answer = self.text_entry.get().lower()
        if answer == self.color and answer != '' and self.timer != 0:
            self.score += 1
            self.label_score.config(text='Score: ' + str(self.score))
            self.text_entry.delete(0, tk.END)
        self.random_color()

    def clock(self):
        if self.timer > 0:
            self.timer -= 1
            self.label_time.config(text='Time left: ' + str(self.timer))
            self.root.after(1000, self.clock)
        else:
            self.message.config(text="Game over")

    def enter_click(self, event):
        if self.timer == 10:
            self.clock()
        self.next_color()

    def main_loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = ColorGame()
    app.main_loop()


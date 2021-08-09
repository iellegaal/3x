from tkinter import *
import random

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        x1, y1 = (400, 0)
        x2, y2 = (400, 0)
        canvas.create_line(x1, y1, x2, y2)
        for i in range(50):
            randx = random.randint(10, 25)
            randy = random.randint(10, 25)
            x1, y1 = x2, y2
            if randx % 2 == 0:
                x2, y2 = x1 - randx, y1 + randy
            else:
                x2, y2 = x1 + randx, y1 + randy
            canvas.create_line(x1, y1, x2, y2)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    rows = 1000
    columns = 1000
    root.geometry(f"{rows}x{columns}")
    root.mainloop()


if __name__ == '__main__':
    main()
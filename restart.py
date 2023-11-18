import turtle

scr = turtle.Screen()


class Restart(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.take_input = None
        self.hideturtle()

    def restart_game(self):
        self.take_input = scr.textinput(title="Do you wanna restart? ", prompt="press 'y' to restart or 'n' to exit")
        print(self.take_input)

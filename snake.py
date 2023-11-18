import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []
        self.make_blocks()
        self.head = self.blocks[0]

    def make_blocks(self):
        for position in STARTING_POSITIONS:  # postion contains two value i.e. from the tuple STARTING_POSITION
            self.add_block(position)

    def add_block(self, position):
        new_block = t.Turtle()
        new_block.pu()
        new_block.color("white")
        new_block.shape("square")
        new_block.setpos(position)
        self.blocks.append(new_block)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def reset_snake(self):
        for seg in self.blocks:
            seg.goto(1000, 1000)
        self.blocks.clear()
        self.make_blocks()
        self.head =self.blocks[0]

    def move(self):
        for seg in range(len(self.blocks) - 1, 0, -1):
            hold_x = self.blocks[seg - 1].xcor()
            hold_y = self.blocks[seg - 1].ycor()
            self.blocks[seg].setpos(x=hold_x, y=hold_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

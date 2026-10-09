from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def move(self):
        next_position = None
        for segment in self.segments:
            current_position = segment.position()
            if next_position is None:
                segment.forward(MOVE_DISTANCE)
            else:
                segment.goto(next_position)
            next_position = current_position



    def right(self):
        orientation = self.segments[0].heading()
        if orientation == 180:
            return
        self.head.setheading(0)

    def left(self):
        orientation = self.segments[0].heading()
        if orientation == 0:
            return
        self.head.setheading(180)

    def up(self):
        orientation = self.segments[0].heading()
        if orientation == 270:
            return
        self.head.setheading(90)

    def down(self):
        orientation = self.segments[0].heading()
        if orientation == 90:
            return
        self.head.setheading(270)
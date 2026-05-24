from manim import *
from typing import override


class CreateCircle(Scene):
    @override
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency
        self.play(Create(circle))  # animate the creation of the circle


import random


class Hat:

    def __init__(self, **balls):
        self.balls = balls
        contents = list()
        for i in balls:
            for n in range(balls[f"{i}"]):
                contents.append(i)
        self.contents = contents

    def draw(self, num):
        drew_balls = list()
        print(self.contents)
        remaining_balls = self.contents
        if num > len(self.contents):
            drew_balls = self.contents
            remaining_balls = []
        else:
            for n in range(num):
                drew_ball = random.choice(remaining_balls)
                drew_balls.append(drew_ball)
                remaining_balls.remove(drew_ball)

        return drew_balls


import random
import copy


class Hat:

    def __init__(self, **balls):
        self.balls = balls
        contents = list()
        for i in balls:
            for n in range(balls[f"{i}"]):
                contents.append(i)
        self.contents = contents

    def draw(self, num):
        drawn_balls = list()
        remaining_balls = self.contents
        if num > len(self.contents):
            drawn_balls = self.contents
            remaining_balls = []
        else:
            for n in range(num):
                drawn_ball = random.choice(remaining_balls)
                drawn_balls.append(drawn_ball)
                remaining_balls.remove(drawn_ball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0  # number of wins
    N = 0  # number of performed experiments

    for n in range(num_experiments):
        hat_o = copy.deepcopy(hat)
        e_drawn_balls = hat_o.draw(num_balls_drawn)
        condition = []
        for color in expected_balls:

            c = e_drawn_balls.count(color)
            if expected_balls[color] <= c:
                condition.append('+')
            else:
                condition.append('-')

        if '-' in condition:
            M = M
        else:
            M = M + 1
        N = N + 1


    return M/N

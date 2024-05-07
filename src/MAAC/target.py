from math import cos, sin, pi
import random

dt = 0.1


class TARGET:
    def __init__(self, x0: float, y0: float, h0: float, a0: float, v_max: float = 50, h_max: float = pi / 6):
        """
        :param x0: scalar
        :param y0: scalar
        :param h0: scalar
        :param v_max: scalar
        :param h_max: scalar
        """
        # the position, velocity and heading of this uav
        self.x = x0
        self.y = y0
        self.h = h0
        self.v_max = v_max

        # the max heading angular rate and the action of this uav
        self.h_max = h_max
        self.a = a0

    def update_position(self, x_max, y_max) -> (float, float, float):
        """
        receive the action (heading angular rate), then update the current position
        :param y_max:
        :param x_max:
        :return:
        """
        self.a = random.uniform(-self.h_max, self.h_max)
        dx = dt * self.v_max * cos(self.h)  # x 方向位移
        dy = dt * self.v_max * sin(self.h)  # y 方向位移
        self.x += dx
        self.y += dy

        if self.x > x_max:
            self.x = x_max
        if self.x < 0:
            self.x = 0

        if self.y > y_max:
            self.y = y_max
        if self.y < 0:
            self.y = 0

        self.h += dt * self.a  # 更新朝向角度
        self.h = (self.h + pi) % (2 * pi) - pi  # 确保朝向角度在 [-pi, pi) 范围内

        return self.x, self.y
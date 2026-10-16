import time
import math
from lib import puzz_msgs
import numpy as np


class DeadReckoning:
    def __init__(self):
        self.pose = [0.0, 0.0, 0.0]   # [x, y, theta]

        self.k = 0.1                 # wheel noise coefficient

        self.w_r = 0.0
        self.w_l = 0.0

        self.R = 0.05                # wheel radius [m]
        self.L = 0.09                # wheel base [m] (coursework spec)

        self.Sig = np.zeros((3, 3))

        self.t_start = time.time()

    def spin(self, topics):

        dt = time.time() - self.t_start
        self.t_start = time.time()
        if dt <= 0:
            return topics

        # Read wheel speeds
        if "VelocityEncR" in topics:
            self.w_r = topics["VelocityEncR"].data
        if "VelocityEncL" in topics:
            self.w_l = topics["VelocityEncL"].data
        if "Pose" in topics:
            self.pose = topics["Pose"].pose
            self.Sig = topics["Pose"].cov

        x, y, theta = self.pose

        # ===== 1. Compute robot velocity =====
        v = self.R * (self.w_r + self.w_l) / 2.0
        w = self.R * (self.w_r - self.w_l) / self.L

        # ===== 2. Pose update =====
        x_new = x + v * math.cos(theta) * dt
        y_new = y + v * math.sin(theta) * dt
        theta_new = theta + w * dt

        # Wrap heading to (-pi, pi]
        theta_new = math.atan2(math.sin(theta_new), math.cos(theta_new))

        self.pose = [x_new, y_new, theta_new]

        # ===== 3. Covariance propagation =====
        H = np.array([
            [1, 0, -v * math.sin(theta) * dt],
            [0, 1,  v * math.cos(theta) * dt],
            [0, 0, 1]
        ])

        Q = np.array([
            [self.k * abs(self.w_r), 0.0],
            [0.0, self.k * abs(self.w_l)]
        ])

        G = np.array([
            [self.R / 2.0 * math.cos(theta) * dt, self.R / 2.0 * math.cos(theta) * dt],
            [self.R / 2.0 * math.sin(theta) * dt, self.R / 2.0 * math.sin(theta) * dt],
            [self.R / self.L * dt,               -self.R / self.L * dt]
        ])

        self.Sig = H @ self.Sig @ H.T + G @ Q @ G.T

        # Publish pose
        msg_pose = puzz_msgs.Pose()
        msg_pose.pose = self.pose
        msg_pose.cov = self.Sig
        topics["Pose"] = msg_pose

        return topics
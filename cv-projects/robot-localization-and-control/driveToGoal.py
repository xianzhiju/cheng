import math
from lib import puzz_msgs
from my_examples import dead_reckoning as dr


class DriveToGoal:
    def __init__(self):

        # Localisation (Task 1)
        self.dead_reckon = dr.DeadReckoning()

        # ===================== Goal point (Task 2 requirement) =====================
        # Set these to the last two digits of your CIS ID: [x_g, y_g] = [a, b]
        self.target_x = 2.0
        self.target_y = 1.0

        # ===================== Robot limits =====================
        self.v_max = 0.20
        self.wheel_max = 2.0   # conservative; increase in simulation if needed

        # Kinematic parameters (match dead_reckoning.py / coursework spec)
        self.R = 0.05
        self.L = 0.09

        # ===================== Controller gains (tunable) =====================
        self.k_rho = 0.8
        self.k_alpha = 2.2

        # ===================== Behaviour thresholds =====================
        self.rho_tol = 0.10
        self.alpha_rotate_only = math.radians(25)
        self.alpha_stop = math.radians(3)

        # Near-goal slowdown
        self.slow_radius = 0.50
        self.v_min = 0.05

        # Outputs
        self.w_setR = 0.0
        self.w_setL = 0.0

    # --------------------- helpers ---------------------
    @staticmethod
    def _wrap_to_pi(a: float) -> float:
        return math.atan2(math.sin(a), math.cos(a))

    @staticmethod
    def _clamp(x: float, lo: float, hi: float) -> float:
        return max(lo, min(hi, x))

    # --------------------- main loop ---------------------
    def spin(self, topics):

        # Update localisation
        self.dead_reckon.spin(topics)
        x, y, theta = self.dead_reckon.pose

        # ===== Compute errors =====
        dx = self.target_x - x
        dy = self.target_y - y
        rho = math.sqrt(dx * dx + dy * dy)

        goal_heading = math.atan2(dy, dx)
        alpha = self._wrap_to_pi(goal_heading - theta)

        # ===== Stop condition =====
        if rho < self.rho_tol:
            self.w_setR = 0.0
            self.w_setL = 0.0
            topics["IsDone"] = True
            return self._publish(topics)

        # ===== Two-stage controller =====
        if abs(alpha) > self.alpha_rotate_only:
            v = 0.0
            w = self.k_alpha * alpha
        else:
            v_cmd = self.k_rho * rho

            if rho < self.slow_radius:
                scale = rho / self.slow_radius
                v_cmd = self.v_min + (self.v_max - self.v_min) * scale

            v = self._clamp(v_cmd, -self.v_max, self.v_max)
            w = self.k_alpha * alpha

        if rho < self.slow_radius and abs(alpha) < self.alpha_stop:
            w = 0.0

        # ===== Map (v, w) to wheel speeds =====
        w_r = (2.0 * v + w * self.L) / (2.0 * self.R)
        w_l = (2.0 * v - w * self.L) / (2.0 * self.R)

        # ===== Wheel saturation =====
        max_abs = max(abs(w_r), abs(w_l), 1e-9)
        if max_abs > self.wheel_max:
            scale = self.wheel_max / max_abs
            w_r *= scale
            w_l *= scale

        self.w_setR = float(w_r)
        self.w_setL = float(w_l)

        return self._publish(topics)

    def _publish(self, topics):
        msg_w_setR = puzz_msgs.Float32()
        msg_w_setL = puzz_msgs.Float32()
        msg_w_setR.data = self.w_setR
        msg_w_setL.data = self.w_setL
        topics["VelocitySetR"] = msg_w_setR
        topics["VelocitySetL"] = msg_w_setL
        return topics
import math
import robot_params

len1 = robot_params.link_1_length  # file robot_params for link lengths
len2 = robot_params.link_2_length


def fw_kin(joint_angles):
    # Compute end effector position [in meters] for the given pair of joint angles [in degrees]
    angles_hodler = [angle * (3.14 / 180) for angle in joint_angles]
    x_end_effector = len1 * math.cos(angles_hodler[0]) + len2 * math.cos(angles_hodler[0] + angles_hodler[1])
    y_end_effector = len1 * math.sin(angles_hodler[0]) + len2 * math.sin(angles_hodler[0] + angles_hodler[1])

    end_effector_position_analytic = [x_end_effector, y_end_effector]

    print("End effector position (analytic)", end_effector_position_analytic)
    return end_effector_position_analytic

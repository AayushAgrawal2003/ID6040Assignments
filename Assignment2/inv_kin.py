# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:01:49 2023

@author: Bijo Sebastian
"""

len1 = robot_params.link_1_length
len2 = robot_params.link_2_length

import math
import numpy as np
import robot_params

def inv_kin_fn(goal_position):
    #Compute joint angles [in degrees] to reach desired position [in meters] 
    x_desired = goal_position[0]
    y_desired = goal_position[1]
    
    theta_1 = 180 / math.pi
    theta_2 = 180 / math.pi  

    ### Fill this part ###
    c_theta2 = (x_desired**2 + y_desired**2 - len1**2 - len2**2)/(2*len1*len2)
    if c_theta2 > 1 or c_theta2 < -1:
        raise ValueError("No Solution")
    else:    
        theta_2 = np.arccos(c_theta2)
        M = len1 + (len2 * c_theta2)
        N = len2 * np.sin(theta_2)
        theta_1 = np.arctan2(y_desired, x_desired) - np.arctan2(N, M)
        theta_1 = theta_1 * 180 / math.pi
        theta_2 = theta_2 * 180 / math.pi  


    print("Desired joint angles",[theta_1, theta_2])
    return [theta_1, theta_2]
# -*- coding: utf-8 -*-
"""

PREDICTING KICK SUCCESS

This function takes FC Python event tagger coordinates 
(https://fcpython-rugbytracker.netlify.app/) and uses them to predict place
kick success. It uses binomial logistic regression with predefined coefficients
(found prior) for distance (to centre of crossbar) and angle to posts 
(similar to goalkickers.co.za and my RWC paper).

Can change the predefined coefficients in lines 40-42.

Created on Wed Sep  9 20:19:20 2020

@author: Sam

"""

def predictKickSuccessSimple(x,y): # In this function x and y will be flipped compared to my definitions (pitch horizontal) to match the FC Python (pitch vertical)
    
    import numpy as np

    # FCPython gives coords 100x100 so need to make them relative to pitch size (100x70)
    x1 = (x/100)*70   # 70 being pitch width in metres
    
    # Calculate medio-lateral difference between kick and centre of posts
    x_diff = abs(x1 - 35)
    
    # Calculate distance to bottom of posts
    dist = np.sqrt(x_diff**2 + y**2)
    
    # Calculate distance to centre of crossbar
    dist1 = np.sqrt(dist**2 + 3**2) # Height of crossbar is 3 m.
    
    # Calculate angle to posts (angle from kick to pitch centre like, like goalkickers)
    angle = np.rad2deg(np.arctan(x_diff/y))
    
    # Use logistic regression coefficients to calculate predicted success
    const = 5.07 # Constant
    d_coeff = -0.105 # Distance coefficient
    a_coeff = -0.022 # Angle coefficient
    
    predSucc = (1 / (1 + np.exp(-(const + (d_coeff * dist1) + (a_coeff * angle))))) * 100
    predSucc = round(predSucc, 1)
    
    return predSucc


def predictKickSuccessInteract(x,y):
# Calc.s predicted kick success using interactin between distance and angle
# Uses x,y coord.s as x horizontal and y vertical (pitch left to right)
    
    import math
    import numpy as np

    # Coefficients for logistic regression - values calc.ed using RWC 19 data
    b0 = 7.9685 # Constant
    b1 = -0.1702 # Distance
    b2 = -0.1154 # Angle
    b3 = 0.0024 # Distance:Angle interaction (Distance x Angle)

    rel_y = abs(y-35) # Calculate y relative to middle of pitch
    
    angle = math.degrees(math.atan(rel_y/x)) # Angle to middle of pitch (like goalkickers)
    
    d1 = np.sqrt(x**2 + rel_y**2) # Distance to base of posts
    
    # d2 = np.sqrt(d1**2 + 3**2) # Distance to middle of crossbar    
    
    pred_succ = (1 / (1+np.exp(-(b0 + b1*d1 + b2*angle + b3*d1*angle)))) *100
    
    # print(pred_succ)
    return pred_succ
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:13:29 2020

@author: Sam
"""
# Import necessary modules/functions

import matplotlib.pyplot as plt
import pandas as pd

from function_PlotRugbyPitchInfield import CreateRugbyPitch
from function_PredictKickSuccess import predictKickSuccessInteract

kickData = [] # Setup up list of data

def onclick(event): # Function that runs when keyboard button (key) is pressed
                    # This can be changed to run on mouse click in 'cid = ...' line near bottom
   
    
    # print(event.xdata, event.ydata) # Print x and y coords
    # print(event.key) # Print event type (key pressed)

    
    pred_succ = predictKickSuccessInteract(event.xdata, event.ydata) # Calc. predicted success
    print("Predicted Success = ", pred_succ)    
    

    global x, y, eventType, predSucc # Create global variables
    x, y, eventType, predSucc = event.xdata, event.ydata, event.key, pred_succ # Define what global variables equate to
    
    global kickData # Create global list variable
    kickData.append([x, y, eventType, predSucc]) # Append/add global variables from above to the list
    
    
    # Plotting event tag/key press on pitch
    circleSize = 0.75   # Constant circle size
    if (event.key=='2'):
        plot=plt.Circle((x,y),circleSize,color="cyan", ec='cyan', zorder=6)
    elif (event.key=='3'):
        plot=plt.Circle((x,y),circleSize,color="yellow", ec='yellow', zorder=6)
    elif (event.key=='c'):
        plot = plt.scatter(event.xdata, event.ydata, color='cyan', marker='x', zorder=6)
    elif (event.key=='p'):
        plot = plt.scatter(event.xdata, event.ydata, color='yellow', marker='x', zorder=6)
    else:
        plot = plt.scatter(event.xdata, event.ydata, color='k', marker='x', zorder=6) 

    ax.add_artist(plot)
    ax.figure.canvas.draw()


fig,ax = CreateRugbyPitch('forestgreen', 'limegreen', 'white')
cid = fig.canvas.mpl_connect('key_press_event', onclick) # Function run on mouse click using 'button_press_event'

plt.show()



"""
Once done, run the below two lines of code in the console to turn coords variable
to a dataframe with relevant column headings.

data = pd.DataFrame(kickData)
data.columns=['x','y','EventCode', 'PredSucc']
"""


""" Attempt at adding user inputs when button pressed but not working

    # Calculate kick value
    if event.key == '2' or event.key == 'c':
        kick_val = 2 * pred_succ
    elif event.key == '3' or event.key == 'p':
        kick_val = 3 * pred_succ
        
    # Calculate value added by kick
    if event.key == '2':
        val_added = 2 - kick_val
    elif event.key == '3':
        val_added = 3 - kick_val
    elif event.key == 'c' or event.key == 'p':
        val_added = -kick_val

    # Ask for kicker name
    k = input('Kicker: ')

    # Ask for time of kick
    t = input('Time in game:')
    (m, s) = t.split(':')
    t_decimal = int(m) + (int(s)/60)
    
    # Ask for kicker's team
    tm = input('Team:')
    
    # Ask for score of kicker's team
    kScore = input('Kicker score:')
    
    # Ask for score of opponent's team
    oScore = input('Opponent score:')

    global kicker, time, time_decimal, team, kicker_score, opp_score, x, y, eventType, predSucc, kick_value, value_added # Create global variables
    kicker, time, time_decimal, team, kicker_score, opp_score, x, y, eventType, predSucc, kick_value, value_added = k, t, t_decimal, tm, kScore, oScore, event.xdata, event.ydata, event.key, pred_succ, kick_val, val_added # Define what global variables equate to
    
    global kickData # Create global list variable
    kickData.append([kicker, time, time_decimal, team, kicker_score, opp_score, x, y, eventType, predSucc, kick_value, value_added]) # Append/add global variables from above to the list
"""
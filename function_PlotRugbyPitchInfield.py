# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:51:41 2020

@author: Sam
"""


import matplotlib.pyplot as plt

def CreateRugbyPitch(PitchColour, StripeColour, LineColour):
    
# PitchColour  = "forestgreen" / "white"
# StripeColour = "limecolour"  / "white"
# LineColour   = "white"

    fig,ax = plt.subplots(figsize=(10,7))
    ax.axis('off') # this hides the x and y ticks

    # Side and try lines
    y1 = [0,0,70,70,0]
    x1 = [0,100,100,0,0]
    plt.plot(x1,y1,color=LineColour,zorder=5)
  
    # Posts
    y3 = [32.2,37.8]
    x3 = [0,0]
    plt.plot(x3,y3,color=LineColour,linewidth=3,zorder=5)
    y4 = [32.2,37.8]
    x4 = [100,100]
    plt.plot(x4,y4,color=LineColour,linewidth=3,zorder=5)
    
    post1 = plt.Rectangle((-0.5,31.7), 1,1,color=LineColour,zorder=5,alpha=1)
    post2 = plt.Rectangle((-0.5,37.3), 1,1,color=LineColour,zorder=5,alpha=1)
    post3 = plt.Rectangle((99.5,31.7), 1,1,color=LineColour,zorder=5,alpha=1)
    post4 = plt.Rectangle((99.5,37.3), 1,1,color=LineColour,zorder=5,alpha=1)
    ax.add_artist(post1)
    ax.add_artist(post2)
    ax.add_artist(post3)
    ax.add_artist(post4)
    
    # Halfway line and 22m lines
    y5 = [0,70,70,0,0,70]
    x5 = [22,22,50,50,78,78]
    plt.plot(x5,y5,color=LineColour,zorder=5)
    # Centre dash
    y6 = [35,35]
    x6 = [49.5,50.5]
    plt.plot(x6,y6,color=LineColour,zorder=5)
    
    # Try line 5m dashes (left)
    y7 = [2.5,7.5]
    x7 = [5,5]
    plt.plot(x7,y7,color=LineColour,zorder=5)
    y8 = [12.5,17.5]
    x8 = [5,5]
    plt.plot(x8,y8,color=LineColour,zorder=5)
    y9 = [27.2,32.2]
    x9 = [5,5]
    plt.plot(x9,y9,color=LineColour,zorder=5)
    y10 = [37.8,42.8]
    x10 = [5,5]
    plt.plot(x10,y10,color=LineColour,zorder=5)
    y11 = [52.5,57.5]
    x11 = [5,5]
    plt.plot(x11,y11,color=LineColour,zorder=5)
    y12 = [62.5,67.5]
    x12 = [5,5]
    plt.plot(x12,y12,color=LineColour,zorder=5)
    
    # Try line 5m dashes (right)
    y7 = [2.5,7.5]
    x7 = [95,95]
    plt.plot(x7,y7,color=LineColour,zorder=5)
    y8 = [12.5,17.5]
    x8 = [95,95]
    plt.plot(x8,y8,color=LineColour,zorder=5)
    y9 = [27.2,32.2]
    x9 = [95,95]
    plt.plot(x9,y9,color=LineColour,zorder=5)
    y10 = [37.8,42.8]
    x10 = [95,95]
    plt.plot(x10,y10,color=LineColour,zorder=5)
    y11 = [52.5,57.5]
    x11 = [95,95]
    plt.plot(x11,y11,color=LineColour,zorder=5)
    y12 = [62.5,67.5]
    x12 = [95,95]
    plt.plot(x12,y12,color=LineColour,zorder=5)
    
    # 10m dashes (left)
    y7 = [2.5,7.5]
    x7 = [40,40]
    plt.plot(x7,y7,color=LineColour,zorder=5)
    y8 = [12.5,17.5]
    x8 = [40,40]
    plt.plot(x8,y8,color=LineColour,zorder=5)
    y9 = [27.2,32.2]
    x9 = [40,40]
    plt.plot(x9,y9,color=LineColour,zorder=5)
    y10 = [37.8,42.8]
    x10 = [40,40]
    plt.plot(x10,y10,color=LineColour,zorder=5)
    y11 = [52.5,57.5]
    x11 = [40,40]
    plt.plot(x11,y11,color=LineColour,zorder=5)
    y12 = [62.5,67.5]
    x12 = [40,40]
    plt.plot(x12,y12,color=LineColour,zorder=5)
    
    # 10m dashes (right)
    y7 = [2.5,7.5]
    x7 = [60,60]
    plt.plot(x7,y7,color=LineColour,zorder=5)
    y8 = [12.5,17.5]
    x8 = [60,60]
    plt.plot(x8,y8,color=LineColour,zorder=5)
    y9 = [27.2,32.2]
    x9 = [60,60]
    plt.plot(x9,y9,color=LineColour,zorder=5)
    y10 = [37.8,42.8]
    x10 = [60,60]
    plt.plot(x10,y10,color=LineColour,zorder=5)
    y11 = [52.5,57.5]
    x11 = [60,60]
    plt.plot(x11,y11,color=LineColour,zorder=5)
    y12 = [62.5,67.5]
    x12 = [60,60]
    plt.plot(x12,y12,color=LineColour,zorder=5)
    
    # Touchline 5m dashes (top)
    y13 = [65,65]
    x13 = [5,10]
    plt.plot(x13,y13,color=LineColour,zorder=5)
    y14 = [65,65]
    x14 = [19.5,24.5]
    plt.plot(x14,y14,color=LineColour,zorder=5)
    y15 = [65,65]
    x15 = [37.5,42.5]
    plt.plot(x15,y15,color=LineColour,zorder=5)
    y16 = [65,65]
    x16 = [47.5,52.5]
    plt.plot(x16,y16,color=LineColour,zorder=5)
    y17 = [65,65]
    x17 = [57.5,62.5]
    plt.plot(x17,y17,color=LineColour,zorder=5)
    y18 = [65,65]
    x18 = [75.5,80.5]
    plt.plot(x18,y18,color=LineColour,zorder=5)
    y19 = [65,65]
    x19 = [90,95]
    plt.plot(x19,y19,color=LineColour,zorder=5)
    
    # Touchline 5m dashes (bottom)
    y13 = [5,5]
    x13 = [5,10]
    plt.plot(x13,y13,color=LineColour,zorder=5)
    y14 = [5,5]
    x14 = [19.5,24.5]
    plt.plot(x14,y14,color=LineColour,zorder=5)
    y15 = [5,5]
    x15 = [37.5,42.5]
    plt.plot(x15,y15,color=LineColour,zorder=5)
    y16 = [5,5]
    x16 = [47.5,52.5]
    plt.plot(x16,y16,color=LineColour,zorder=5)
    y17 = [5,5]
    x17 = [57.5,62.5]
    plt.plot(x17,y17,color=LineColour,zorder=5)
    y18 = [5,5]
    x18 = [75.5,80.5]
    plt.plot(x18,y18,color=LineColour,zorder=5)
    y19 = [5,5]
    x19 = [90,95]
    plt.plot(x19,y19,color=LineColour,zorder=5)
    
    # Touchline 15m dashes (top)
    y13 = [55,55]
    x13 = [5,10]
    plt.plot(x13,y13,color=LineColour,zorder=5)
    y14 = [55,55]
    x14 = [19.5,24.5]
    plt.plot(x14,y14,color=LineColour,zorder=5)
    y15 = [55,55]
    x15 = [37.5,42.5]
    plt.plot(x15,y15,color=LineColour,zorder=5)
    y16 = [55,55]
    x16 = [47.5,52.5]
    plt.plot(x16,y16,color=LineColour,zorder=5)
    y17 = [55,55]
    x17 = [57.5,62.5]
    plt.plot(x17,y17,color=LineColour,zorder=5)
    y18 = [55,55]
    x18 = [75.5,80.5]
    plt.plot(x18,y18,color=LineColour,zorder=5)
    y19 = [55,55]
    x19 = [90,95]
    plt.plot(x19,y19,color=LineColour,zorder=5)
    
    # Touchline 15m dashes (bottom)
    y13 = [15,15]
    x13 = [5,10]
    plt.plot(x13,y13,color=LineColour,zorder=5)
    y14 = [15,15]
    x14 = [19.5,24.5]
    plt.plot(x14,y14,color=LineColour,zorder=5)
    y15 = [15,15]
    x15 = [37.5,42.5]
    plt.plot(x15,y15,color=LineColour,zorder=5)
    y16 = [15,15]
    x16 = [47.5,52.5]
    plt.plot(x16,y16,color=LineColour,zorder=5)
    y17 = [15,15]
    x17 = [57.5,62.5]
    plt.plot(x17,y17,color=LineColour,zorder=5)
    y18 = [15,15]
    x18 = [75.5,80.5]
    plt.plot(x18,y18,color=LineColour,zorder=5)
    y19 = [15,15]
    x19 = [90,95]
    plt.plot(x19,y19,color=LineColour,zorder=5)
    
    
    ## Background (green) pitch rectangle
    rec3 = plt.Rectangle((-2,-2), 104,74,color=PitchColour,zorder=1,alpha=1)
    ax.add_artist(rec3)
    
    # Option to add 10m pitch length intervals (different shade of green) if using green pitch
    rec4 = plt.Rectangle((10,0), 10, 70, color=StripeColour, zorder=2)
    ax.add_artist(rec4)
    rec4 = plt.Rectangle((30,0), 10, 70, color=StripeColour, zorder=2)
    ax.add_artist(rec4)
    rec4 = plt.Rectangle((50,0), 10, 70, color=StripeColour, zorder=2)
    ax.add_artist(rec4)
    rec4 = plt.Rectangle((70,0), 10, 70, color=StripeColour, zorder=2)
    ax.add_artist(rec4)
    rec4 = plt.Rectangle((90,0), 10, 70, color=StripeColour, zorder=2)
    ax.add_artist(rec4)
    return fig,ax
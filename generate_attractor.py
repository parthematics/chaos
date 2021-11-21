import numpy as np, os
from scipy.integrate import odeint
import plotly.offline as py
import plotly.graph_objs as go
from attractors import *

def get_xyz_arrays_for_attractor(initial_state, params, attractor_type):
    # define the time points to solve for, evenly spaced between the start and end times
    start_time = 0
    end_time = 100
    time_points = np.linspace(start_time, end_time, end_time*100)
    # initialize arrays of x, y, z points that will be populated using odeint
    xyz = [[], [], []]

    # use odeint to solve a system of ordinary differential equations
    # the arguments are: 
    # 1, a function - computes the derivatives
    # 2, a vector of initial system conditions (aka x, y, z positions in space)
    # 3, a sequence of time points to solve for
    # returns an array of x, y, and z value arrays for each time point, with the initial values in the first row
    xyz = odeint(system_map[attractor_type], initial_state, time_points, args=(params,))
        
    # extract the individual arrays of x, y, and z values from the array of arrays
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    
    return (x, y, z)

def graph_3d_attractor(x, y, z, title, colormap=0, save_to_html=False):
    # defining various color schemes allowed. can add more
    colormaps = ['Blackbody', 'Bluered', 'Blues', 'Earth', 
     'Electric', 'Greens', 'Greys', 'Hot', 
     'Jet', 'Picnic', 'Portland', 'Rainbow',
     'RdBu', 'Reds', 'Viridis', 'YlGnBu', 'YlOrRd']

    trace = go.Scatter3d(
        x=x, y=y, z=z,
        marker=dict(
            size=0.01,
            color=z,
            colorscale=colormaps[colormap],
        ),
        line=dict(
            color=z,
            colorscale=colormaps[colormap],
            width=3
        )
    )

    data = [trace]
    layout = dict(
        width=800,
        height=800,
        autosize=False,
        title=title,
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=False,
                backgroundcolor='rgb(180, 255, 230)',
                showgrid=False, # thin lines in the background
                zeroline=False, # thick line at x=0
                visible=False
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=False,
                backgroundcolor='rgb(255, 180, 230)',
                showgrid=False, # thin lines in the background
                zeroline=False, # thick line at x=0
                visible=False
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=False,
                backgroundcolor='rgb(180, 230, 255)',
                showgrid=False, # thin lines in the background
                zeroline=False, # thick line at x=0
                visible=False
            ),
            camera=dict(
                up=dict(x=1, y=0, z=0),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=0, y=0, z=2)
            ),
            aspectratio = dict( x=1, y=1, z=1 ),
            aspectmode = 'manual'
        ),
    )

    formatted_title = '_'.join(title.lower().split())
    fig = dict(data=data, layout=layout)
    if save_to_html:
        py.plot(fig, filename=f"./animations/{formatted_title}_3d_animation.html")
        
    py.iplot(fig)
    
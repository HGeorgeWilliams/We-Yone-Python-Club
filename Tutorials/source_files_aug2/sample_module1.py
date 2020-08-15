#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 08:23:09 2020

@author: hindologeorge-williams

This module holds functions for plotting graphs and doing some basic calculations. 

"""

# import relevant libraries

import pandas as pd 
import math as m 
import numpy as np 
import os

try:

    import wget 

except ImportError:

    os.system("pip install wget") 
    import wget 
    
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,7) # set figure size to 10 inches by 7 inches

# define functions

def plot_chart(file_path: str, chart_type: str):
    """.
    
    Plots the data contained in the excel file specified by file_path
    as a histogram, pie chart, or bar chart, as specified by chart_type. 
    
    Parameters
    ----------
    file_path : str
        DESCRIPTION. Path to excel file holding data. Use full path if file not residing in   
        current directory. 
        
    chart_type : str
        DESCRIPTION. Specifies the type of chart to plot. hist for histogram, pie for pie chart,
        and bar for bar chart.

    Returns
    -------
    None.

    """
  # import data

    data = pd.read_excel(file_path, sheet_name = 'Demographic Data', index_col = 'Town') 

  # plot data 

    if chart_type == 'pie':
  
       data.plot.pie(subplots = True, figsize = (15, 15)) # plot pie chart
  
    elif chart_type == 'hist':
  
       data.hist(bins = 10, figsize = (7, 11)) # plot histogram
  
    elif chart_type == 'bar':
  
       data.plot.bar(figsize = (7, 11)) # plot bar chart
  
    else:
        print('Unsupported chart type')
        



def get_quadratic_roots(a: float, b: float, c: float):
    """.
    
    Computes the roots of a quadratic function with real roots and plots the graph of the function

    Parameters
    ----------
    a : float
        DESCRIPTION. The coefficient of the squared term
        
    b : float
        DESCRIPTION. The coefficient of the middle term
        
    c : float
        DESCRIPTION. The value of the constant term

    Returns
    -------
    root1: float
        DESCRIPTION. The first root
        
    root2: float
        DESCRIPTION. The second root
        
    
    """
  # find roots of equation

    root1 = (-b+m.sqrt(b**2-4*a*c))/(2*a) # first root (enclose 2a in a bracket!)
    root2 = (-b-m.sqrt(b**2-4*a*c))/(2*a) # second root
   
  # plot function

    x = np.linspace(min(root1,root2)-5,max(root1,root2)+5,100) # generate 100 x values
    f_of_x = a*x**2 + b*x +c # evaluate quadratic function
    fig,axes = plt.subplots()
    axes.plot(x, f_of_x, color = 'red', linestyle = '-.')
    axes.set_xlabel('x')
    axes.set_ylabel(r'$f\left(x\right)$')
    axes.set_title(r'Graph of $f\left(x\right)=' + '{}x^2+{}x+{}$'.format(a,b,c))
   
  # return output

    return round(root1,2), round(root2,2)




def get_complex_quadratic_roots(a: float, b: float, c: float):
    """.
    
    Computes the roots of a quadratic function with complex roots and plots its graph 

    Parameters
    ----------
    a : float
        DESCRIPTION. The coefficient of the squared term
        
    b : float
        DESCRIPTION. The coefficient of the middle term
        
    c : float
        DESCRIPTION. The value of the constant term

    Returns
    -------
    root1: float
        DESCRIPTION. The first root
        
    root2: float
        DESCRIPTION. The second root
        
    
    """
    # find roots of equation
  
    real_part = round(-b/(2*a),2) # real part of roots to 2 decimal places
    imag_part = round(m.sqrt(4*a*c - b**2)/(2*a),2) # imaginary part of roots to 2 d.p
    root1 = complex(real_part, imag_part) # first root 
    root2 = complex(real_part, -imag_part) # second root
     
    # plot function
  
    x = np.linspace(root1.real - 10, root1.real + 10, 100) # generate 100 x values
    f_of_x = a*x**2 + b*x +c # evaluate quadratic function
    fig,axes = plt.subplots()
    axes.plot(x, f_of_x, color = 'red', linestyle = '-.')
    axes.set_xlabel('x')
    axes.set_ylabel(r'$f\left(x\right)$')
    axes.set_title(r'Graph of $f\left(x\right)=' + '{}x^2+{}x+{}$'.format(a,b,c))
     
    # return output

    return root1, root2 



def quadratic_root_calculator(a: float, b: float, c: float):
    """.
    
    Computes the roots of a quadratic function and plots the graph of the function

    Parameters
    ----------
    a : float
        DESCRIPTION. The coefficient of the squared term
        
    b : float
        DESCRIPTION. The coefficient of the middle term
        
    c : float
        DESCRIPTION. The value of the constant term

    Returns
    -------
    root1: float
        DESCRIPTION. The first root
        
    root2: float
        DESCRIPTION. The second root
        
    
    """
    if b**2 - 4*a*c >= 0:
       
       # call get_quadratic_roots
  
       root1, root2 = get_quadratic_roots(a, b, c)
  
    else:
  
       # call get_complex_quadratic_roots
  
       root1, root2 = get_complex_quadratic_roots(a, b, c)
  
    return root1, root2


test_variable = {"A": 1, "B": 2}

# test functions

if __name__ == "__main__":
    
   #1. test the function plot_chart
   
   
   # Note: replace the RHS of the assignment below with the full path to the file plotdata.xlsx
          
   file_path = "/Users/hindologeorge-williams/OneDrive - Nexus365/We Yone Python Club/Code/" + \
                 "Python/source_files_aug2/plotdata.xlsx"
   
   if not os.path.exists(file_path): # if file does not exist
       
      # download data from github
      
      wget.download('https://github.com/HGeorgeWilliams/We-Yone-Python-Club/' + 
        'raw/master/Tutorials/source_files_aug2/plotdata.xlsx')
      
      current_directory = os.getcwd() # get current directory
      file_path = current_directory + '/plotdata.xlsx'
   
   plot_chart(file_path = file_path, chart_type = 'pie') #  call function
   
   #2. test the function quadratic_root_calculator
   
   x,y = quadratic_root_calculator(a = 2, b = 8, c = 3) # call function
   
   print("The roots of the equation 2x^2+2x+3 are: {} and {}".format(x,y))
   
   # print test_variable
   
   print("test_variable = {}".format(test_variable))
   
   
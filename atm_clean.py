# import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

class atm:
    """
    The `atm` class represents a model for the relationship between altitude and temperature.
    
    Attributes:
    - data (pd.DataFrame): DataFrame containing altitude and temperature data.
    - r (float): Unknown parameter representing the slope in the linear relationship.
    - T0 (float): Unknown parameter representing the y-intercept in the linear relationship.
    - r_error (float): Error associated with the unknown parameter `r`.
    - T0_error (float): Error associated with the unknown parameter `T0`.
    
    Methods:
    - __init__(self, csv_file): Initializes the `atm` class by reading in the CSV file.
    - clean_data(self): Cleans the data and converts temperature to Kelvin.
    - linear(altitude, r, T0): Static method representing the linear relationship between altitude and temperature.
    - fit_data(self): Fits the data to the linear model and calculates unknown parameters.
    - plot_data_and_fit(self): Plots the data and the linear fit on the same graph.
    - calculate_parameters(self): Cleans the data, fits it, and returns unknown parameters with errors.
    """
    
    def __init__(self, csv_file):
        """
        Initialize the atm class. Automatically read in the CSV file.
        
        Parameters:
        - csv_file (str): Path to the CSV file containing altitude and temperature data.
        """
    
    def clean_data(self):
        """
        Clean the data and create new columns for Temperature in Kelvin.
        """
    
    @staticmethod
    def linear(altitude, r, T0):
        """
        Static method representing the linear relationship between altitude and temperature.
        
        Parameters:
        - altitude (float): Altitude in kilometers.
        - r (float): Unknown parameter representing the slope.
        - T0 (float): Unknown parameter representing the y-intercept.
        
        Returns:
        - float: Predicted temperature in Kelvin.
        """
    
    def fit_data(self):
        """
        Fits the data to the linear model and calculates unknown parameters with errors.
        """

    def plot_data_and_fit(self):
        """
        Plot the data and the fit on the same graph.
        """

    def calculate_parameters(self):
        """
        Cleans the data, fits it to the linear model, and returns unknown parameters with errors.
        
        Returns:
        - dict: Dictionary containing 'r', 'r_error', 'T0', and 'T0_error'.
        """
        values = {"r":0, "r_error":0, "T0":0, "T0_error":0}
        self.clean_data()
        params, covariance = self.fit_data()
        perr = np.sqrt(np.diag(params))
        values["r"] = params[0]
        values["r_error"] = perr[0][0]
        values["T0"] = params[1]
        values["T0_error"] = perr[1][1]
        return values
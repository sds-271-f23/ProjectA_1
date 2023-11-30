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
    data_cleaned = pd.DataFrame()
    data = pd.DataFrame()
    r = 0.0
    T0 = 0.0
    r_error = 0.0
    T0_error = 0.0
    
    def __init__(self, csv_file):
        """
        Initialize the atm class. Automatically read in the CSV file.
        
        Parameters:
        - csv_file (str): Path to the CSV file containing altitude and temperature data.
        """
        self.data = pd.read_csv(csv_file)
        self.data_cleaned = pd.DataFrame()
        
        
    
    def clean_data(self):
        """
        Clean the data and create new columns for Temperature in Kelvin.
        """
        self.data_cleaned = self.data.dropna().copy()
        # netc.loc[:, "DeltaAMPP"] = netc_copied["LOAD_AM"] - netc_copied["VPP12_AM"]
        self.data_cleaned.loc[:, 'temperature_k'] = self.data_cleaned['Temperature (C)']  + 273.15
        # print ("Data cleaned!")
        return self.data_cleaned
    
    
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
        return -r * altitude + T0
        
        
    def fit_data(self):
        """
        Fits the data to the linear model and calculates unknown parameters with errors.
        """
        kelvin = self.data_cleaned['temperature_k']
        altitude = self.data_cleaned['Altitude (km)']
        params, covariance = curve_fit(self.linear, altitude, kelvin)
        return(params, covariance)

    def plot_data_and_fit(self):
        """
        Plot the data and the fit on the same graph.
        """
        params, covariance = self.fit_data()
        x_test = self.data_cleaned['temperature_k']
        y_fit = params[0]*x_test + params[1]
        x, y = self.data_cleaned['temperature_k'], self.data_cleaned['Altitude (km)']
        plt.scatter(x, y)
        plt.plot(x_test,y_fit, color = "pink")
        plt.show()

    def calculate_parameters(self):
        """
        Cleans the data, fits it to the linear model, and returns unknown parameters with errors.
        
        Returns:
        - dict: Dictionary containing 'r', 'r_error', 'T0', and 'T0_error'.
        """
        dict = {"r":0, "r_error":0, "T0":0, "T0_error":0}
        
df = pd.read_csv('atm_data.csv')        
new_atm = atm('atm_data.csv')
new_atm.clean_data()
new_atm.fit_data()
new_atm.plot_data_and_fit()
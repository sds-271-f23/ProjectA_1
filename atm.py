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
        self.data = pd.read_csv(csv_file)
    
    def clean_data(self):
        """
        Clean the data and create new columns for Temperature in Kelvin.
        """
        self.data.loc[:,"Temperature (K)"] = self.data.loc[:,"Temperature (C)"] + 273.15
        self.data.dropna(subset=['Altitude (km)', 'Temperature (K)'], inplace=True)
    
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
        params, cov = curve_fit(self.linear, self.data['Altitude (km)'], self.data['Temperature (K)'])
        self.r = params[0]
        self.T0 = params[1]
        self.r_error = np.sqrt(cov[0, 0])
        self.T0_error = np.sqrt(cov[1, 1])

    def plot_data_and_fit(self):
        """
        Plot the data and the fit on the same graph.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['Altitude (km)'], self.data['Temperature (K)'], label='Data', color='b')
        altitude_range = np.linspace(min(self.data['Altitude (km)']), max(self.data['Altitude (km)']), 100)
        temperature_fit = self.linear(altitude_range, self.r, self.T0)
        plt.plot(altitude_range, temperature_fit, label='Fit', color='r')
        plt.xlabel('Altitude (km)')
        plt.ylabel('Temperature (K)')
        plt.legend()
        plt.title('Altitude vs. Temperature Relationship')
        plt.grid()
        plt.show()

    def calculate_parameters(self):
        """
        Cleans the data, fits it to the linear model, and returns unknown parameters with errors.
        
        Returns:
        - dict: Dictionary containing 'r', 'r_error', 'T0', and 'T0_error'.
        """
        self.clean_data()
        self.fit_data()
        return {
            'r': self.r,
            'r_error': self.r_error,
            'T0': self.T0,
            'T0_error': self.T0_error
        }
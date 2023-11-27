# SDS271-F23-YSI
This mini python package uses the class atm to perform data wrangling, data modeling and data visualization for the atm_data.csv. Users can import this class to analyze and model the relationship between altitude and temperature.

The class initialized the class by reading in the atm_data.csv. The class offers the following functionality through its methods:

Class Attributes:
1. data (pd.DataFrame): A DataFrame containing altitude and temperature data.<br>
2. r (float): A parameter representing the slope in the linear relationship.<br>
3. T0 (float): A parameter representing the y-intercept in the linear relationship.<br>
4. r_error (float): Error associated with the parameter r.<br>
5. T0_error (float): Error associated with the parameter T0.<br>

Methods:
1. __init__(self, csv_file):
Initializes the atm class by reading in a CSV file containing altitude and temperature data.
2. clean_data(self):
Cleans the data by converting temperature to Kelvin and dropping rows with missing values.
3. linear(altitude, r, T0):
Models linear relationship between altitude and temperature.
Takes altitude, slope (r), and y-intercept (T0) as parameters and returns the predicted temperature in Kelvin.
4. fit_data(self):
Fits the data to the linear model using the curve_fit function.
Calculates unknown parameters r and T0 along with their errors.
5. plot_data_and_fit(self):
Plots the original data points and the linear fit
6. calculate_parameters(self):
Calls clean_data and fit_data methods.
Returns a dictionary containing the calculated unknown parameters (r, r_error, T0, T0_error).

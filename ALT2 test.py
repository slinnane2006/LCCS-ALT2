#Event:ALT2
import statistics
import pandas
import matplotlib.pyplot as plt
import csv

filename = 'ALT2_data.csv'
csvfile = open(filename, "r")


csvfile.close()
print("closed")
# Compute and display the mean
mean_value = round(statistics.mean(ALT2_data.csv))
print("Mean Value:", mean_value)
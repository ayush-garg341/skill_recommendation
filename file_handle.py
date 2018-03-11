import csv
import pandas as pd
from machine_learning import MachineLearning

class FileHandle:
    
    def __init__(self, df = None):
        self.df = df
        if self.df is None:
            self.df = MachineLearning(None).get_processed_frame()
        self.write_into_text()
    
    def write_into_text(self):
        new_file = 'C:\pythoncode\\new_suggestions.csv'
        with open(new_file, 'a', newline = '') as csvfile:
            fieldnames = ['antecedants', 'consequents']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            for index, rows in self.df.iterrows():
            	writer.writerow({'antecedants':rows['antecedants'], 'consequents':rows['consequents']})
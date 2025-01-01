import pandas as pd
import ydata_profiling as pp

iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

profile = pp.ProfileReport(iris_data)

profile.to_file("data_profile_report.html")
profile.to_notebook_iframe()
profile.to_file(output_file="pandas_profiler.json")

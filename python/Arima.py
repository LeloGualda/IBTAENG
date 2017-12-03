from matplotlib import pyplot
import pandas as pd
from pandas.plotting import autocorrelation_plot
import statsmodels


series = pd.read_csv('Data/data.csv',
                    dayfirst=True,
                    index_col=0,
                    delimiter=";",
                    header=0,
                    parse_dates=[0],
                    squeeze=True
                  )

series.plot()
autocorrelation_plot(series)
pyplot.show()

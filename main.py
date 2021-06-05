import numpy as np
import pandas as pd

def main():
	pd.set_option('display.max_rows', None)
	happiness_data = pd.read_csv("world-happiness-report.csv")
	input("Press enter to show countries' GDP sorted by those countries' perceptions of corruption.")

	country_by_corruption = happiness_data[["CountryName", "Perceptions of corruption", "Log GDP per capita"]].groupby("CountryName").mean() #if we don't do mean, we won't group data properly
	print(country_by_corruption.sort_values(by="Perceptions of corruption"))
	input("Press enter to show life expectancy and generosity data.")

	life_expectancy_and_generosity = happiness_data[["CountryName", "Generosity", "Healthy life expectancy at birth"]].groupby("CountryName").mean()
	print(life_expectancy_and_generosity.sort_values(by="Generosity"))


main()
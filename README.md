# EnergyConsumption-GroupB

This is the solution proposed by Group B to the Energy Consumption case study given in the Da.Re Residential School. The repository contains the following groups:

### Data Preparation (data_preparation.R)

R code containing the procedure of the feature extraction and the creation of the final dataset.

### Final Dataset (dataset.csv)

Csv dataset produced by the R script: every row contains the date, irradiance, energy, external temperature, internal temperature, delta temperature, day, month, hours and working day.

### Data Analysis and Visualization (program_energy.py)

Python script that performs three regression algorithms on the final dataset: linear regression, polynomial regression and random forest regression. Results are plotted for each algorithm.

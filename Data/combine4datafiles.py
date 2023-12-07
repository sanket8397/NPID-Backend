import pandas as pd

# Load each CSV file into a pandas DataFrame
income_df = pd.read_csv('MedianHouseholdIncome2015.csv')
poverty_df = pd.read_csv('PercentagePeopleBelowPovertyLevel.csv')
education_df = pd.read_csv('PercentOver25CompletedHighSchool.csv')
race_df = pd.read_csv('ShareRaceByCity.csv')

# Perform an inner join on the DataFrames using the common 'GeographicArea' and 'City' columns
merged_data = pd.merge(income_df, poverty_df, on=['GeographicArea', 'City'], how='inner')
merged_data = pd.merge(merged_data, education_df, on=['GeographicArea', 'City'], how='inner')
merged_data = pd.merge(merged_data, race_df, on=['GeographicArea', 'City'], how='inner')

# Print the combined data
print(merged_data)

# Optionally, you can save the merged data to a new CSV file
merged_data.to_csv('combined_data.csv', index=False)


# Load the combined data into a pandas DataFrame
combined_data_df = pd.read_csv('combined_data.csv')

# Remove " city", " CDP", " town", and " village" from the end of the city names
combined_data_df['City'] = combined_data_df['City'].replace({' city$': '', ' CDP$': '', ' town$': '', ' village$': ''}, regex=True)

combined_data_df.to_csv('modified_combined_data.csv', index=False)

import pandas as pd

# Load the combined data and the PoliceKillingsUS data into pandas DataFrames
combined_data_df = pd.read_csv('modified_combined_data.csv')
police_killings_df = pd.read_csv('PoliceKillingsUS.csv')

# Perform a left join on the DataFrames using the common 'GeographicArea' and 'City' columns
final_data = pd.merge(police_killings_df, combined_data_df, on=['GeographicArea', 'City'], how='left')

# Remove entries with empty 'MedianIncome'
final_data = final_data.dropna(subset=['MedianIncome'])

# For the column 'City' replace with 'GeographicArea' + ' - ' + 'City'
final_data['City'] = final_data['GeographicArea'] + " - " + final_data['City']

# Reordering columns
final_data = final_data[['id', 'name', 'date', 'manner_of_death', 'armed', 'age', 'gender', 'race', 'City', 'GeographicArea', 'signs_of_mental_illness', 'threat_level', 'flee', 'body_camera', 'MedianIncome', 'poverty_rate', 'percent_completed_hs', 'share_white', 'share_black', 'share_native_american', 'share_asian', 'share_hispanic']]
final_data = final_data.dropna()
final_data = final_data[~final_data['MedianIncome'].isin(['(X)', '-'])]
final_data['date'] = pd.to_datetime(final_data['date'])
final_data['deathYear'] = final_data['date'].dt.year

# Split the 'name' column into a list of words
final_data['name'] = final_data['name'].str.split()

# Create 'FirstName' and 'LastName' columns
final_data['FirstName'] = final_data['name'].apply(lambda x: x[0])
final_data['LastName'] = final_data['name'].apply(lambda x: x[-1])

# Drop the 'name' column
final_data = final_data.drop(columns=['name'])
print(final_data['armed'].unique())

# Optionally, you can save the final merged data to a new CSV file
final_data.to_csv('final_combined_data.csv', index=False)
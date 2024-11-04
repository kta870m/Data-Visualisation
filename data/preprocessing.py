import pandas as pd

# Load the datasets
health_and_social_df = pd.read_csv('health_and_social.csv')
# hospital_employment_df = pd.read_csv('hospital_employment.csv')
# technical_resources_df = pd.read_csv('technical_resources.csv')

# Define columns to keep based on relevant data insights
columns_to_keep = ['STRUCTURE_ID', 'STRUCTURE_NAME', 'Variable', 'UNIT', 'Measure', 'Country', 
                   'Year', 'OBS_VALUE']

# Filter each DataFrame
health_and_social_df = health_and_social_df[columns_to_keep]
# hospital_employment_df = hospital_employment_df[columns_to_keep]
# technical_resources_df = technical_resources_df[columns_to_keep]

# Handle missing values (e.g., filling or dropping)
health_and_social_df.dropna(subset=['OBS_VALUE'], inplace=True)
# hospital_employment_df.dropna(subset=['OBS_VALUE'], inplace=True)
# technical_resources_df.dropna(subset=['OBS_VALUE'], inplace=True)

# Rename columns for consistency if needed
health_and_social_df.rename(columns={'OBS_VALUE': 'Value'}, inplace=True)
# hospital_employment_df.rename(columns={'OBS_VALUE': 'Value'}, inplace=True)
# technical_resources_df.rename(columns={'OBS_VALUE': 'Value'}, inplace=True)

# Merge datasets on common columns if needed
# combined_df = pd.concat([health_and_social_df, hospital_employment_df, technical_resources_df], ignore_index=True)

combined_df = pd.concat([health_and_social_df], ignore_index=True)

# Save preprocessed data to a new CSV
combined_df.to_csv('preprocessed_social_data.csv', index=False)

import pandas as pd

# Load data
df = pd.read_csv('data/hospital_timely_data.csv')

# Filter only ED1b measure
df = df[df['Measure ID'] == 'ED1b']

# Sort by wait time
df_sorted = df.sort_values(by='Score', ascending=False)

# Print top 5 hospitals with longest wait time
print(df_sorted[['Hospital Name', 'Score']].head())

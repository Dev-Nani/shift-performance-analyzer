import os
import pandas as pd
import matplotlib.pyplot as plt

# Get absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to input CSV
data_path = os.path.join(script_dir, '..', 'data', 'sample_shift_data.csv')

# Load the data with date parsing
df = pd.read_csv(data_path, parse_dates=['Date'])

# Calculate KPIs
df['Output_per_Hr'] = df['Output'] / df['Planned_Hours']
df['Downtime_per_Hr'] = df['Downtime_Minutes'] / 60 / df['Planned_Hours']
df['Scrap_Ratio'] = df['Scrap_Lbs'] / df['Output']

# Group by Shift and calculate mean KPIs
summary = df.groupby('Shift').agg({
    'Output_per_Hr': 'mean',
    'Downtime_per_Hr': 'mean',
    'Scrap_Ratio': 'mean'
}).reset_index()

# Prepare output directory path
output_dir = os.path.join(script_dir, '..', 'output')

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save summary CSV
summary.to_csv(os.path.join(output_dir, 'results.csv'), index=False)
print(f"Shift KPI summary saved to {os.path.join(output_dir, 'results.csv')}")

# Plotting the KPIs
summary.set_index('Shift').plot(kind='bar', figsize=(8,5))
plt.title('Average KPIs per Shift')
plt.ylabel('Value')
plt.xticks(rotation=0)
plt.tight_layout()

# Save the plot image
plt.savefig(os.path.join(output_dir, 'shift_comparison.png'))
print(f"Shift comparison chart saved to {os.path.join(output_dir, 'shift_comparison.png')}")

# Show the plot window (optional, comment out if running headless)
plt.show()

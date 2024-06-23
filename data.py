import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Generate a date range
date_range = pd.date_range(start='2024-01-01', periods=100, freq='H')

# Generate sample data
data = {
    'Timestamp': date_range,
    'CPU_Usage': np.random.uniform(10, 90, size=len(date_range)),
    'Memory_Usage': np.random.uniform(20, 80, size=len(date_range)),
    'Disk_IO': np.random.uniform(100, 1000, size=len(date_range)),
    'Network_In': np.random.uniform(1000, 5000, size=len(date_range)),
    'Network_Out': np.random.uniform(1000, 5000, size=len(date_range)),
    'Cost': np.random.uniform(0.01, 0.1, size=len(date_range))
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())
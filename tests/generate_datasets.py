import pandas as pd
import numpy as np

# Create six sample datasets with different anomalies

# Dataset 1: Normal data
data1 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 53, 52, 51],
    'Memory_Usage': [40, 42, 43, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 325, 340],
    'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

# Dataset 2: Sudden spike in CPU usage
data2 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 100, 52, 51],
    'Memory_Usage': [40, 42, 43, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 325, 340],
    'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

# Dataset 3: Sudden drop in Memory usage
data3 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 53, 52, 51],
    'Memory_Usage': [40, 42, 15, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 325, 340],
    'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

# Dataset 4: Sudden spike in Disk IO
data4 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 53, 52, 51],
    'Memory_Usage': [40, 42, 43, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 800, 340],
    'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

# Dataset 5: Sudden drop in Network In
data5 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 53, 52, 51],
    'Memory_Usage': [40, 42, 43, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 325, 340],
    'Network_In': [1000, 1100, 1050, 300, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

# Dataset 6: Sudden spike in Network Out
data6 = {
    'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
    'CPU_Usage': [50, 60, 55, 53, 52, 51],
    'Memory_Usage': [40, 42, 43, 44, 45, 46],
    'Disk_IO': [300, 320, 310, 330, 325, 340],
    'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
    'Network_Out': [1200, 1300, 1250, 2000, 1270, 1290],
    'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
}

datasets = [data1, data2, data3, data4, data5, data6]

# Save datasets to CSV for testing
for i, data in enumerate(datasets, start=1):
    df = pd.DataFrame(data)
    df.to_csv(f'dataset_{i}.csv', index=False)

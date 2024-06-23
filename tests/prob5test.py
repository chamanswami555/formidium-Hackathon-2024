import logging
import pandas as pd
import numpy as np

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Sample data
datasets = [
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 53, 52, 51],
        'Memory_Usage': [40, 42, 43, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 325, 340],
        'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    },
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 100, 52, 51],
        'Memory_Usage': [40, 42, 43, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 325, 340],
        'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    },
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 53, 52, 51],
        'Memory_Usage': [40, 42, 15, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 325, 340],
        'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    },
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 53, 52, 51],
        'Memory_Usage': [40, 42, 43, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 800, 340],
        'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    },
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 53, 52, 51],
        'Memory_Usage': [40, 42, 43, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 325, 340],
        'Network_In': [1000, 1100, 1050, 300, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 1280, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    },
    {
        'Timestamp': pd.date_range(start='2024-01-01 00:00:00', periods=6, freq='H'),
        'CPU_Usage': [50, 60, 55, 53, 52, 51],
        'Memory_Usage': [40, 42, 43, 44, 45, 46],
        'Disk_IO': [300, 320, 310, 330, 325, 340],
        'Network_In': [1000, 1100, 1050, 1080, 1070, 1090],
        'Network_Out': [1200, 1300, 1250, 2000, 1270, 1290],
        'Cost': [0.1, 0.12, 0.11, 0.115, 0.113, 0.114]
    }
]

# Anomaly Detection
class AnomalyDetector:
    def __init__(self):
        self.actions = {
            'CPU_Usage': 'Optimize CPU usage by scaling resources or optimizing code.',
            'Memory_Usage': 'Optimize memory usage by identifying memory leaks or inefficiencies.',
            'Disk_IO': 'Optimize disk I/O by reviewing data access patterns and caching strategies.',
            'Network_In': 'Optimize incoming network traffic by analyzing data transfer patterns.',
            'Network_Out': 'Optimize outgoing network traffic by compressing data or reducing data transfer size.',
            'Cost': 'Review cost anomalies to ensure they do not exceed budget constraints.'
        }

    def detect_anomalies(self, data):
        anomalies = []
        for i, dataset in enumerate(data, start=1):
            # Extracting relevant columns
            X = np.array([dataset['CPU_Usage'], dataset['Memory_Usage'], dataset['Disk_IO'], dataset['Network_In'], dataset['Network_Out']]).T
            y = np.array(dataset['Cost'])

            # Simple anomaly detection (for demonstration)
            threshold = 0.2
            predictions = np.mean(X, axis=1) * y  # Simplified for demonstration
            anomalies_idx = np.where(predictions > threshold)[0]

            if len(anomalies_idx) > 0:
                anomalies.append({
                    'Dataset': f'Dataset {i}',
                    'Anomaly Indices': anomalies_idx,
                    'Anomaly Details': {key: [dataset[key][idx] for idx in anomalies_idx] for key in dataset.keys()}
                })

        return anomalies

    def accuracy_score(self, detected_anomalies, total_datasets):
        detected_count = sum(len(anomaly['Anomaly Indices']) for anomaly in detected_anomalies)
        total_possible_anomalies = sum(len(dataset['CPU_Usage']) for dataset in total_datasets)
        return detected_count / total_possible_anomalies

# Main function
def main():
    detector = AnomalyDetector()
    anomalies = detector.detect_anomalies(datasets)

    if len(anomalies) > 0:
        for anomaly in anomalies:
            print(f"Anomalies detected in {anomaly['Dataset']} at indices: {anomaly['Anomaly Indices']}")
            print(f"Anomaly Details:")
            for key, value in anomaly['Anomaly Details'].items():
                print(f"{key}: {value}")
                if key in detector.actions:
                    print(f"Action: {detector.actions[key]}")
            print("Appropriate action: Investigate and take necessary steps to optimize resources.")
            print()

        accuracy = detector.accuracy_score(anomalies, datasets)
        print(f"Accuracy score: {accuracy:.2%}")
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    main()

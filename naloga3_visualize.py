import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('.\\results3.csv')

# Create the plot
plt.figure(figsize=(6, 4))

plt.plot(df['Threshold'], df['Precision'], label='Precision', marker='o')
plt.plot(df['Threshold'], df['Recall'], label='Recall', marker='o')
plt.plot(df['Threshold'], df['F-score'], label='F-score', marker='o')

# Add labels and title
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Performance Metrics vs. Threshold')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
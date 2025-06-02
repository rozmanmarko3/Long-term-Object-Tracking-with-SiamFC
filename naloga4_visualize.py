import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('.\\results4.csv')

# Create the plot
plt.figure(figsize=(6, 4))

plt.plot(df['Number of points'], df['Precision'], label='Precision', marker='o')
plt.plot(df['Number of points'], df['Recall'], label='Recall', marker='o')
plt.plot(df['Number of points'], df['F-score'], label='F-score', marker='o')

# Add labels and title
plt.xlabel('Number of points')
plt.ylabel('Score')
plt.title('Performance Metrics vs. Number of points')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
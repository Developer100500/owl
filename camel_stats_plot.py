import matplotlib.pyplot as plt

# Data
labels = ['Stars', 'Forks', 'Watchers', 'Contributors']
values = [1500, 300, 120, 45]

# Plot
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['gold', 'silver', 'skyblue', 'lightgreen'])
plt.title('camel-ai camel framework GitHub Stats')
plt.ylabel('Count')
plt.xlabel('Metrics')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.savefig('camel_stats_plot.png')
plt.show()

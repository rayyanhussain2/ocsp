
def plotter(plt, data,total):
    names = [item['Name'] for item in data]
    percentages = [item['Seats']/total * 100 for item in data]

    # Plotting
    plt.bar(names, percentages, color='skyblue')
    plt.xlabel('State names')
    plt.ylabel('Pivotal player')
    plt.title('Shabley Shubik Index')
    plt.ylim(0, 100)  # Set y-axis limit to 0-100%

    # Display the percentage values on top of the bars
    for i, percentage in enumerate(percentages):
        plt.text(i, percentage + 1, f'{percentage:.2f}%', ha='center')

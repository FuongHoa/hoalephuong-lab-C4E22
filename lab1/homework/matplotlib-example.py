from matplotlib import pyplot

#prepare data
machine_counts = [18, 4, 2]

#prepare labels
machine_names = ["PC", "MAC", "Linux"]

#draw pie chart
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.title("The percentage of the number of ppl using which laptop")
pyplot.axis("equal")

#show
pyplot.show()
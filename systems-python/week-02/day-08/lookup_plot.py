import matplotlib.pyplot as plt

# X axis — the three sizes we tested
sizes = [1_000, 10_000, 100_000]

# Y axis — the list lookup times you measured
list_times = [0.0000042920, 0.0000394580, 0.0003887080]

# Y axis — the set lookup times you measured
set_times = [0.0000002090, 0.0000006670, 0.0000001660]

# Draw the list line — 'o-' means dots connected by a line
plt.plot(sizes, list_times, 'o-', label="List lookup")

# Draw the set line on the same chart
plt.plot(sizes, set_times, 'o-', label="Set lookup")

# Label the X axis
plt.xlabel("Number of items")

# Label the Y axis
plt.ylabel("Lookup time (seconds)")

# Title at the top
plt.title("List vs Set Lookup Time")

# Show which line is which
plt.legend()

# Display the chart window
plt.show()
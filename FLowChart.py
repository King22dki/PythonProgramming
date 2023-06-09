import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define the flowchart elements
elements = [
    ('Start', 'rounded', 'green'),
    ('Input', 'box', 'white'),
    ('Process 1', 'box', 'white'),
    ('Decision', 'diamond', 'yellow'),
    ('Yes', 'ellipse', 'blue'),
    ('Process 2', 'box', 'white'),
    ('No', 'diamond', 'red'),
    ('Process 3', 'box', 'white'),
    ('End', 'rounded', 'green')
]

# Define the flowchart connections
connections = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (4, 7),
    (5, 7),
    (7, 8)
]

# Create the flowchart figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Define spacing between elements
vertical_spacing = 1.5

# Draw the flowchart elements
for i, (element, shape, color) in enumerate(elements):
    y = 9 - i * vertical_spacing
    if shape == 'rounded':
        bbox_props = dict(boxstyle='round', facecolor=color, edgecolor='gray')
        ax.annotate(element, xy=(5, y), ha='center', va='center', bbox=bbox_props)
    elif shape == 'diamond':
        diamond = Polygon([[5, y], [4.6, y - 0.4], [5, y - 0.8], [5.4, y - 0.4]],
                          closed=True, facecolor=color, edgecolor='gray')
        ax.add_patch(diamond)
        ax.annotate(element, xy=(5, y), ha='center', va='center')

    else:
        ax.annotate(element, xy=(5, y), ha='center', va='center', bbox=dict(boxstyle='square', facecolor=color, edgecolor='gray'))

# Draw the flowchart connections
for connection in connections:
    start_point = (5, 9 - connection[0] * vertical_spacing)
    end_point = (5, 9 - connection[1] * vertical_spacing)
    ax.annotate('', xy=end_point, xytext=start_point, arrowprops=dict(arrowstyle='->'))

# Show the flowchart
plt.show()



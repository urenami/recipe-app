from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Function to get the recipe name from a given ID
def get_recipename_from_id(val):
    # Fetch the recipe object from the database using the ID
    recipename = Recipe.objects.get(id=val)
    return recipename

# Function to generate a graph and return it as a base64-encoded string
def get_graph():
    # Create an in-memory buffer to store the graph image
    buffer = BytesIO()

    # Save the current plot to the buffer in PNG format
    plt.savefig(buffer, format="png")

    # Move the pointer to the beginning of the buffer
    buffer.seek(0)

    # Get the raw image data from the buffer
    image_png = buffer.getvalue()

    # Encode the image to base64 for use in web applications
    graph = base64.b64encode(image_png)

    # Decode the base64-encoded image to a UTF-8 string
    graph = graph.decode("utf-8")

    # Close the buffer to free up resources
    buffer.close()

    # Return the base64 string of the graph
    return graph

# Function to generate a chart (bar, pie, or line) based on the provided chart type
def get_chart(chart_type, data, **kwargs):
    # Switch to the AGG backend for rendering images (this is for non-interactive environments)
    plt.switch_backend("AGG")

    # Increase figure size for better visibility of charts
    fig = plt.figure(figsize=(6, 3))  # Adjusted figure size for a more horizontal layout

    # Check the chart type and create the respective chart
    if chart_type == "#1":
        # Create a bar chart (cooking time vs. recipe name)
        plt.bar(data["name"], data["cooking_time"])

        # Rotate x-axis labels to avoid overlap (important for long recipe names)
        plt.xticks(rotation=45, ha='right')  # Rotate labels 45 degrees to the right

    elif chart_type == "#2":
        # Create a pie chart (cooking time distribution)
        labels = kwargs.get("labels")  # Get additional labels from kwargs if provided
        plt.pie(data["cooking_time"], labels=labels, autopct='%1.1f%%')  # Display percentage on the pie slices

    elif chart_type == "#3":
        # Create a line chart (cooking time vs. recipe name)
        plt.plot(data["name"], data["cooking_time"])

        # Rotate x-axis labels for better readability in line charts
        plt.xticks(rotation=45, ha='right')  # Rotate labels for line chart as well if needed

    else:
        # If the chart type is unknown, print a message (could be handled better)
        print("Unknown chart type")

    # Adjust the layout to prevent overlapping elements
    plt.tight_layout()

    # Generate the graph image and return it as a base64-encoded string
    chart = get_graph()
    return chart

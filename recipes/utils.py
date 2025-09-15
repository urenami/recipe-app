from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# Function to get the recipe name from a given ID
def get_recipename_from_id(val):
    recipename = Recipe.objects.get(id=val)
    return recipename

# Function to generate a graph and return it as a base64-encoded string
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png", transparent=True)  # transparent background
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode("utf-8")
    buffer.close()
    return graph

# Function to generate a chart (bar, pie, or line) based on the provided chart type
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend("AGG")
    plt.figure(figsize=(6, 4), facecolor="none")

    # 🔥 Dark theme + fonts
    plt.rcParams.update({
        "text.color": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "font.family": "Poppins"
    })

    # 🎨 Color map based on difficulty
    difficulty = None
    if "difficulty" in data.columns:
        difficulty = data["difficulty"].iloc[0]

    color_map = {
        "Easy": "#00ff00",         # green
        "Intermediate": "#ffa500", # orange
        "Hard": "#ff4c4c",         # red
    }
    color = color_map.get(difficulty, "#00ff00")  # default green

    if chart_type == "#1":  # bar chart
        plt.bar(data["name"], data["cooking_time"], color=color)
        plt.xticks(rotation=45, ha="right")

    elif chart_type == "#2":  # pie chart
        labels = kwargs.get("labels")
        plt.pie(
            data["cooking_time"],
            labels=labels,
            autopct="%1.1f%%",
            colors=[color] * len(data)
        )

    elif chart_type == "#3":  # line chart
        plt.plot(data["name"], data["cooking_time"], marker="o", color=color)
        plt.xticks(rotation=45, ha="right")

    else:
        print("Unknown chart type")

    plt.tight_layout()
    chart = get_graph()
    return chart
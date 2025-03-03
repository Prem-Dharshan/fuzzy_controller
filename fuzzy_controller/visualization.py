import numpy as np
import matplotlib.pyplot as plt
from .fuzzy_logic import get_membership

def plot_fuzzy_sets(fuzzy_sets, title, highlight_x=None):
    plt.figure(figsize=(8, 4))
    x_vals = np.linspace(0, 255, 500)

    for label, params in fuzzy_sets.items():
        y_vals = np.array([get_membership(x, params) for x in x_vals])
        plt.plot(x_vals, y_vals, label=label)

    if highlight_x is not None:
        plt.axvline(x=highlight_x, color='red', linestyle='--', label=f"Output: {highlight_x:.2f}")

    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Membership")
    plt.legend()
    plt.grid(True)
    plt.show()

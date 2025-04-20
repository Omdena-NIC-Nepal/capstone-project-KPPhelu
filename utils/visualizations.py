"""
This file deals with the visualization functions
"""
import matplotlib as plt


def plot_district_map (gdf, title="Nepal District Map"):
    """
    Plot map of Nepal districts using gievn GeoDataFrame.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    gdf.plot(ax=ax, color='none', edgecolor='black', legend=True)
    plt.title("Nepal's Administrative Boundaries")
    ax.axis('off')
    plt.tight_layout()
    return plt
"""
This file deals with the visualization functions
"""
import matplotlib.pyplot as plt
import geoplot as gplt
import geoplot.crs as gcrs


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

def choropleth_map (gdf_districtwise, column, title):
    """
    Choropleth in map of Nepal for given environment variable
    Parameters:
        gdf (gdf_districtwise): A GeoDataFrame containing district geometries and a value column.
        column (str): The name of the column to visualize.
        title (str): Title of the plot.
    """
    # fig, ax = plt.subplots(figsize=(10, 6))
    gplt.choropleth(
        gdf_districtwise, #GeoDataframe
        hue = column,  # column to visualize
        projection= gcrs.AlbersEqualArea(),
        legend=True,
        cmap='inferno_r',
        linewidth=0.5,    
        figsize=(12, 6),
        edgecolor='black',
        # ax=ax,
    )
    plt.title(title)
    plt.tight_layout()

    return plt

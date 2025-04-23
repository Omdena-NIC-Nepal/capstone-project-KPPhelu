"""
This file deals with the visualization functions
"""
import matplotlib.pyplot as plt
import seaborn as sns
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
        gdf (_gdf_districtwise): A GeoDataFrame containing district geometries and a value column.
            By prefixing the parameter with an underscore, Streamlit knows not to hash or track it for cache invalidation.
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

def plot_time_series(df, column, title):
    """
    plots time series data
    """
    fig, ax = plt.subplots(figsize = (12, 4))
    ax.plot(df['Date'], df[column])
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.set_title(title)
    ax.grid(True)
    return fig

def plot_boxplot_monthly(df, column, title):
    """
    Plot monthwise boxplot to show seasonal trend
    """
    fig, ax = plt.subplots(figsize = (12, 4))
    sns.boxplot(x='Month', y=column, data=df, ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel(column)
    ax.set_title(title)
    ax.grid(True)
    # plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    #                             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    return fig

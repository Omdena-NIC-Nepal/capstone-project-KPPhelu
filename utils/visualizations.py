"""
This file deals with the visualization functions
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geoplot as gplt
import geoplot.crs as gcrs


def plot_histogram(df, fig_size, subplot_rows, subplot_cols):
    ### Uni-variate visualization: Visualize histogram and boxplot of each variables
    ## visualize histogram

    # select numeric columns
    numeric_columns = df.select_dtypes(include=np.number).columns
    
    ## check number of sub-plots
    if subplot_rows*subplot_cols < len(numeric_columns):
        print('Number of subplots are insufficient.')
        print('Number of columns: ', len(numeric_columns))
        print('Number of subplots: ', subplot_rows, ' x ', subplot_cols)
        return None
        
    fig, axs = plt.subplots(subplot_rows, subplot_cols, figsize=fig_size)
    
    ## first turn axis off all axs
    for ax in axs:
        if len(ax)>1:
            for axis in ax:
                axis.set_axis_off()
        else:
            ax.set_axis_off()
        
    row_index = 0
    col_index = 0
    for col in numeric_columns:              
        # make required axis visible
        axs[row_index, col_index].set_axis_on()
        sns.histplot(df[col], ax=axs[row_index, col_index], kde=True)
#         ax=axs[row_index, col_index].title.set_text(col)
        col_index += 1
        if col_index == subplot_cols:
            col_index = 0
            row_index += 1
            
    fig.suptitle("Histogram and KDE plot of Climate data.")
    plt.tight_layout()
    return fig

def plot_pairplot(df):
    ## Pair plot
    fig = sns.pairplot(df)
    return fig
    
def plot_correlation_heatmap(df, figsize=(8,8), annot=True):
    # select numeric columns
    numeric_columns = df.select_dtypes(include=np.number).columns
    corr_matrix = df[numeric_columns].corr()

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr_matrix, annot=annot, fmt=".2f", cmap='coolwarm', square=True, ax=ax, cbar_kws={'shrink': 0.75})
    ax.set_title("Correlation Coefficient Heatmap", fontsize=10)

    return fig

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


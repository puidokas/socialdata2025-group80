import pandas as pd
import numpy as np
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, ColorBar, LinearColorMapper, HoverTool, Select
from bokeh.layouts import column, row
from bokeh.transform import transform
from bokeh.palettes import Viridis256
import calendar

# Load dataset (Replace with the actual path to your dataset)
data = pd.read_csv("merged_data.csv")

# Convert month names to numbers
month_to_num = {month: index for index, month in enumerate(calendar.month_name) if month}
data["Month"] = data["Month"].map(month_to_num).fillna(pd.NA).astype(float)

# Ensure correct data types
data["DayOfWeek"] = pd.Categorical(data["DayOfWeek"], categories=[
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
], ordered=True)

# Filter for narcotics incidents
data_narcotics = data[data["Category"] == "DRUG/NARCOTIC"].copy()

# Reverse month mapping for display
num_to_month = {index: month for index, month in enumerate(calendar.month_name) if month}

def get_heatmap_data(year, month_name):
    month = month_to_num[month_name]
    filtered = data_narcotics[(data_narcotics["Year"] == year) & (data_narcotics["Month"] == month)]
    heatmap_data = filtered.groupby(["DayOfWeek", "TimeOfDay"], observed=True).size().reset_index(name="Count")

    # Ensure full grid (fill missing values with 0)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hours = list(range(24))
    full_grid = pd.MultiIndex.from_product([days, hours], names=["DayOfWeek", "TimeOfDay"])
    heatmap_data = heatmap_data.set_index(["DayOfWeek", "TimeOfDay"]).reindex(full_grid, fill_value=0).reset_index()

    return heatmap_data

# Default values for Year and Month
year_default = data_narcotics["Year"].max()
month_default = "January"
heatmap_data = get_heatmap_data(year_default, month_default)

# Ensure nonzero color mapping
count_min = heatmap_data["Count"].min()
count_max = heatmap_data["Count"].max()
if count_min == count_max:
    count_min, count_max = 0, count_max + 1

# Color Mapping
mapper = LinearColorMapper(palette=Viridis256, low=count_min, high=count_max)

# Create ColumnDataSource
source = ColumnDataSource(heatmap_data)

# Bokeh Figure
p = figure(title=f"Narcotics Incidents Heatmap ({year_default}, {month_default})",
           x_range=(0, 23), y_range=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
           x_axis_label="Hour of Day", y_axis_label="Day of Week",
           toolbar_location=None, tools="")

p.rect(x="TimeOfDay", y="DayOfWeek", width=1, height=1, source=source,
       line_color=None, fill_color=transform("Count", mapper))

# Hover Tool
hover = HoverTool(tooltips=[("Hour", "@TimeOfDay"), ("Day", "@DayOfWeek"), ("Incidents", "@Count")])
p.add_tools(hover)

# ColorBar
color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p.add_layout(color_bar, 'right')

# Dropdown and Slider for Dynamic Updates
year_select = Select(title="Year", value=str(year_default),
                     options=[str(y) for y in sorted(data_narcotics["Year"].unique(), reverse=True)])
month_select = Select(title="Month", value=month_default, options=list(num_to_month.values()))

def update_plot(attr, old, new):
    year = int(year_select.value)
    month_name = month_select.value
    updated_data = get_heatmap_data(year, month_name)

    # Ensure nonzero color mapping
    count_min = updated_data["Count"].min()
    count_max = updated_data["Count"].max()
    if count_min == count_max:
        count_min, count_max = 0, count_max + 1

    # Update ColumnDataSource
    source.data = dict(ColumnDataSource(updated_data).data)

    # Update color scale
    mapper.low = count_min
    mapper.high = count_max

    # Update title
    p.title.text = f"Narcotics Incidents Heatmap ({year}, {month_name})"

# Attach callbacks
year_select.on_change("value", update_plot)
month_select.on_change("value", update_plot)

# Layout
layout = column(row(year_select, month_select), p)

# Add layout to Bokeh server document
curdoc().add_root(layout)
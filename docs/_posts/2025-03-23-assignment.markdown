---
layout: post
title:  "02806 Social Data Analysis: Assignment 2 - Group 77"
date:   2025-03-23 13:26:43 +0100
categories: jekyll update
---

# Introduction of the dataset

## Understanding San Francisco's Crime Data  

San Francisco has long been a city of contrasts—booming industries and persistent challenges, innovation alongside deep-rooted issues. To better understand crime trends over time, we analyzed a dataset that merges two key sources from the **DataSF Open Data Portal**:  

- **Police Department Incident Reports (2003 - May 2018):** This historical dataset contains police-reported crime incidents up until mid-2018. Data was sourced from an older system, which was eventually replaced due to reliability concerns.  
- **Police Department Incident Reports (2018 - Present):** This dataset continues from 2018 onward and is maintained in the **Crime Data Warehouse**, a more stable and comprehensive reporting system.  

## What’s in the Data?  
Each reported incident includes details such as the **type of crime, date and time, police district, and general location (mapped to nearby intersections for privacy)**. 

For example, a record from 2016 might describe a **burglary reported in the Mission District at 2:30 AM**.

## What This Data Tells Us  
By analyzing nearly two decades of crime reports, we can uncover patterns and trends—how crime rates fluctuate over time, how certain offenses become more or less common, and how policy changes or social factors influence reported crime.  

This page will highlight one crime category from the dataset, DRUG/NARCOTIC, helping shed light on the evolving nature of crime in San Francisco.

## Heatmap

<iframe src="{{ site.baseurl }}/assets/heatmap.html" width="100%" height="600px" style="border: none;"></iframe>

# Narcotics-Related Crime Patterns in San Francisco: Trends by Hour, Day, and Month

Using a heatmap graph to analyze narcotics-related arrests in San Francisco provides a clear visual representation of when these incidents are most likely to occur. The graph highlights patterns across **hour of the day**, **day of the week**, and **month/year**, offering valuable insights into drug-related activity in the city.

The heatmap provides a compelling visual tool for identifying patterns in narcotics-related arrests:
- **Time-Based Trends**: Hotspots during late afternoon/evening and late-night hours[1][7].
- **Day-Based Trends**: Weekday enforcement peaks; weekend spikes tied to nightlife[1][7][8].
- **Seasonal Stability**: Arrests remain steady across months but may shift year-to-year based on policy changes[1][8].

<iframe src="{{ site.baseurl }}/assets/bokeh.html" width="100%" height="650px" style="border: none;"></iframe>

> The heatmap on this site does not currently support dynamic filtering by year or month. However, you can achieve this interactivity by running the heatmap using a Bokeh server. This setup allows real-time updates based on selected filters. The file can be downloaded [here](https://github.com/puidokas/socialdata2025-group77/blob/main/bokeh_app.py).

## Polar Bar-Chart
<iframe src="{{ site.baseurl }}/assets/drug_narcotic_polar_chart.html" width="100%" height="850px" style="border: none;"></iframe>

> **Figure:** Monthly distribution of DRUG/NARCOTIC crimes over the dataset period.


## Hour of the Day.

The heatmap reveals that narcotics-related arrests peak during the **late afternoon and evening hours**, particularly between **15 and 20**. This period likely corresponds to heightened street-level drug activity and enforcement efforts. A secondary hotspot appears **late at night**, around **23 to 2**, which aligns with nightlife activity and drug trafficking in specific areas. In contrast, early morning hours (4 to 8) are relatively cooler on the heatmap, indicating fewer arrests during this time[1][7].

## Day of the Week

The graph shows increased arrest activity on **weekdays**, especially from **Tuesday to Thursday**, which may be tied to routine law enforcement operations targeting drug markets. While weekends generally appear cooler on the heatmap, hotspots emerge late Friday and Saturday nights, likely reflecting drug use and sales associated with nightlife areas[1][7][8].

## Month of the Year

The heatmap for months shows relatively consistent arrest activity throughout the year, with no significant seasonal spikes. This suggests that narcotics-related crime is less influenced by external factors like weather or holidays compared to other types of crime. However, annual trends may reveal fluctuations due to shifts in law enforcement priorities or public health campaigns targeting drug use[1][8].

# References

1. [Minimaxir: *Analyzing San Francisco Crime Data to Determine When Arrests Happen*](https://minimaxir.com/2015/12/sf-arrests/) - Provides detailed analysis of arrest patterns, including time-of-day and day-of-week trends.  
2. [SF Crime Map: *San Francisco Drug Arrest Dashboard*](https://www.sfcrimemap.org/drugs) - Focused on drug-related arrests with interactive heatmaps.  
3. [San Francisco Police Department Crime Dashboard](https://www.sanfranciscopolice.org/stay-safe/crime-data/crime-dashboard) - Interactive dashboard for analyzing crime statistics over time.  
4. [SF OpenData](https://data.sfgov.org) - Offers raw datasets for creating heatmaps and analyzing crime trends.  
5. [Kaggle: *San Francisco Crime EDA & Classifier*](https://www.kaggle.com/code/georgesaavedra/san-francisco-crime-eda-classifier) - Exploratory data analysis of San Francisco crime datasets, including narcotics incidents.

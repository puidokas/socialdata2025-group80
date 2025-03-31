---
layout: post
title:  "02806 Social Data Analysis: Assignment 2 - Group 77"
date:   2025-03-23 13:26:43 +0100
categories: jekyll update
---

# 1. Introduction of the dataset

## Understanding San Francisco's Crime Data  

San Francisco has long been a city of contrasts—booming industries and persistent challenges, innovation alongside deep-rooted issues. To better understand crime trends over time, we analyzed a dataset that merges two key sources from the **DataSF Open Data Portal**:  

- **Police Department Incident Reports (2003 - May 2018):** This historical dataset contains police-reported crime incidents up until mid-2018. Data was sourced from an older system, which was eventually replaced due to reliability concerns.  
- **Police Department Incident Reports (2018 - Present):** This dataset continues from 2018 onward and is maintained in the **Crime Data Warehouse**, a more stable and comprehensive reporting system.  

## What’s in the Data?  
Each reported incident includes details such as the **type of crime, date and time, police district, and general location (mapped to nearby intersections for privacy)**. 

For example, a record from 2016 might describe a **burglary reported in the Mission District at 2:30 AM**.

## What This Data Tells Us  
By analyzing nearly two decades of crime reports, we can uncover patterns and trends—how crime rates fluctuate over time, how certain offenses become more or less common, and how policy changes or social factors influence reported crime.  

This page will highlight one crime category from the dataset, **DRUG/NARCOTIC**, helping shed light on the evolving nature of crime in San Francisco.

# 2. Heatmap

<iframe src="{{ site.baseurl }}/assets/heatmap.html" width="100%" height="600px" style="border: none;"></iframe>

# 3. Polar Bar-Chart
<iframe src="{{ site.baseurl }}/assets/drug_narcotic_polar_chart.html" width="100%" height="850px" style="border: none;"></iframe>

> **Figure:** Monthly distribution of DRUG/NARCOTIC crimes over the dataset period.Brighter colours show higher numbers of arrests.

# 4. Narcotics-Related Crime Patterns in San Francisco: Trends by Hour, Day, and Month

Using a heatmap graph to analyze narcotics-related arrests in San Francisco provides a clear visual representation of when these incidents are most likely to occur. The graph highlights patterns across **hour of the day**, **day of the week**, and **month/year**, offering valuable insights into drug-related activity in the city.

The heatmap provides a compelling visual tool for identifying patterns in narcotics-related arrests:
- **Time-Based Trends**: Hotspots during late afternoon/evening and late-night hours[1][7].
- **Day-Based Trends**: Weekday enforcement peaks; weekend spikes tied to nightlife[1][7][8].
- **Seasonal Stability**: Arrests remain steady across months but may shift year-to-year based on policy changes[1][8].

<iframe src="{{ site.baseurl }}/assets/bokeh.html" width="100%" height="650px" style="border: none;"></iframe>

> The heatmap on this site does not currently support dynamic filtering by year or month. However, you can achieve this interactivity by running the heatmap using a Bokeh server. This setup allows real-time updates based on selected filters. The file can be downloaded [here](https://github.com/puidokas/socialdata2025-group77/blob/main/bokeh_app.py).

## Hour of the Day.

The heatmap reveals that narcotics-related arrests peak during the **late afternoon and evening hours**, particularly between **15 and 20**. This period likely corresponds to heightened street-level drug activity and enforcement efforts. A secondary hotspot appears **late at night**, around **23 to 2**, which aligns with nightlife activity and drug trafficking in specific areas. In contrast, early morning hours (4 to 8) are relatively cooler on the heatmap, indicating fewer arrests during this time[1][7].

## Day of the Week

The graph shows increased arrest activity on **weekdays**, especially from **Tuesday to Thursday**, which may be tied to routine law enforcement operations targeting drug markets. While weekends generally appear cooler on the heatmap, hotspots emerge late Friday and Saturday nights, likely reflecting drug use and sales associated with nightlife areas[1][7][8].

## Month of the Year

The heatmap for months shows relatively consistent arrest activity throughout the year, with no significant seasonal spikes. This suggests that narcotics-related crime is less influenced by external factors like weather or holidays compared to other types of crime. However, annual trends may reveal fluctuations due to shifts in law enforcement priorities or public health campaigns targeting drug use[1][8].

# 5. Conclusion

When analyzing patterns in drug related arrests in San Francisco there is a clear trend, most incidents are concentrated in neighborhoods like SoMa(South of Market), Tenderloin and Mission District. These all have something else in common, they are part of the city’s largest clusters of SRO(Single-Room Occupancy) buildings. SROs are a type of low-cost housing, providing a single room and often shared bathrooms and minimal facilities. Originally, they were implemented for transient workers but have nowadays become the permanent residence of the city’s most impoverished residents. These same buildings are also the epicenter of San Francisco’s drug related crimes. A 2022 investigation [6] reveals that since 2019, more than 40% of the of the accidental overdose incidents in the Tenderloin and Sixth Street areas took place inside city-funded SROs. In total, in the city of San Francisco, at least 16% of fatal overdoses occur in SROs even though the buildings house less than 1% of the total population. The heatmap visualization in our project makes the connection clear, the highest arrest clusters line up with the SRO-heavy areas. We have pointed out 5 of those SROs which are placed around the highest concentrated arrest areas of the city. One big outlier on why this phenomenon exists is the level of living conditions inside the SROs. A 2022 article [7] reveals that more than 1100 violations cited by inspectors in city-funded SROs were related to unsanitary living conditions. Problems like polluted water supplies, mold-covered rooms and rodent infestations are everyday problems for the residents of those buildings. Conditions like these not only endanger the residents health conditions but may also push them into the use of narcotics, playing a crucial role in the phenomenon we are observing.

# References

1. [Minimaxir: *Analyzing San Francisco Crime Data to Determine When Arrests Happen*](https://minimaxir.com/2015/12/sf-arrests/) - Provides detailed analysis of arrest patterns, including time-of-day and day-of-week trends.  
2. [SF Crime Map: *San Francisco Drug Arrest Dashboard*](https://www.sfcrimemap.org/drugs) - Focused on drug-related arrests with interactive heatmaps.  
3. [San Francisco Police Department Crime Dashboard](https://www.sanfranciscopolice.org/stay-safe/crime-data/crime-dashboard) - Interactive dashboard for analyzing crime statistics over time.  
4. [SF OpenData](https://data.sfgov.org) - Offers raw datasets for creating heatmaps and analyzing crime trends.  
5. [Kaggle: *San Francisco Crime EDA & Classifier*](https://www.kaggle.com/code/georgesaavedra/san-francisco-crime-eda-classifier) - Exploratory data analysis of San Francisco crime datasets, including narcotics incidents.
6. [San Francisco Chronicle: *Overdoses in SROs*](https://www.sfchronicle.com/projects/2022/san-francisco-sros-overdoses/) - Overdose problem in SROs
7. [San Francisco Chronicle: *SRO Living Conditions*](https://www.sfchronicle.com/projects/2022/san-francisco-sros/) - Living conditions in SROs

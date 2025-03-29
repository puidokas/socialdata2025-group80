---
layout: post
title:  "02806 Social Data Analysis: Assignment 2 - Group 77"
date:   2025-03-23 13:26:43 +0100
categories: jekyll update
---

# Introduction of the dataset

# Understanding San Francisco's Crime Data  

San Francisco has long been a city of contrasts—booming industries and persistent challenges, innovation alongside deep-rooted issues. To better understand crime trends over time, we analyzed a dataset that merges two key sources from the **DataSF Open Data Portal**:  

- **Police Department Incident Reports (2003 - May 2018):** This historical dataset contains police-reported crime incidents up until mid-2018. Data was sourced from an older system, which was eventually replaced due to reliability concerns.  
- **Police Department Incident Reports (2018 - Present):** This dataset continues from 2018 onward and is maintained in the **Crime Data Warehouse**, a more stable and comprehensive reporting system.  

## What’s in the Data?  
Each reported incident includes details such as the **type of crime, date and time, police district, and general location (mapped to nearby intersections for privacy)**. 

For example, a record from 2016 might describe a **burglary reported in the Mission District at 2:30 AM**.

## What This Data Tells Us  
By analyzing nearly two decades of crime reports, we can uncover patterns and trends—how crime rates fluctuate over time, how certain offenses become more or less common, and how policy changes or social factors influence reported crime.  

This page will highlight one crime category from the dataset, DRUG/NARCOTIC, helping shed light on the evolving nature of crime in San Francisco.

# Heatmap

<iframe src="{{ site.baseurl }}/assets/heatmap.html" width="100%" height="600px" style="border: none;"></iframe>

---

# Dynamic visualization

<iframe src="{{ site.baseurl }}/assets/bokeh.html" width="100%" height="650px" style="border: none;"></iframe>

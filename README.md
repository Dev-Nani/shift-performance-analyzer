﻿# shift-performance-analyzer
# Shift Performance Analyzer

A Python tool that compares productivity KPIs across A/B/C shifts in an aluminum extrusion plant.

## Features
- Input: Daily production data
- KPIs: Output/hour, Downtime/hour, Scrap Ratio
- Ranks shifts based on average performance
- Saves results as CSV + bar chart

## How to Run

```bash
pip install -r requirements.txt
python src/analyze_shifts.py

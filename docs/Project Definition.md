# Project Definition – Training Report Generator

## Goal

Build an automated analytics system that generates weekly, monthly and yearly
training reports based on running activities.

## Motivation

- Track training progress
- Analyze training load
- Identify trends in performance

## Core Questions

- How much did I train this week?
- How did training load change compared to last week?
- Are there trends in pace or heart rate?
- Is training consistent?
- Did I accomplish my training goal?

## Definition of Done

A task is considered complete when:

- the feature is implemented
- the code runs without errors
- the result is reproducible
- the functionality is documented
- the output is correctly integrated into the report

## Target Users

Primary user: the athlete (myself) who wants to analyze training progress,
training load and long-term performance trends.

## Data Source

Strava API

Key fields:

- distance
- moving_time
- elevation_gain
- average_heartrate
- start_date

## Metrics

Weekly, Monthly and Yearly metrics:

- distance
- elevation
- avg_pace_per_km
- training_days
- total_hours
- longest_run

Derived metrics:

- training_load
- long_run_ratio
- interval_training_ratio
- rolling_distance

## Report Types

The system generates three types of reports:

- Weekly report – short-term training summary
- Monthly report – medium-term training trends
- Yearly report – long-term performance overview

## Output

Weekly, Monthly and Yearly report including:

- volume summary
- elevation summary
- pace trends
- training consistency
- visualizations
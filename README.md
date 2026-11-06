# Community Dataset Explorer – Student Performance Analysis

## Overview

This project analyzes student performance data to explore how weekly study time and school absences relate to students' final grades.

The dataset contains information about 395 students, including study time, absences, and final grades. It is the Student Performance dataset from the UCI Machine Learning Repository.

Dataset source: https://archive.ics.uci.edu/dataset/320/student+performance

The purpose of this software is to explore educational data, identify patterns in student performance, calculate statistics, and present findings using charts. This project helps me develop my skills in Python programming and data analysis.

**Software Demo Video:**  
[(https://www.youtube.com/watch?v=7QsGza8XTZU)]

## Data Analysis Results

This project explores three main questions:

**1. How does weekly study time relate to students' final grades?**

Students in study-time category 3 had the highest average final grade, approximately 11.40 out of 20. Category 4 followed with approximately 11.26.

**2. How do school absences relate to students' final grades?**

Students with 1–3 absences had the highest average final grade, approximately 11.91 out of 20. Students with zero absences had an average of approximately 8.44.

**3. How do previous class failures relate to students' final grades?**

Students with zero past class failures had the highest average final grade, approximately 11.25 out of 20. Students with one, two, and three past failures had progressively lower average final grades. This suggests that previous class failures are associated with lower academic performance.

**Conclusion:**

The analysis shows differences in average final grades across study-time and absence groups. Study time and school attendance are useful factors to explore when understanding student performance. These results show patterns in this dataset and do not prove that one factor directly causes a particular grade.

## Development Environment

The software was developed using:

- Visual Studio Code
- Python 3.13
- Windows operating system

**Programming Language and Libraries:**

- Python – Main programming language.
- Pandas – Used to load, organize, group, and analyze the dataset.
- Matplotlib – Used to create bar charts and visualize the analysis results.

**Dataset File:** `data/student-mat.csv`

## Useful Websites

- [UCI Machine Learning Repository – Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance)
- [Python Official Website](https://www.python.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)

## Future Work

- Add more analysis questions about student performance.
- Create additional charts to explore other factors in the dataset.
- Improve the program by allowing users to select which data they want to analyze.
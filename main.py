
# Community Dataset Explorer
# CSE 310 - Applied Programming
# Project: Student Performance Analysis
# This program explores education data using Python.

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------
# FUNCTION 1: LOAD THE STUDENT DATASET
# -----------------------------------------

def load_data():
    """Load the student dataset from the CSV file."""

    data = pd.read_csv("data/student-mat.csv", sep=";")

    print("Dataset loaded successfully!")

    return data


# -----------------------------------------
# FUNCTION 2: DISPLAY DATASET OVERVIEW
# -----------------------------------------

def show_overview(data):
    """Display student records and dataset statistics."""

    print("\n===================================")
    print("     COMMUNITY DATASET EXPLORER")
    print("       STUDENT PERFORMANCE")
    print("===================================")

    # Display the first five student records
    print("\nFirst five student records:")
    print(data.head())

    # Display dataset information
    print("\nDataset information:")
    print("Total students:", len(data))
    print("Total columns:", len(data.columns))

    # Display available column names
    print("\nAvailable columns:")
    print(data.columns.tolist())

    # Display final grade statistics
    print("\nFinal Grade Statistics:")
    print(data["G3"].describe())


# -----------------------------------------
# FUNCTION 3: ANALYSE STUDY TIME
# -----------------------------------------

def analyze_study_time(data):
    """Analyse the relationship between study time and grades."""

    # Calculate average final grades for each study-time group
    study_analysis = data.groupby("studytime")["G3"].mean()

    # Display the results
    print("\nAverage Final Grade by Study Time:")
    print(study_analysis)

    # Sort the results from highest to lowest
    print("\nStudy Time Analysis (Highest to Lowest):")
    print(study_analysis.sort_values(ascending=False))

    # Create a bar chart
    study_analysis.plot(
        kind="bar",
        title="Average Final Grade by Weekly Study Time",
        xlabel="Study Time Category",
        ylabel="Average Final Grade",
        rot=0
    )

    # Display the chart
    plt.tight_layout()
    plt.show()

    return study_analysis


# -----------------------------------------
# FUNCTION 4: ANALYSE SCHOOL ABSENCES
# -----------------------------------------

def analyze_absences(data):
    """Group school absences and compare average final grades."""

    # Create categories based on the number of absences
    absence_bins = [-1, 0, 3, 6, float("inf")]
    absence_labels = ["0", "1-3", "4-6", "7 or more"]

    # Convert absence numbers into categories
    data["absence_group"] = pd.cut(
        data["absences"],
        bins=absence_bins,
        labels=absence_labels
    )

    # Calculate average final grades for each group
    absence_analysis = data.groupby(
        "absence_group", observed=False
    )["G3"].mean()

    # Display the results
    print("\nAverage Final Grade by Absence Group:")
    print(absence_analysis)

    # Sort the results from highest to lowest
    print("\nAbsence Analysis (Highest to Lowest):")
    print(absence_analysis.sort_values(ascending=False))

    # Create a bar chart
    absence_analysis.plot(
        kind="bar",
        title="Average Final Grade by Number of Absences",
        xlabel="Number of Absences",
        ylabel="Average Final Grade",
        rot=0
    )

    # Display the chart
    plt.tight_layout()
    plt.show()

    return absence_analysis

# -----------------------------------------
# FUNCTION 5: ANALYSE PAST CLASS FAILURES
# -----------------------------------------

def analyze_failures(data):
    """Analyse the relationship between past failures and final grades."""

    # Group students by the number of past class failures
    failure_analysis = data.groupby("failures")["G3"].mean()

    # Display the results
    print("\nAverage Final Grade by Past Class Failures:")
    print(failure_analysis)

    # Sort the results from highest to lowest
    print("\nFailure Analysis (Highest to Lowest):")
    print(failure_analysis.sort_values(ascending=False))

    # Create a bar chart
    failure_analysis.plot(
        kind="bar",
        title="Average Final Grade by Past Class Failures",
        xlabel="Number of Past Failures",
        ylabel="Average Final Grade",
        rot=0
    )

    # Display the chart
    plt.tight_layout()
    plt.show()

    return failure_analysis


# -----------------------------------------
# FUNCTION 6: DISPLAY PROJECT FINDINGS
# -----------------------------------------

def show_summary(study_analysis, absence_analysis, failure_analysis):
    """Display the main findings from all three analyses."""

    print("\n===================================")
    print("         PROJECT FINDINGS")
    print("===================================")

    # Finding 1: Study Time
    best_study_group = study_analysis.idxmax()

    print("\nFinding 1: Study Time")
    print("Study-time category", best_study_group)
    print("had the highest average final grade of",
          round(study_analysis.max(), 2))

    # Finding 2: School Absences
    best_absence_group = absence_analysis.idxmax()

    print("\nFinding 2: School Absences")
    print("Students in the", best_absence_group,
          "absence group had the highest average final grade of",
          round(absence_analysis.max(), 2))

    # Finding 3: Past Class Failures
    best_failure_group = failure_analysis.idxmax()

    print("\nFinding 3: Past Class Failures")
    print("Students with", best_failure_group,
          "past failures had the highest average final grade of",
          round(failure_analysis.max(), 2))

    # Project conclusion
    print("\nConclusion:")
    print("Study time, school attendance, and")
    print("past class failures are useful factors")
    print("to explore when understanding student performance.")

    print("\nThank you for using Community Dataset Explorer!")


# -----------------------------------------
# MAIN FUNCTION: RUN THE COMPLETE PROGRAM
# -----------------------------------------


def main():
    """Run all Community Dataset Explorer features."""

    # Load the student dataset
    data = load_data()

    # Display the dataset overview
    show_overview(data)

    # Analyse study time
    study_results = analyze_study_time(data)

    # Analyse school absences
    absence_results = analyze_absences(data)

    # Analyse past class failures
    failure_results = analyze_failures(data)

    # Display the final project findings
    show_summary(study_results, absence_results, failure_results)


# Start the program
if __name__ == "__main__":
    main()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("datasets/FOAI-assignment2-1.csv")


def plot_histogram(
    df, column_name, bins=30, title=None, xlabel=None, ylabel="Frequency"
):
    plt.figure(figsize=(10, 6))

    plt.hist(df[column_name], bins=bins, alpha=0.7, color="skyblue", edgecolor="black")

    if title is None:
        title = f"Histogram of {column_name}"
    plt.title(title)

    if xlabel is None:
        xlabel = column_name
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


plot_histogram(data, "salary_in_usd", 10, "Salary Ranges for Data Scientists in USD")


def plot_pie_chart(df, column_name, title, threshold=3.0):
    # Count the number of unique values in the column
    value_counts = df[column_name].value_counts()
    # Calculate percentages
    total = value_counts.sum()
    percentages = (value_counts / total) * 100

    # Separate values above and below threshold
    above_threshold = value_counts[percentages >= threshold]
    below_threshold = value_counts[percentages < threshold]

    # Create new data with "Others" category
    if len(below_threshold) > 0:
        others_count = below_threshold.sum()
        final_counts = above_threshold.copy()
        final_counts["Others"] = others_count
    else:
        final_counts = above_threshold

    # Create the pie chart
    plt.figure(figsize=(10, 8))

    plt.pie(
        final_counts.values,
        labels=final_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title(f"{title}\n(Values < {threshold}% grouped as 'Others')")
    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()


plot_pie_chart(data, "job_title", "Job Title Proportions for Data Scientists", 3.0)


def plot_avg_salary_by_year(df):
    avg_salary_by_year = df.groupby("work_year")["salary_in_usd"].mean()
    plt.figure(figsize=(10, 8))
    plt.plot(avg_salary_by_year.index, avg_salary_by_year.values, marker="o")
    plt.xticks(avg_salary_by_year.index)
    plt.title("Average Salary of Data Scientists by Work Year (2020-2023)")
    plt.xlabel("Work Year")
    plt.ylabel("Average Salary (USD)")
    plt.show()


plot_avg_salary_by_year(data)


def box_plot(df, x_col, y_col, order=None):
    plt.figure(figsize=(10, 8))
    df_plot = df.copy()
    if order is not None:
        df_plot[x_col] = pd.Categorical(df_plot[x_col], categories=order, ordered=True)
    sns.boxplot(x=x_col, y=y_col, data=df_plot)

    plt.title(f"Box Plot of {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


box_plot(data, "experience_level", "salary_in_usd", order=["EN", "MI", "SE", "EX"])
box_plot(data, "employment_type", "salary_in_usd", order=["FT", "PT", "CT", "FL"])


def scatter_plot(df, x_col, y_col, order=None):
    plt.figure(figsize=(10, 8))
    df_plot = df.copy()
    if order is not None:
        df_plot[x_col] = pd.Categorical(df_plot[x_col], categories=order, ordered=True)
    sns.scatterplot(x=x_col, y=y_col, data=df_plot)

    plt.title(f"Scatter Plot of {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


scatter_plot(data, "experience_level", "salary_in_usd", order=["EN", "MI", "SE", "EX"])
scatter_plot(data, "employment_type", "salary_in_usd", order=["FT", "PT", "CT", "FL"])

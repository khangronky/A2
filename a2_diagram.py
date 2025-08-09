import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_pie_chart(df, column_name, title, threshold=3.0):
    # Count the number of unique values in the column
    value_counts = df[column_name].value_counts()
    print("Original value counts:")
    print(value_counts)

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

    print(f"\nAfter grouping (threshold: {threshold}%):")
    print(final_counts)
    print(f"\nFinal percentages:")
    for label, count in final_counts.items():
        print(f"{label}: {(count/total)*100:.1f}%")

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


def plot_avg_salary_by_year(df):
    avg_salary_by_year = df.groupby("work_year")["salary_in_usd"].mean()
    plt.figure(figsize=(10, 8))
    plt.plot(avg_salary_by_year.index, avg_salary_by_year.values, marker="o")
    plt.xticks(avg_salary_by_year.index)
    plt.title("Average Salary of Data Scientists by Work Year (2020-2023)")
    plt.xlabel("Work Year")
    plt.ylabel("Average Salary (USD)")
    plt.show()


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


def correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        center=0,
        square=True,
        fmt=".2f",
    )
    plt.title("Correlation Matrix of Numerical Variables")
    plt.tight_layout()
    plt.show()


data = pd.read_csv("datasets/FOAI-assignment2-1.csv")
correlation_matrix(data)

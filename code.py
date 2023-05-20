import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from a file
def load_data(file_path):
    data = pd.read_csv(file_path)  # Modify this line for different file formats
    return data

# Function to perform exploratory data analysis (EDA)
def perform_eda(data):
    # Display summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Display data types of columns
    print("\nData Types:")
    print(data.dtypes)

    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

# Function to generate a bar plot
def generate_bar_plot(data, x, y):
    plt.bar(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Bar Plot")
    plt.show()

# Function to generate a line chart
def generate_line_chart(data, x, y):
    plt.plot(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Line Chart")
    plt.show()

# Function to generate a scatter plot
def generate_scatter_plot(data, x, y):
    plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Scatter Plot")
    plt.show()

# Function to generate a histogram
def generate_histogram(data, column):
    plt.hist(data[column], bins=10)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

# Main function
def main():
    file_path = "data.csv"  # Modify this line with the path to your data file

    # Load data
    data = load_data(file_path)

    # Perform exploratory data analysis (EDA)
    perform_eda(data)

    # Generate visualizations
    generate_bar_plot(data, "Category", "Value")
    generate_line_chart(data, "Date", "Value")
    generate_scatter_plot(data, "X", "Y")
    generate_histogram(data, "Value")

# Run the main function
if __name__ == "__main__":
    main()

# Automobile-MPG-Analysis
Data Cleaning, Feature Engineering & Visualization using Pandas • NumPy • Matplotlib • Seaborn

This project performs a complete Exploratory Data Analysis (EDA) on the classic Automobile MPG dataset.
It showcases essential data-science skills including:

✔ Data loading
✔ Data cleaning
✔ Handling missing values
✔ Feature engineering
✔ Visual analysis
✔ Statistical summarization

📁 Project Structure
├── mpg_analysis.py       # Main Python script
├── weather_data.csv      # (Only if you add your file)
├── README.md             # Project documentation

🔧 Technologies Used

Python 3.x

Pandas – Data manipulation

NumPy – Numerical operations

Matplotlib – Plotting

Seaborn – Statistical visualizations

📊 Key Features
1. Data Loading

Loads the MPG dataset directly from Seaborn.

2. Data Cleaning

Handles missing values using median imputation (NumPy).

Drops unused fields.

Inspects dataset structure and summary.

3. Feature Engineering

Creates a new categorical column: Weight Category
(Light, Medium, Heavy, Very Heavy)

4. Data Visualization

Includes multiple high-quality visualizations:

Histogram + KDE of MPG

Scatter plot of MPG vs Weight

Box plot of MPG by origin

PairPlot of major numerical features

Bar chart of MPG by cylinder count

5. Statistical Summary

Generates descriptive stats grouped by country of origin, including:
mean, median, std, min, max.

📈 Sample Insights

Lighter vehicles tend to have higher fuel efficiency.

Cars from different regions show unique MPG patterns.

Displacement, horsepower, and weight strongly correlate with MPG.

🚀 How to Run This Project
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install dependencies
pip install pandas numpy matplotlib seaborn

3. Run the script
python mpg_analysis.py

📚 Learnings from the Project

By completing this analysis, you gain experience in:

Data wrangling with Pandas

Working with missing values

Applying NumPy for numerical preprocessing

Visual storytelling using Matplotlib & Seaborn

Exploratory data analysis workflows

Building a clean and readable Python script

🤝 Contributions

Pull requests are welcome!
Feel free to fork the repo and enhance the analysis or add new visualizations.

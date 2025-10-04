#Student Performance Analysis using Python

📌 Overview
This project analyzes student performance data using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.
It explores how different factors (like gender, parental education, and study hours) affect students’ math, reading, and writing scores.

🧰 Technologies Used
Python 3
NumPy
Pandas
Matplotlib
Seaborn

📊 Features
Load and clean dataset (handle null values, drop unnecessary columns).
Modify or standardize inconsistent data formats.
Perform group-wise analysis:
 1.By Parent Education
 2.By Marital Status
 3.Detect outliers using boxplots.
Analyze gender distribution and ethnic group composition using visualizations.

📈 Visualizations
The project uses various plots to show insights:
 1.Countplot → For Gender Distribution
 2.Heatmap → For Average Scores by Parental Education and Marital Status
 3.Boxplot → For Outlier Detection
 4.Pie Chart → For Ethnic Group Distribution

🗂️ Dataset
The dataset used is named student_scores.csv, containing columns such as:
Gender
ParentEduc
ParentMaritalStatus
EthnicGroup
MathScore
ReadingScore
WritingScore
WklyStudyHours

⚙️ How to Run
Clone the repository: git clone https://github.com/AjayPrajapati030409/student-performance-analysis.git
Install dependencies: pip install pandas numpy matplotlib seaborn
Run the script: python student_analysis.py

📌 Output Example
Heatmaps showing score averages
Pie chart showing ethnic group distribution
Boxplot showing score outliers

🧠 Insights
Parental education and marital status have noticeable effects on student performance.
Some students spend fewer study hours yet score higher, indicating other influencing factors.
Ethnic group distribution helps identify demographic variations.

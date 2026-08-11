# Netflix Data Analysis & Business Insights

An end-to-end Netflix data analysis project focused on **data cleaning, exploratory data analysis, business insights, visualization, and interactive dashboard development using Streamlit**.

The project was completed through multiple analytical tasks and includes the raw dataset, cleaned dataset, Jupyter notebooks, visualizations, presentation, and an interactive Streamlit application.

---

## Project Overview

The objective of this project is to transform raw Netflix content data into a clean, analysis-ready dataset and generate meaningful business insights from it.

The project covers:

- Data cleaning and preparation
- Missing-value analysis
- Duplicate detection
- Categorical data inspection
- Country-wise content analysis
- Movie vs TV Show analysis
- Release-year trend analysis
- Business insight generation
- Data visualization
- Interactive Streamlit dashboard

---

## Dataset

The project uses a Netflix titles dataset containing information about movies and TV shows available on Netflix.

### Main columns

| Column | Description |
|---|---|
| `show_id` | Unique identifier for each title |
| `type` | Movie or TV Show |
| `title` | Title name |
| `director` | Director information |
| `country` | Country associated with the title |
| `date_added` | Date the title was added to Netflix |
| `release_year` | Original release year |
| `rating` | Content rating |
| `duration` | Movie duration or number of seasons |
| `listed_in` | Genres/categories |

The original dataset and cleaned dataset are both included in the repository.

---

# Project Tasks

## Task 1 — Netflix Data Cleaning & Preparation

### Objective

Prepare the Netflix dataset for reliable business analysis and reporting.

### Work performed

- Imported the dataset using Python and Pandas
- Inspected dataset structure and data types
- Checked missing values
- Investigated categorical columns using unique values and cardinality
- Identified placeholder values such as `Not Given`
- Checked duplicate records
- Investigated inconsistent categorical values
- Evaluated whether missing information could be reliably recovered
- Preserved missing information where reliable inference was not possible
- Standardized important categorical columns
- Exported the cleaned dataset for further analysis

### Important data-quality decision

Missing values were not blindly filled using assumptions.

For example, director information marked as `Not Given` was not artificially assigned based on country, genre, or other indirect relationships. A value was considered for recovery only when there was strong evidence, such as an exact matching title with known information.

This approach helps prevent introducing incorrect information into the dataset.

---

# Task 2 — Content Type Analysis

### Objective

Analyze the distribution of Movies and TV Shows available on Netflix.

### Analysis performed

The `type` column was analyzed to calculate the total number of:

- Movies
- TV Shows

### Visualization

A bar chart was created to compare Movies and TV Shows.

### Key Insight

Movies represent the larger share of Netflix titles in the analyzed dataset, while TV Shows form a smaller portion.

---

# Task 3 — Country-Wise Netflix Content Analysis

### Objective

Analyze Netflix content availability across different countries.

### Analysis performed

- Inspected country values
- Checked country formatting and missing placeholders
- Calculated content count by country
- Identified the top content-producing countries
- Ranked countries by number of titles
- Calculated the contribution of the top 10 countries compared with the remaining countries

### Visualizations

- Top 10 countries bar chart
- Top 10 countries vs remaining countries pie chart

### Key Insight

The United States contributes the largest number of titles in the dataset, followed by other major content-producing countries such as India and the United Kingdom.

---

# Task 4 — Trend Analysis by Release Year

### Objective

Analyze how Netflix content production has changed over time.

### Analysis performed

- Validated the `release_year` column
- Confirmed its numerical data type
- Checked the minimum and maximum release years
- Grouped titles by release year
- Calculated yearly content counts
- Calculated changes between years
- Identified the highest production year
- Identified the largest increase and decline in yearly content counts

### Visualization

A release-year trend line chart was created to show changes in Netflix content production over time.

### Key Insight

Netflix content production increased substantially during the 2010s and reached its highest yearly content count around 2018 in the analyzed dataset.

---

# Interactive Streamlit Dashboard

The project includes an interactive dashboard built with **Streamlit**.

### Dashboard features

- Dataset overview
- Total title count
- Movie count
- TV Show count
- Country count
- Content type visualization
- Top 10 country analysis
- Country contribution comparison
- Release-year trend
- Dataset explorer

### Dataset Explorer

The dashboard provides a simple interactive section where users can select:

- X-Axis
- Y-Axis

and generate a visualization based on the selected columns.

The dashboard intentionally keeps the interface minimal so that the important analytical results remain easy to understand.

---

# Project Files

```text
netflix-data-analysis-dashboard/
│
├── DATA ANALYSIS USING PYTHON TASK LIST.pdf
│
├── Netflix-Data-Analysis-and-Business-Insights.pptx
│
├── Netflix_Cleaned_Dataset.csv
│
├── netflix_raw.csv
│
├── README.md
│
├── Task_1_Netflix_Data_Analysis.ipynb
│
├── Task_2_&_3_Netflix_Data_Analysis.ipynb
│
├── app.py
│
├── requirement.txt.txt
│
├── overview.png
│
├── task2-content-type-1.png
├── task2-content-type-2.png
│
├── task3-country-analysis-1.png
├── task3-country-analysis-2.png
│
├── task4-release-trend-1.png
└── task4-release-trend-2.png
```

### Notebook organization

The Jupyter notebooks are organized to keep the analysis traceable:

- `Task_1_Netflix_Data_Analysis.ipynb` contains the Task 1 analysis, questions/steps, and data-cleaning work.
- `Task_2_&_3_Netflix_Data_Analysis.ipynb` contains the analysis, solutions, calculations, and visualizations for Tasks 2 and 3.

The PDF provided with the project contains the original task requirements and workflow.

---

# Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Jupyter Notebook | Exploratory analysis |
| Streamlit | Interactive dashboard |
| Git | Version control |
| GitHub | Project hosting |

---

# How to Run the Dashboard

## 1. Clone the repository

```bash
git clone https://github.com/Khushal-dak/netflix-data-analysis-dashboard.git
```

## 2. Open the project folder

```bash
cd netflix-data-analysis-dashboard
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Streamlit

```bash
streamlit run app.py
```

The dashboard will open automatically in the browser.

---

# Business Insights

The analysis provides several useful observations:

- Movies make up the majority of Netflix titles in the dataset.
- The United States is the largest content-producing country.
- The top content-producing countries account for a significant share of the dataset.
- Netflix content production increased strongly during the 2010s.
- 2018 has the highest yearly content count in the analyzed data.
- The cleaned dataset provides a more reliable foundation for further analysis and reporting.

---

# Data Quality Approach

The project follows a practical data-quality workflow rather than applying automatic transformations without validation.

The general process was:

```text
Raw Dataset
     ↓
Dataset Inspection
     ↓
Missing Value Analysis
     ↓
Categorical Value Analysis
     ↓
Duplicate Check
     ↓
Inconsistency Check
     ↓
Data Cleaning
     ↓
Validation
     ↓
Cleaned Dataset
     ↓
Analysis & Visualization
     ↓
Business Insights
     ↓
Streamlit Dashboard
```

This makes the analysis reproducible and keeps the reasoning behind data-cleaning decisions traceable.

---

# Project Presentation

A project presentation is also included:

**`Netflix-Data-Analysis-and-Business-Insights.pptx`**

It summarizes the project tasks, analysis, visualizations, and key findings.

---

# Screenshots

The repository also contains screenshots of the major visualizations and dashboard outputs, including:

- Dataset overview
- Content type analysis
- Country analysis
- Release-year trend analysis
- Dashboard visualizations

---

# Author

## Khushal Dak

**B.Tech — Computer Science Engineering**

Techno NJR Institute of Technology

GitHub: [Khushal-dak](https://github.com/Khushal-dak)

---

## Project Focus

**Data Cleaning → Exploratory Data Analysis → Visualization → Business Insights → Interactive Dashboard**

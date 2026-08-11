# 🎬 Netflix Data Analysis & Business Insights

> **Raw Data → Clean Data → Analysis → Visualization → Business Insights → Interactive Dashboard**

An end-to-end **Netflix Data Analysis project** built using **Python, Pandas, Matplotlib, Jupyter Notebook and Streamlit**.

The project focuses on **data cleaning, exploratory data analysis, visualization, business insight generation and interactive dashboard development**.

## 🖥️ Dashboard Preview

![Streamlit Dashboard](overview.png)

> **Minimal interface. Clear visualizations. Business-focused insights.**
---

## 🚀 Project at a Glance

| Metric | Value |
|---|---:|
| 🎬 Total Titles | **8,790** |
| 🎥 Movies | **6,126** |
| 📺 TV Shows | **2,664** |
| 🌍 Countries | **86** |
| 🧹 Data Cleaning | ✅ Completed |
| 📊 Data Visualization | ✅ Completed |
| 🌐 Streamlit Dashboard | ✅ Completed |

---

## 🎯 Project Objective

The objective of this project is to prepare, analyze and visualize Netflix content data for **business analytics and reporting**.

The project follows a structured workflow starting from raw data inspection and cleaning, followed by analysis, visualization and business insight generation.

### Key Questions

- 🎬 How is Netflix content distributed between Movies and TV Shows?
- 🌍 Which countries contribute the most Netflix content?
- 📈 How has Netflix content production changed over the years?
- 📊 What meaningful patterns can be identified from the dataset?
- 🌐 How can the findings be presented through an interactive dashboard?

---

## 🔄 Overall Project Workflow

```text
📁 Raw Netflix Dataset
        ↓
🔍 Data Inspection
        ↓
🧹 Data Cleaning & Preparation
        ↓
📊 Exploratory Data Analysis
        ↓
📈 Visualization
        ↓
💡 Business Insights
        ↓
🌐 Interactive Streamlit Dashboard
```

---

# 📂 Dataset

The project uses a Netflix titles dataset containing information about **Movies and TV Shows**.

### Main Columns

| Column | Description |
|---|---|
| `show_id` | Unique identifier for each title |
| `type` | Movie or TV Show |
| `title` | Name of the title |
| `director` | Director information |
| `country` | Country associated with the title |
| `date_added` | Date added to Netflix |
| `release_year` | Original release year |
| `rating` | Content rating |
| `duration` | Movie duration / number of seasons |
| `listed_in` | Genres / categories |

The repository contains both the **raw dataset** and the **cleaned dataset**.

---

# 🧹 Task 1 — Netflix Data Cleaning & Preparation

## 📌 Task Description

Prepare and organize the Netflix dataset for **business analytics and reporting**.

## 🔄 Task Workflow

1. Import the dataset using Python and Pandas.
2. Identify and handle missing values.
3. Remove duplicate records and formatting inconsistencies.
4. Standardize columns such as **Country, Rating and Type**.
5. Export the cleaned dataset for analysis.

## 🧠 Skills You Will Learn

- Pandas Fundamentals
- Data Cleaning
- Data Preprocessing
- Data Quality Management

## 🔑 Key Features

- Data Import
- Missing Value Handling
- Data Cleaning
- Dataset Preparation

## 🔧 Work Performed

During the implementation:

- Imported the dataset using Python and Pandas
- Inspected dataset structure and data types
- Checked missing values
- Examined categorical columns
- Checked categorical cardinality
- Identified placeholder values such as `Not Given`
- Checked duplicate records
- Investigated categorical inconsistencies
- Validated Country, Rating and Type columns
- Evaluated missing information carefully
- Standardized important categorical columns
- Exported the cleaned dataset

## 🛡️ Data Quality Approach

Missing information was **not blindly replaced**.

Where reliable evidence was unavailable, the missing information was preserved rather than introducing potentially incorrect values.

This approach helps maintain **data integrity and analytical reliability**.

---

# 🎬 Task 2 — Content Type Analysis Dashboard

## 📌 Task Description

Analyze the distribution of **Movies and TV Shows** available on Netflix.

## 🔄 Task Workflow

1. Load the cleaned dataset.
2. Calculate the total number of Movies and TV Shows.
3. Create visualizations for content distribution.
4. Compare content proportions.
5. Summarize key findings.

## 🧠 Skills You Will Learn

- Data Visualization
- Matplotlib
- Seaborn
- Exploratory Data Analysis

## 🔑 Key Features

- Content Analysis
- Charts & Visualizations
- Distribution Insights
- Summary Report

## 📄 Task Requirements

![Task 2 Requirements](task2-content-type-1.png)

## 📊 Analysis Performed

The `type` column was analyzed to calculate the total number of Movies and TV Shows.

### Results

- 🎬 Movies: **6,126**
- 📺 TV Shows: **2,664**
- 📊 Total Titles: **8,790**

## 📈 Visualization

![Task 2 Content Distribution](task2-content-type-2.png)

## 💡 Key Finding

**Movies represent the majority of Netflix titles**, while TV Shows form a comparatively smaller portion of the dataset.

---

# 🌍 Task 3 — Country-Wise Netflix Content Analysis

## 📌 Task Description

Analyze Netflix content availability across different countries.

## 🔄 Task Workflow

1. Extract and clean country information.
2. Calculate content count by country.
3. Identify top content-producing countries.
4. Create charts and rankings.
5. Generate business insights.

## 🧠 Skills You Will Learn

- GroupBy Operations
- Data Aggregation
- Business Analytics
- Visualization Techniques

## 🔑 Key Features

- Country Analysis
- Ranking Reports
- Geographic Insights
- Data Visualization

## 📄 Task Requirements

![Task 3 Requirements](task3-country-analysis-1.png)

## 📊 Analysis Performed

The country column was analyzed to:

- Examine country values
- Calculate country-wise content counts
- Rank countries by content volume
- Identify the Top 10 content-producing countries
- Compare the Top 10 countries with the remaining countries

## 📈 Country Analysis Results

![Task 3 Country Analysis](task3-country-analysis-2.png)

## 💡 Key Findings

The **United States** contributes the largest number of titles in the analyzed dataset, followed by other major content-producing countries including **India and the United Kingdom**.

The analysis also compares the contribution of the **Top 10 countries against the remaining countries**.

---

# 📈 Task 4 — Netflix Content Trend Analysis

## 📌 Task Description

Analyze Netflix content production trends over different release years.

## 🔄 Task Workflow

1. Load the cleaned dataset.
2. Group content by release year.
3. Calculate yearly content counts.
4. Analyze growth and decline trends.
5. Create visualizations.
6. Summarize key findings.

## 🧠 Skills Applied

- Data Aggregation
- Time-Based Analysis
- Trend Analysis
- Data Visualization
- Insight Generation

## 🔑 Key Features

- Release-Year Analysis
- Yearly Content Counts
- Growth & Decline Analysis
- Trend Visualization
- Business Insights

## 📄 Task Analysis

The `release_year` column was validated before performing the analysis.

The analysis included:

- Checking the data type
- Checking the minimum and maximum release years
- Grouping titles by release year
- Calculating yearly content counts
- Calculating year-over-year percentage changes
- Identifying the highest production year
- Identifying major growth and decline periods

## 📈 Visualization

![Netflix Release Year Trend](task4-release-trend-1.png)

## 📊 Detailed Analysis

![Netflix Release Trend Analysis](task4-release-trend-2.png)

## 💡 Key Finding

Netflix content production increased significantly during the **2010s**, reaching its highest yearly content count around **2018** in the analyzed dataset.

The trend highlights a major expansion of Netflix's content library during the mid-to-late 2010s.

---

# 🌐 Interactive Streamlit Dashboard

The project includes an interactive **Streamlit dashboard** that brings the major findings together into a simple analytical interface.

## 📊 Dashboard Features

- 📊 Dataset Overview
- 🎬 Movie Count
- 📺 TV Show Count
- 🌍 Country Count
- 📈 Content Type Analysis
- 🏆 Top 10 Countries
- 🥧 Country Contribution Analysis
- 📅 Release-Year Trend
- 🔎 Dataset Explorer

## 🔎 Dataset Explorer

Users can select:

```text
X-Axis
   +
Y-Axis
   ↓
Visualization
```

This provides a simple way to explore relationships between available dataset columns.
---

# 💡 Consolidated Business Insights

### 🎬 Content Strategy

Movies form the majority of titles in the analyzed Netflix dataset, indicating a stronger representation of movie content compared with TV Shows.

### 🌍 Geographic Distribution

The United States is the largest contributor of Netflix titles, while India and the United Kingdom are also major content-producing markets.

### 📈 Historical Growth

Netflix content production expanded rapidly during the 2010s, with the highest yearly title count occurring around **2018** in the analyzed dataset.

### 📊 Content Concentration

The Top 10 content-producing countries account for a substantial portion of the overall content, highlighting geographic concentration within the Netflix content library.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Data analysis & processing |
| 🐼 Pandas | Data cleaning & manipulation |
| 🔢 NumPy | Numerical operations |
| 📊 Matplotlib | Data visualization |
| 📓 Jupyter Notebook | Exploratory analysis |
| 🌐 Streamlit | Interactive dashboard |
| 🔧 Git | Version control |
| 🐙 GitHub | Project hosting |

---

# 📁 Project Structure

```text
netflix-data-analysis-dashboard/
│
├── 📄 DATA ANALYSIS USING PYTHON TASK LIST.pdf
├── 📊 Netflix-Data-Analysis-and-Business-Insights.pptx
│
├── 📄 netflix_raw.csv
├── 📄 Netflix_Cleaned_Dataset.csv
│
├── 📓 Task_1_Netflix_Data_Analysis.ipynb
├── 📓 Task_2_&_3_Netflix_Data_Analysis.ipynb
│
├── 🌐 app.py
├── 📄 requirements.txt
├── 📄 README.md
│
├── 🖼️ overview.png
├── 🖼️ task2-content-type-1.png
├── 🖼️ task2-content-type-2.png
├── 🖼️ task3-country-analysis-1.png
├── 🖼️ task3-country-analysis-2.png
├── 🖼️ task4-release-trend-1.png
└── 🖼️ task4-release-trend-2.png
```

---

# 📓 Analysis Notebooks

## Task 1

`Task_1_Netflix_Data_Analysis.ipynb`

Contains the complete data cleaning and preparation workflow.

### Includes

- Data inspection
- Missing-value analysis
- Duplicate checking
- Categorical analysis
- Data quality checks
- Data cleaning
- Validation

## Tasks 2 & 3

`Task_2_&_3_Netflix_Data_Analysis.ipynb`

Contains the analytical implementation for:

- Content Type Analysis
- Country-Wise Analysis
- Calculations
- Visualizations
- Business Insights

The notebooks keep the analytical workflow **traceable and reproducible**.

---

# 📦 Project Deliverables

This repository contains:

- ✅ Raw Dataset
- ✅ Cleaned Dataset
- ✅ Data Cleaning Notebook
- ✅ Analysis Notebooks
- ✅ Task Requirement Screenshots
- ✅ Analytical Visualizations
- ✅ Streamlit Dashboard
- ✅ Project Presentation
- ✅ Task Requirements PDF
- ✅ Business Insights

---

# ▶️ How to Run the Dashboard

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Khushal-dak/netflix-data-analysis-dashboard.git
```

### 2️⃣ Open the Project

```bash
cd netflix-data-analysis-dashboard
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# 🎓 Skills Demonstrated

This project demonstrates practical understanding of:

- 🧹 Data Cleaning
- 🔍 Exploratory Data Analysis
- 📊 Data Visualization
- 📈 Trend Analysis
- 🌍 Country-Wise Analysis
- 📋 Data Aggregation
- 🛡️ Data Quality Management
- 💡 Business Insight Generation
- 🌐 Interactive Dashboard Development
- 🐙 Git & GitHub

---

# 👨‍💻 Author

## Khushal Dak

**B.Tech — Computer Science Engineering**  
Techno NJR Institute of Technology

🔗 **GitHub:**  
https://github.com/Khushal-dak

---

# ⭐ Final Takeaway

> **Clean Data → Reliable Analysis → Meaningful Insights → Better Decisions**

### 🚀 Netflix Data Analysis

**Raw Data → Cleaning → Analysis → Visualization → Insights → Interactive Dashboard**

---

⭐ If you find this project useful, consider giving the repository a star!

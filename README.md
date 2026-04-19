# 📊 Student Exam Performance Analysis
### Power BI Capstone Project

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 👤 Author Details

| Field | Details |
|-------|---------|
| **Name** | Arnab Kaushik Bora |
| **Roll Number** | 2306267 |
| **Batch / Program** | 2023-24 (BTech) |
| **Course** | Power BI |

---

## 📌 Project Overview

This project analyses **student exam performance** across 5 subjects, 5 departments, and 3 academic years (2022–2024). It uses a Python-generated and cleaned dataset of **600 student records** and presents findings through a 3-page **Power BI dashboard**.

### 🎯 Business Questions Answered
- Which department scores the highest on average?
- How does attendance affect grades?
- Does private tuition improve performance?
- What is the year-wise performance trend?
- Which subject needs the most improvement?

---

## 📁 Repository Structure

```
student-exam-performance-analysis/
│
├── student_raw.csv           ← Original dataset (606 rows with noise)
├── student_cleaned.csv       ← Cleaned dataset (600 rows, 0 nulls)
├── data_cleaning.py          ← Python cleaning script
├── StudentExamAnalysis.pbix  ← Power BI dashboard file
├── Project_Documentation.pdf ← Project report
└── README.md
```

---

## 🗂️ Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| Student_ID | Text | Unique ID per student |
| Gender | Text | Male / Female |
| Department | Text | Science / Commerce / Arts / Technology / Management |
| Attendance_Range | Text | Below 60% / 60-75% / 75-90% / Above 90% |
| Study_Hours_Daily | Number | Average daily study hours (1–8) |
| Math_Score | Number | Marks out of 100 |
| Science_Score | Number | Marks out of 100 |
| English_Score | Number | Marks out of 100 |
| Social_Score | Number | Marks out of 100 |
| Computer_Score | Number | Marks out of 100 |
| Total_Marks | Number | Sum of all 5 subjects (max 500) |
| Average_Score | Number | Total / 5 |
| Grade | Text | A (≥80) / B (≥65) / C (≥50) / D (<50) |
| Result | Text | Pass (avg ≥ 40) / Fail |
| Academic_Year | Number | 2022 / 2023 / 2024 |

---

## 🧹 Data Cleaning Steps (`data_cleaning.py`)

1. Load raw CSV
2. Remove 6 duplicate Student_IDs
3. Fill missing `Study_Hours_Daily` with **median**
4. Fill missing `Private_Tuition` with **mode**
5. Fill missing `Parental_Education` with **mode**
6. Strip whitespace from all text columns
7. Clip all scores to valid range [0, 100]
8. Recalculate `Total_Marks`, `Average_Score`, `Grade`, `Result`
9. Enforce correct data types
10. Export clean CSV (600 rows, 0 nulls)

```bash
pip install pandas numpy
python data_cleaning.py
```

---

## 📊 Power BI Dashboard Structure

### Page 1 — Executive Summary
- KPI Cards: Total Students, Avg Score, Pass Rate, Grade A Count
- Donut Chart: Grade distribution (A/B/C/D)
- Bar Chart: Avg Score by Department
- Slicers: Year, Department, Gender

### Page 2 — Detailed Analysis
- Bar Chart: Avg Score by Attendance Range
- Stacked Bar: Grade by Gender
- Scatter Plot: Study Hours vs Avg Score
- Table: Top students by score

### Page 3 — Insights
- Line Chart: Year-wise avg score trend (2022–2024)
- Bar: Private Tuition vs No Tuition comparison
- Donut: Pass vs Fail distribution
- Bar: Parental Education vs Avg Score

### Key DAX Measures

```dax
-- Pass Rate
Pass Rate =
DIVIDE(
    COUNTROWS(FILTER(student_cleaned, student_cleaned[Result] = "Pass")),
    COUNTROWS(student_cleaned)
) * 100

-- YoY Score Change
YoY Score Change =
VAR CY = CALCULATE(AVERAGE(student_cleaned[Average_Score]),
    FILTER(student_cleaned, student_cleaned[Academic_Year] = MAX(student_cleaned[Academic_Year])))
VAR PY = CALCULATE(AVERAGE(student_cleaned[Average_Score]),
    FILTER(student_cleaned, student_cleaned[Academic_Year] = MAX(student_cleaned[Academic_Year]) - 1))
RETURN DIVIDE(CY - PY, PY) * 100

-- Grade A Count
Grade A Count =
CALCULATE(COUNTROWS(student_cleaned), student_cleaned[Grade] = "A")
```

---

## ✅ ZIP Submission Checklist

- [ ] `student_raw.csv`
- [ ] `student_cleaned.csv`
- [ ] `data_cleaning.py`
- [ ] `StudentExamAnalysis.pbix`
- [ ] `Project_Documentation.pdf`

---

## ⚙️ How to Run

1. Run `python data_cleaning.py` to produce `student_cleaned.csv`
2. Open `StudentExamAnalysis.pbix` in Power BI Desktop
3. If Power BI asks for the file location, browse to student_cleaned.csv on your PC
4. Click **Refresh** — all visuals update automatically

---

*Submitted for Power BI Capstone | Arnab Kaushik Bora | 2306267 | 2023-24 (BTech)*

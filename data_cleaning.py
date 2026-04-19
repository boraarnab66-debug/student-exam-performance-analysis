"""
==============================================================
  Student Exam Performance Analysis - Data Cleaning Script
  Author      : Arnab Kaushik Bora
  Roll Number : 2306267
  Batch       : 2023-24 (BTech)
  Course      : Power BI
  Tool        : Python 3.x | Pandas | NumPy
==============================================================
"""

import pandas as pd
import numpy as np

INPUT_FILE  = "student_raw.csv"
OUTPUT_FILE = "student_cleaned.csv"

print("=" * 55)
print("  Student Exam Performance - Data Cleaning")
print("=" * 55)

# ── STEP 1: Load ──────────────────────────────────────────
df = pd.read_csv(INPUT_FILE)
print(f"\nSTEP 1 - Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ── STEP 2: Remove Duplicates ─────────────────────────────
before = len(df)
df.drop_duplicates(subset=['Student_ID'], keep='first', inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"STEP 2 - Duplicates removed: {before - len(df)} | Remaining: {len(df)}")

# ── STEP 3: Handle Missing Values ─────────────────────────
n1 = df['Study_Hours_Daily'].isna().sum()
df['Study_Hours_Daily'] = df['Study_Hours_Daily'].fillna(
    df['Study_Hours_Daily'].median()).round(1)
print(f"STEP 3 - Study_Hours_Daily: {n1} filled with median")

n2 = df['Private_Tuition'].isna().sum()
df['Private_Tuition'] = df['Private_Tuition'].fillna(
    df['Private_Tuition'].mode()[0])
print(f"       - Private_Tuition: {n2} filled with mode")

n3 = df['Parental_Education'].isna().sum()
df['Parental_Education'] = df['Parental_Education'].fillna(
    df['Parental_Education'].mode()[0])
print(f"       - Parental_Education: {n3} filled with mode")

# ── STEP 4: Strip Whitespace ──────────────────────────────
text_cols = ['Gender','Department','Study_Group','Attendance_Range',
             'Parental_Education','Internet_Access','Private_Tuition',
             'Grade','Result']
for col in text_cols:
    df[col] = df[col].str.strip()
print("STEP 4 - Whitespace stripped from all text columns")

# ── STEP 5: Clip Scores (0-100) ───────────────────────────
score_cols = ['Math_Score','Science_Score','English_Score',
              'Social_Score','Computer_Score']
for col in score_cols:
    df[col] = df[col].clip(0, 100)
print("STEP 5 - Scores clipped to valid range [0, 100]")

# ── STEP 6: Recalculate Derived Columns ──────────────────
df['Total_Marks']   = df[score_cols].sum(axis=1)
df['Average_Score'] = (df['Total_Marks'] / 5).round(2)

def assign_grade(avg):
    if avg >= 80:   return 'A'
    elif avg >= 65: return 'B'
    elif avg >= 50: return 'C'
    else:           return 'D'

df['Grade']  = df['Average_Score'].apply(assign_grade)
df['Result'] = df['Average_Score'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail')
print("STEP 6 - Total_Marks, Average_Score, Grade, Result recalculated")

# ── STEP 7: Fix Data Types ────────────────────────────────
df['Academic_Year']     = df['Academic_Year'].astype(int)
df['Study_Hours_Daily'] = df['Study_Hours_Daily'].astype(float)
print("STEP 7 - Data types enforced")

# ── STEP 8: Final Validation ──────────────────────────────
print("\n" + "=" * 55)
print("  FINAL VALIDATION")
print("=" * 55)
print(f"  Rows          : {len(df)}")
print(f"  Columns       : {len(df.columns)}")
print(f"  Total Nulls   : {df.isnull().sum().sum()}")
print(f"  Pass Rate     : {(df['Result']=='Pass').mean()*100:.1f}%")
print(f"  Avg Score     : {df['Average_Score'].mean():.2f}")
print(f"  Grade A Count : {(df['Grade']=='A').sum()}")

# ── STEP 9: Export ────────────────────────────────────────
df.to_csv(OUTPUT_FILE, index=False)
print(f"\n  Saved -> {OUTPUT_FILE}")
print("  DATA CLEANING COMPLETE")
print("=" * 55)

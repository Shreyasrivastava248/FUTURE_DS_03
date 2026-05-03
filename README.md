# 📊 Task 3 — Marketing Funnel & Conversion Performance Analysis

## 🗂️ Project Overview

This project is part of the **Future Interns Data Science Internship (FUTURE_DS_03)**. The goal is to analyze a **Bank Telemarketing Campaign** dataset, clean the raw data, and build an interactive **Power BI Dashboard** to uncover conversion insights.

---

## 📁 Project Structure
FUTURE_DS_03/
│
├── bank_detail.csv          # Raw dataset (original)
├── cleand_dataset.csv       # Cleaned dataset (after preprocessing)
├── task3.py                 # Data cleaning script
├── bussiness_ques.py        # Business questions analysis script
├── task3.pbix               # Power BI Dashboard file
└── README.md                # Project documentation
---

## 📌 Problem Statement

Analyze a bank's telemarketing campaign data to answer:
- Where are users **dropping off** in the funnel?
- Which **channels** bring high-quality leads?
- How can **conversion rates** be improved?

---

## 🧹 Data Cleaning Steps (`task3.py`)

| Step | Action |
|------|--------|
| 1 | Loaded raw `bank_detail.csv` |
| 2 | Stripped and lowercased column names |
| 3 | Replaced `unknown` values with `NaN` |
| 4 | Dropped null values |
| 5 | Checked and noted duplicates (not dropped — impact on results) |
| 6 | Uppercased all categorical columns |
| 7 | Removed rows with negative numeric values |
| 8 | Saved cleaned data as `cleand_dataset.csv` |

---

## 📊 Dashboard Features (Power BI)

### KPI Cards
- **643** — Total Customers
- **633** — Engaged Users
- **156** — Connected (Converted) Users

### Visuals Included
- Funnel Bar Chart — drop-off at each stage
- Conversion Rate by Channel (Cellular vs Telephone)
- Job-wise Conversion Matrix
- Interactive Slicers — Contact Type, Loan Status, Outcome

---

## 🔍 Key Insights

1. **24.3% conversion rate** — 643 contacted, only 156 converted
2. **Telephone (22%)** outperforms Cellular (20%) — focus on telephone
3. **Retired customers** have the highest conversion rate (0.34)
4. **Blue-collar** segment has the lowest ROI (0.10) — reduce budget
5. **477 "Other" outcome** users are an untapped re-targeting opportunity

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy) | Data Cleaning & Analysis |
| Matplotlib | Exploratory Visualization |
| Power BI | Interactive Dashboard |
| CSV | Data Storage |

---

## ▶️ How to Run

**Step 1 — Data Cleaning**
```bash
python task3.py
```

**Step 2 — Business Analysis**
```bash
python bussiness_ques.py
```

**Step 3 — Dashboard**
- Open `task3.pbix` in Power BI Desktop
- Refresh data source path if needed

---

## 👤 Author

Shreya srivastava  
Future Interns — Data Science Intern  


---

## 📃 License

This project is part of an internship program and is intended for educational purposes only.
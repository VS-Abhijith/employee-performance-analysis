# employee_analysis.py
# Email: 22ds3000188@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------
# Step 1: Create dataset (100 employees, realistic distribution)
# ----------------------
data = {
    "employee_id": [f"EMP{i:03d}" for i in range(1, 101)],
    "department": (
        ["Operations"] * 17 + 
        ["Sales"] * 20 + 
        ["Marketing"] * 15 + 
        ["Finance"] * 18 + 
        ["HR"] * 10 + 
        ["IT"] * 20
    ),
    "region": (["North America", "Europe", "Asia", "Africa", "Middle East"] * 20)[:100],
    "performance_score": [round(x, 2) for x in list(range(60, 160))[:100]],
    "years_experience": [i % 15 + 1 for i in range(100)],
    "satisfaction_rating": [round((i % 5) + 1 + (i % 3) * 0.1, 1) for i in range(100)]
}

df = pd.DataFrame(data)

# ----------------------
# Step 2: Frequency count for Operations dept
# ----------------------
operations_count = (df["department"] == "Operations").sum()
print("Frequency count for Operations department:", operations_count)

# ----------------------
# Step 3: Histogram of departments
# ----------------------
plt.figure(figsize=(6,4))
df["department"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save chart as image
plt.savefig("histogram.png")

# ----------------------
# Step 4: Save as HTML (embed count + image)
# ----------------------
html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h2>Employee Performance Analysis</h2>
<p><b>Email:</b> 22ds3000188@ds.study.iitm.ac.in</p>
<p><b>Frequency count for Operations department:</b> {operations_count}</p>
<img src="histogram.png" alt="Department Distribution Histogram" width="600">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

# employee_analysis.py
# Author: Abhijith
# Email: 22ds3000188@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------
# Step 1: Load dataset
# ----------------------
data = {
    "employee_id": ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005", "EMP006", "EMP007", "EMP008", "EMP009", "EMP010"],
    "department": ["Marketing", "Sales", "Operations", "Sales", "Finance", "Operations", "Operations", "Marketing", "HR", "Finance"],
    "region": ["Africa", "Europe", "Middle East", "North America", "North America", "Asia", "Europe", "Africa", "Asia", "Middle East"],
    "performance_score": [94.96, 66.27, 92.12, 80.09, 67.90, 72.15, 88.23, 59.77, 81.33, 69.44],
    "years_experience": [14, 15, 3, 3, 12, 8, 6, 4, 10, 7],
    "satisfaction_rating": [3.1, 3.7, 3.5, 4.6, 3.2, 4.0, 4.3, 2.9, 4.1, 3.8]
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
# Step 4: Save as HTML (with embedded image)
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

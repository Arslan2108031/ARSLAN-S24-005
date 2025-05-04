filename = "bomojobrandindices.csv" 
data = []
with open(filename, "r", encoding="utf-8") as file:
    header = file.readline().strip().split(",")
    for line in file:
        row = line.strip().split(",")
        while len(row) < len(header):
            row.append('')  
        data.append(row)
total_rows = len(data)
total_columns = len(header)
print("Total Rows:", total_rows)
print("Total Columns:", total_columns)
print("\nColumn Names:")
for col in header:
    print("-", col)
for row in data:
    for i in range(len(row)):
        if row[i].strip() == '':
            row[i] = '0'  
for row in data:
    for i in range(len(row)):
        try:
            row[i] = int(float(row[i]))
        except ValueError:
            pass
print("\nFirst 5 Rows After Pre-processing:")
for i in range(min(5, total_rows)):
    print(dict(zip(header, row if i >= len(data) else data[i])))
print("\nData Types Check:")
for i, col in enumerate(header):
    sample_value = data[0][i]
    print(f"{col}: {type(sample_value).__name__}")

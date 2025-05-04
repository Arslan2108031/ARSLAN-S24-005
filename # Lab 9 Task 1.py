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
print("\nFirst 5 Rows:")
for i in range(min(5, total_rows)):
    print(dict(zip(header, data[i])))
print("\nMissing Values per Column:")
missing = {}
for col_index, col_name in enumerate(header):
    count_missing = 0
    for row in data:
        if row[col_index].strip() == '':
            count_missing += 1
    missing[col_name] = count_missing

for col, count in missing.items():
    print(f"{col}: {count}")
if "brand" in header:
    brand_index = header.index("brand")
    brands = set()
    for row in data:
        brands.add(row[brand_index])

    print("\nUnique Brands:", len(brands))
    print("Some brands:", list(brands)[:5])
else:
    print("\nNo 'brand' column found in dataset.")


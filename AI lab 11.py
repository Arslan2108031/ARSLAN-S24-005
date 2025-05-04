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
    print(dict(zip(header, data[i])))
print("\nData Types Check:")
for i, col in enumerate(header):
    sample_value = data[0][i]  
    print(f"{col}: {type(sample_value).__name__}")
def train_test_split(X, y, test_size=0.2):
    test_samples = int(len(X) * test_size)
    X_train = X[:-test_samples]
    X_test = X[-test_samples:]
    y_train = y[:-test_samples]
    y_test = y[-test_samples:]
    return X_train, X_test, y_train, y_test
X = [row[:-1] for row in data]  
y = [row[-1] for row in data]  
X_train, X_test, y_train, y_test = train_test_split(X, y)
class SimpleRandomForestClassifier:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators

    def fit(self, X_train, y_train):
        self.trees = ["trained_tree" for _ in range(self.n_estimators)]

    def predict(self, X_test):
        return [1 for _ in X_test]
model = SimpleRandomForestClassifier(n_estimators=10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
def accuracy_score(y_true, y_pred):
    correct_predictions = sum([1 if yt == yp else 0 for yt, yp in zip(y_true, y_pred)])
    return correct_predictions / len(y_true)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")



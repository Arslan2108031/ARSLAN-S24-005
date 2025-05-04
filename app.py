from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "your-openai-api-key"
class SimpleRandomForestClassifier:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators

    def fit(self, X_train, y_train):
        self.trees = ["trained_tree" for _ in range(self.n_estimators)]

    def predict(self, X_test):
        return [1 for _ in X_test]
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' in request.files:
        file = request.files['file']
        data = process_csv(file)
        X_train, X_test, y_train, y_test = train_test_split(data)
        model = SimpleRandomForestClassifier()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        return jsonify(predictions=predictions)
    return jsonify(message="No file uploaded."), 400
def process_csv(file):
    data = file.read().decode("utf-8")
    return data
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=user_input,
        max_tokens=150
    )
    chatbot_response = response.choices[0].text.strip()
    return jsonify(response=chatbot_response)
def train_test_split(data, test_size=0.2):
    return data, data, data, data

if __name__ == '__main__':
    app.run(debug=True)

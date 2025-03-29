from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/naive_bayes_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return "Customer Query Classification API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        query = data.get('query')

        if not query:
            return jsonify({"error": "No query provided"}), 400

        query_tfidf = vectorizer.transform([query])

        prediction = model.predict(query_tfidf)[0]

        return jsonify({"query": query, "category": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

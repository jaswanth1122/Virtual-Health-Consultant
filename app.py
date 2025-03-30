from flask import Flask, request, jsonify
from health_ai import analyze_symptoms
from drug_checker import check_drug_interaction

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    symptoms = data.get("symptoms", "")

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    result = analyze_symptoms(symptoms)
    return jsonify({"result": result})

@app.route("/check_drug", methods=["POST"])
def check_drug():
    data = request.json
    medicine = data.get("medicine", "")

    if not medicine:
        return jsonify({"error": "No medicine provided"}), 400

    result = check_drug_interaction(medicine)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

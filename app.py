from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os
import csv

# =================================
# INIT APP
# =================================

app = Flask(__name__, template_folder="templates")
CORS(app)

# =================================
# LOAD MODEL
# =================================

models = {}
accuracies = {}
selected_features = []

try:
    models = {
        "Naive Bayes": joblib.load("naive_bayes_model.pkl"),
        "Decision Tree": joblib.load("decision_tree_model.pkl"),
        "Random Forest": joblib.load("random_forest_model.pkl"),
    }

    accuracies = joblib.load("model_accuracies.pkl")
    selected_features = joblib.load("selected_features.pkl")

    print("Model berhasil dimuat")

except Exception as e:
    print("Error loading model:", e)


# =================================
# ROUTE ASSETS (LOGO / IMAGE)
# =================================

@app.route("/assets/<path:filename>")
def assets(filename):
    return send_from_directory("assets", filename)


# =================================
# ROUTE HALAMAN
# =================================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prediksi")
def prediksi():
    return render_template("prediksi.html")


# =================================
# DATASET
# =================================

@app.route("/dataset")
def dataset():

    file = os.path.join("data", "fetal_health.csv")

    raw_rows = []
    header = []

    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            for row in reader:
                raw_rows.append(row)

    except Exception as e:
        return f"Error membaca dataset: {e}"

    columns_to_remove = [
        "mean_value_of_long_term_variability",
        "histogram_width",
        "histogram_min",
        "histogram_max",
        "histogram_number_of_peaks",
        "histogram_number_of_zeroes",
        "fetal_movement",
        "uterine_contractions",
        "light_decelerations",
        "severe_decelerations",
        "histogram_tendency"
    ]

    # =============================
    # HAPUS DUPLIKAT
    # =============================

    unique_rows = []
    seen = set()

    for row in raw_rows:
        key = tuple(row)

        if key not in seen:
            seen.add(key)
            unique_rows.append(row)

    # =============================
    # CARI INDEX KOLOM DIHAPUS
    # =============================

    remove_indexes = []

    for i, col in enumerate(header):
        if col.strip() in columns_to_remove:
            remove_indexes.append(i)

    # =============================
    # HEADER BARU
    # =============================

    processed_header = [
        col for i, col in enumerate(header)
        if i not in remove_indexes
    ]

    # =============================
    # DATASET BARU
    # =============================

    processed_rows = []

    for row in unique_rows:
        new_row = [
            val for i, val in enumerate(row)
            if i not in remove_indexes
        ]
        processed_rows.append(new_row)

    return render_template(
        "dataset.html",
        header=header,
        raw_rows=raw_rows,
        processed_header=processed_header,
        processed_rows=processed_rows,
        raw_count=len(raw_rows),
        raw_col_count=len(header),
        processed_count=len(processed_rows),
        processed_col_count=len(processed_header),
        duplicate_count=len(raw_rows) - len(unique_rows)
    )


# =================================
# API FEATURES
# =================================

@app.route("/features", methods=["GET"])
def get_features():
    return jsonify({
        "selected_features": selected_features
    })


# =================================
# API PREDICT
# =================================

@app.route("/predict", methods=["POST"])
def predict():

    print("DEBUG /predict - selected_features loaded:", selected_features)

    try:

        data = request.get_json()

        print("DEBUG /predict - Received data keys:", list(data.keys()) if data else "NO DATA")
        print("DEBUG /predict - Expected features:", selected_features)

        if not data:
            return jsonify({"error": "No input data"}), 400

        missing = [f for f in selected_features if f not in data]
        print("DEBUG /predict - Missing features:", missing)

        if missing:
            return jsonify({
                "error": "Missing features",
                "missing_features": missing
            }), 400

        # Validate all numeric
        input_features = []
        for f in selected_features:
            val = data[f]
            if val is None or not isinstance(val, (int, float)) or np.isnan(val):
                return jsonify({"error": f"Invalid value for {f}: {val}"}), 400
            input_features.append(float(val))

        input_array = np.array(input_features).reshape(1, -1)

        label_map = {
            1: "Normal",
            2: "Suspect",
            3: "Pathological"
        }

        results = []

        for name, model in models.items():

            pred = int(model.predict(input_array)[0])
            label = label_map.get(pred, "Unknown")

            # Fix accuracy lookup (match original)
            acc_key = name.lower().replace(" ", "_")
            acc = round(accuracies.get(acc_key, 0) * 100, 2)

            results.append({
                "model": name,
                "prediction": pred,
                "label": label,
                "accuracy": acc
            })

        print("DEBUG /predict - Success, predictions:", [r["label"] for r in results])
        return jsonify({"results": results})

    except Exception as e:
        print("DEBUG /predict - Exception:", str(e))
        return jsonify({"error": str(e)}), 500


# =================================
# RUN APP
# =================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )

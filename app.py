from flask import Flask, request, jsonify
from flask_cors import CORS
from pyspark import SparkContext, SparkConf
import os

# Initialize Flask
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Spark context
conf = SparkConf().setAppName("WordCountApp").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf=conf)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        # Check if a file is part of the request
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Spark Word Count
        text_rdd = sc.textFile(file_path)
        word_counts = (
            text_rdd.flatMap(lambda line: line.split())
                    .map(lambda word: (word.lower(), 1))
                    .reduceByKey(lambda a, b: a + b)
                    .collect()
        )

        return jsonify({"wordcount": dict(word_counts)})

    except Exception as e:
        print("Error:", e)  # Print error to terminal
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

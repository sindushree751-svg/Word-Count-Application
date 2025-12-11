from pyspark.sql import SparkSession

def run_wordcount(filepath):
    spark = SparkSession.builder \
        .appName("WordCountApp") \
        .master("local[*]") \
        .getOrCreate()

    sc = spark.sparkContext

    # Read the text file
    text_file = sc.textFile(filepath)

    # Word count logic
    counts = (text_file.flatMap(lambda line: line.split())
                         .map(lambda word: (word.lower(), 1))
                         .reduceByKey(lambda a, b: a + b)
                         .collect())

    spark.stop()

    # Convert result to dictionary
    result_dict = {word: count for word, count in counts}
    return result_dict

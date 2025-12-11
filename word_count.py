from pyspark import SparkConf, SparkContext
import re

def normalize(word):
    return re.sub(r'[^a-z0-9]', '', word.lower())

def main():
    conf = SparkConf().setAppName("WordCountApp").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # Load file
    text_rdd = sc.textFile("app/data.txt")

    # Process words
    words = (
        text_rdd
        .flatMap(lambda line: line.split())
        .map(lambda w: normalize(w))
        .filter(lambda w: w != "")
    )

    # Count
    word_count = words.map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)

    # Sort
    sorted_words = word_count.sortBy(lambda x: x[1], ascending=False)

    # Show output
    for word, count in sorted_words.take(20):
        print(f"{word} : {count}")

    sc.stop()

if __name__ == "__main__":
    main()

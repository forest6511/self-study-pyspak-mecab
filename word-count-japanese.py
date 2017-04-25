import MeCab
from pyspark import SparkConf, SparkContext


def analyze_japanese_array(text):
    words = []
    m = MeCab.Tagger('mecabrc')
    word_map_lines = m.parse(text).split('\n')
    for word_map_line in word_map_lines:
        if not(word_map_line == 'EOS' or word_map_line == ''):
            word, info = word_map_line.split('\t')[0], word_map_line.split('\t')[1].split(',')
            # part of speech
            if info[0] == '名詞':
                words.append(word)
    return words


if __name__ == '__main__':
    conf = SparkConf().setMaster("local").setAppName("WordCount")
    sc = SparkContext(conf = conf)

    input = sc.textFile("./Japanese-book.txt")
    words = input.flatMap(analyze_japanese_array)

    word_counts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    word_counts_sorted = word_counts.map(lambda x: (x[1], x[0])).sortByKey()
    results = word_counts_sorted.collect()

    for result in results:
        count = str(result[0])
        print(result[1] + ":\t" + count)

# pysparkとMecabでワードカウント

## Environment
Mac OS X  
Python 3.5.0

## Install pyspark
```
$ brew install apache-spark
```

### Confirm to install pyspark
```
$ pyspark
Python 3.5.0 (default, Jun 19 2016, 19:10:17)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
17/04/12 13:07:12 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/04/12 13:07:26 WARN ObjectStore: Failed to get database global_temp, returning NoSuchObjectException
Welcome to
 ____              __
/ __/__  ___ _____/ /__
_\ \/ _ \/ _ `/ __/  '_/
/__ / .__/\_,_/_/ /_/\_\   version 2.1.0
 /_/

Using Python version 3.5.0 (default, Jun 19 2016 19:10:17)
SparkSession available as 'spark'.
```
___

## Install Mecab in Mac

```
$ brew install mecab
$ brew install mecab-ipadic
$ pip install mecab-python3
$ python3
Python 3.5.0 (default, Jun 19 2016, 19:10:17) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import MeCab
>>> m = MeCab.Tagger("-Ochasen")
>>> print(m.parse("はてブは辞書登録されているのかな？"))
はて    ハテ    はて    副詞-一般               
ブ      ブ      ブ      名詞-一般               
は      ハ      は      助詞-係助詞             
辞書    ジショ  辞書    名詞-一般               
登録    トウロク        登録    名詞-サ変接続           
さ      サ      する    動詞-自立       サ変・スル      未然レル接続
れ      レ      れる    動詞-接尾       一段    連用形
て      テ      て      助詞-接続助詞           
いる    イル    いる    動詞-非自立     一段    基本形
の      ノ      の      名詞-非自立-一般                
か      カ      か      助詞-副助詞／並立助詞／終助詞           
な      ナ      な      助詞-終助詞             
？      ？      ？      記号-一般               
EOS

```

## Get Japanese sample text below
http://lipsum.sugutsukaeru.jp/index.cgi

## issue command
```
$ spark-submit word-count-japanese.py
```

## result of sample
```
世の中: 4
君:     4
はず:   4
不愉快: 4
必要:   4
忠告:   4
活動:   4
日:     4
```

# etc
* conf directory  
/usr/local/Cellar/apache-spark/2.1.0/libexec/conf
![](https://dpegb9ebondhq.cloudfront.net/product_photos/56926928/0018_original.jpg)
Art by:[Altered  Artichoke](https://alteredartichoke.storenvy.com/products/21890729-spooky-spider-dictionary-art-print-no-18)


# Dictionary Crawler ![](https://img.shields.io/apm/l/vim-mode.svg) 
This is a python code based on Scrapy package to crawl famous online dictionaries like Oxford, Longman, Cambridge, Webster, and Collins.
Be aware that this code is published on July 21, 2019, and if those sites will be updated in the future this code may not work properly.
## Prerequisites
Scrapy python package

## How to use it?
##### 1- set words:
at *dictionary_crawler/dictionary_crawler/dictionary_crawler/spiders* there is a **\__init__.py** and there is a list named **words** that is initialize like this:
```python
words = ['I', 'hope', 'you', 'like', 'this', 'dictionary', 'web', 'crawler']
```
you can change this list to crawl the words that you want.
##### 2- run:
go to the file *dictionary_crawler/dictionary_crawler/dictionary_crawler/spiders* and run this in the terminal

    scrapy crawl [name of dictionary] -o [name of file to write into].jl
    
for example for Oxford dictionary:

    scrapy crawl oxford -o oxford.jl
and the data will be stored in oxford.jl at *dictionary_crawler/dictionary_crawler/dictionary_crawler/spiders*

## How is the output?
The output is a JSON Lines file format that each line of it is a python dictionary with a word and definitions of it.
for example, the word **hope** in the Webster dictionary is like this:
```json
{"hope":
    {
    "verb": ["to cherish a desire with anticipation  to want something to happen or be true"],
    "noun": ["to desire with expectation of obtainment or fulfillment", "to expect with confidence", "city in southwestern Arkansas that was the childhood home of President Bill Clinton population 10,095"],
    "biographical name": ["desire accompanied by expectation of or belief in fulfillment", "expectation of fulfillment or success", "someone or something on which hopes are centered", "something desired or hoped (see  1) for", "Anthony", "Bob 1903–2003 originally Leslie Townes Hope American (British-born) comedian"],
    "geographical name": ["Victor Alexander John 1887–1951 2nd Marquis of", "British soldier; viceroy of India (1936–43)"]
    }
}
```
## Author

* **Peyman Mohseni kiasari**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

from bs4 import BeautifulSoup
import requests
import re
from collections import Counter

def scrape(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    body = soup.find('body')
    texts = body.text
    words = re.sub("[^\w' ]", " ", texts).split()
    return words

def frequency(word,array):
    count = 0
    for i in range(0, len(array)):
        if(word.lower() == array[i].lower()):
            count += 1
    return count

def throw_numbers(array):
    arr = array
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    lists = []
    length = len(arr)
    for i in range(0, len(arr)):
        word = arr[i]
        for j in range(0, len(numbers)):
            numb = numbers[j]
            if numb in word:
                lists.append(word)
                break
    for i in range(0,len(lists)):
        numb = lists[i]
        arr.remove(numb)
    return arr

def make_unique(array):
    unique = []
    for i in range(0, len(array)):
        is_unique = True
        for j in range(0, len(unique)):
            if array[i].lower() == unique[j].lower():
                is_unique = False
        if is_unique == True and (len(array[i])>1):
            unique.append(array[i])
    return unique

def bubble_sort(unq,full):
    n = len(unq)
    for i in range(n):

        for j in range(0, n-i-1):
  
            if frequency(unq[j],full) > frequency(unq[j+1],full) :
                unq[j], unq[j+1] = unq[j+1], unq[j]
    unq.reverse()
    return unq[:5]

def compare_url(first,second):
    count = 0
    for i in range(0, len(first)):
        for j in range(0, len(second)):
            if first[i].lower() == second[j].lower():
                count += 1
    return count*100/5

def find_link(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    links = []
    sub = "http"
    for a in soup.find_all('a', href=True):
        link = a['href']
        if sub in link:
            links.append(link)
    links = make_unique(links)
    return links

def find_words_in_links(array):
    all_words = []
    length = len(array)
    if length > 4:
        length = 4
    for i in range(0,length):
        ar = scrape(array[i])
        #ar = make_unique(ar)
        ar = throw_numbers(ar)
        all_words.append(ar)
    return all_words

def list_of_frequencies(unq,array):
    frequencies = []
    for i in range(0, len(unq)):
        freq = frequency(unq[i],array)
        frequencies.append(freq)
    return frequencies

def third_degree_links(array):
    third_degree_link = []
    for i in range(0, len(array)):
        link = find_link(array[i])
        third_degree_link.append(link)
    return third_degree_link

def second_degree_keywords(array):
    arr = array[:2]
    keys = []
    for i in range(0, len(arr)):
        unq = make_unique(arr[i])
        key = bubble_sort(unq,arr[i])
        keys.append(key)
    return keys
import requests
import random

# GOOGLE BOOKS

# GET https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=yourAPIKey
# query = "https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699"


def getProperties(topic, key):
    query = f"https://www.googleapis.com/books/v1/volumes?q={topic}&key={key}"
    properties = {'topic': topic.upper()}
    response = requests.get(query).json()
    properties['totalnum']=len(response['items'])
    rand = random.randint(0, properties['totalnum']-1)
    properties['randnum']=rand
    # print(response['items'][rand])
    properties['title'] = response['items'][rand]['volumeInfo']['title']
    if 'description' in response['items'][rand]['volumeInfo'].keys():
        properties['summary'] = response['items'][rand]['volumeInfo']['description']
    else:
        properties['summary'] ="No description provided." 
    properties['source']= response['items'][rand]['volumeInfo']['imageLinks']['thumbnail']
    properties['allcovers']=[]
    for book in response['items']:
        properties['allcovers'].append(book['volumeInfo']['imageLinks']['thumbnail'])
    return properties
    


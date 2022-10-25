from googlesearch import search
query = input('Enter Your Query: ')
 
for url in search(query):
    print(url)
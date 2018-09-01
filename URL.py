import urllib.request



def htmlToFile(url):
    f = open('index.html','w')
    page = urllib.request.urlopen(url)
    f.write( page.read().decode("utf-8")  )
    f.close()
    
def start():
    urlInput = input('Enter a url and I will write the html down \n')
        
    htmlToFile(urlInput)
        

start()


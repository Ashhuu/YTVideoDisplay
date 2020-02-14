from django.shortcuts import render
from django.http import HttpResponse
from . import api

# Create your views here.


def home(request):
    data = api.fetch()
    collection = []
    for i in range(1, 4):
        snippetdetails = data[i]
        dictionary = {}
        fetchid = snippetdetails['id']
        id = fetchid['videoId']
        vidurl = "https://www.youtube.com/watch?v=" + id
        embedurl = "https://www.youtube.com/embed/" + id
        details = snippetdetails['snippet']
        ft = details['thumbnails']
        fil = ft['medium']
        for j in details:
            if j == 'title' or j =='publishedAt' or j == 'description':
                dictionary.update({j: details[j]})
        dictionary.update({'thumbnail': fil['url']})
        dictionary.update({'url': vidurl})
        dictionary.update({'embedurl': embedurl})
        collection.append(dictionary)
    print(collection)
    return render(request, 'channel/embedhome.html', {'data': collection})

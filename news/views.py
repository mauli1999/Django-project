from django.shortcuts import render
from newsapi import NewsApiClient
import requests
# from django.conf import settings
from mysite.settings import API_KEY
from django.http import HttpResponse, JsonResponse
#from hermes.models import Profile
from hermes.models import Profile

# Create your views here.
temp_img = "https://images.pexels.com/photos/3225524/pexels-photo-3225524.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
#  https://www.w3schools.com/code/tryit.asp?filename=GJ8R42LMFRLP

def home(request):
    page = request.GET.get('page', 1)
    current_user = request.user
    active_id = current_user.id
    preferences = Profile.objects.values_list('news_category').filter(user_id = active_id)
    preferences2 = Profile.objects.values_list('news_category_two').filter(user_id = active_id)
    country = Profile.objects.values_list('country').filter(user_id = active_id)
    category =  preferences[0][0]
    category_two =  preferences2[0][0]
    print(category_two)
    location = country[0][0]
    print(location)
    search = request.GET.get('search', category)
    search_two = request.GET.get('search_two', category_two)

    # code to run query from search bar
    if request.method == "POST":
        search = request.POST.get('query')
        

    if search is None or search=="top": 
        # get the top news by country
        url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
            location,1,API_KEY
        )
    else:
        # get the search query request
        url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
            search,"popularity",page,API_KEY
        )
    r = requests.get(url=url)
    
    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    data = data["articles"]
    context = {
        "success": True,
        "data": [],
        "search": search
    }
    # seprating the necessary data
    for i in data:
        context["data"].append({
            "title": i["title"],
            "description":  "" if i["description"] is None else i["description"],
            "url": i["url"],
            "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
            "publishedat": i["publishedAt"]
        })
    # send the news feed to template in context
    return render(request, 'index.html', context=context)


def loadcontent(request):
    try:
        page = request.GET.get('page', 1)
        current_user = request.user
        active_id = current_user.id
        preferences = Profile.objects.values_list('news_category').filter(user_id = active_id)
        preferences2 = Profile.objects.values_list('news_category_two').filter(user_id = active_id)
        country = Profile.objects.values_list('country').filter(user_id = active_id)
        category =  preferences[0][0]
        category_two =  preferences2[0][0]
        print(category_two)
        location = country[0][0]

        search = request.GET.get('search', category)
        # url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
        #     "Technology","popularity",page,settings.APIKEY
        # )
        if search is None or search=="top":
            url = "https://newsapi.org/v2/top-headlines?country={}&page={}&apiKey={}".format(
                "us",page,API_KEY
            )
        else:
            url = "https://newsapi.org/v2/everything?q={}&sortBy={}&page={}&apiKey={}".format(
                search,"popularity",page,API_KEY
            )
        print("url:",url)
        r = requests.get(url=url)
        
        data = r.json()
        if data["status"] != "ok":
            return JsonResponse({"success":False})
        data = data["articles"]
        context = {
            "success": True,
            "data": [],
            "search": search
        }
        for i in data:
            context["data"].append({
                "title": i["title"],
                "description":  "" if i["description"] is None else i["description"],
                "url": i["url"],
                "image": temp_img if i["urlToImage"] is None else i["urlToImage"],
                "publishedat": i["publishedAt"]
            })

        return JsonResponse(context)
    except Exception as e:
        return JsonResponse({"success":False})


# def home(request):
#     newsapi = NewsApiClient(api_key='46867c19a05b4be6be4800e3ba1871f6')
#     topnews = newsapi.get_top_headlines('cnn')   # source=ndtv, bbc-news, cnn,techcrunch,foxnews.

#     latest = topnews['articles']
#     print(topnews)
#     title = []
#     desc = []
#     url = []
#     author = []
#     date = []

#     for i in range(len(latest)):
#         news = latest[i]

#         title.append(news['title'])
#         desc.append(news['description'])
#         url.append(news['url'])
#         author.append(news['author'])
#         date.append(news['publishedAt'])

#     all_news = zip(title, desc, url, author, date)

#     context = {
#         'all_news': all_news
#     }

#     return render(request, "index.html", context)

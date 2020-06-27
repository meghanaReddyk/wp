from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'homepage.html')
def count(request):
    fulltext=request.GET['fulltext']
    print(fulltext)
    l=fulltext.split()
    word_dict={}
    for word in l:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    return  render(request,'count.html',{'text':fulltext,'count':len(l),'dict':word_dict.items()})
def about(request):
    return  render(request,'about.html')


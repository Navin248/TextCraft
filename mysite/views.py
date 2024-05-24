from django.http import HttpResponse
from django.shortcuts import render

#This code is for demonstrate Navigation bar
# def index(request) :
#     return HttpResponse('''<h1>Navigation Bar</h1> <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-6/"> Django Code With Harry</a> <br> <a href="https://www.facebook.com">Facebook</a> <br> <a href="https://www.google.com">Google</a> <br> <a href="https://www.flipkart.com">Flipkart</a> <br> <a href="https://www.news.com">News</a> ''')
# def about(request):
#     return HttpResponse("About Harry Bhai")
def index(request):
    return render(request,'index3.html')
    #this code is for pipeline
    # return HttpResponse('''HOME
    #                     <html> <body> 
    #                     <a href="http://127.0.0.1:8000/removepunc"><span style="margin-left:20px"> <button>Remove Punc</button></span> </a> 
    #                     <a href="http://127.0.0.1:8000/capatilizefirst"><span style="margin-left:20px"> <button>capatilizefirst</button></span> </a>
    #                     <a href="http://127.0.0.1:8000/newlineremove"><span style="margin-left:20px"> <button>NewLine</button></span> </a>
    #                     <a href="http://127.0.0.1:8000/spaceremove"><span style="margin-left:20px"> <button>spaceremove</button></span> </a>
    #                     <a href="http://127.0.0.1:8000/charcount"><span style="margin-left:20px"> <button>charcount</button></span> </a>
    #                     </body> </html>''')
def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    capatilize=request.GET.get('capatilize','off')
    NewLineRemove=request.GET.get('NewLineRemove','off')
    spaceremove=request.GET.get('spaceremove','off')
    charcount=request.GET.get('charcount','off')

    #check which checkbox is on
    if removepunc=='on':
        punctations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in punctations:
                analyzed=analyzed + char
        params={'purpose':'Removed puncations','analyzed_text':analyzed}
        print(analyzed)
        return render(request,'analyze.html',params)
    
    elif(capatilize=="on"):
        capatilized=''
        for char in djtext:
            capatilized=capatilized+char.upper()
        params={'purpose':'Capatilized text','analyzed_text':capatilized}
        return render(request,'analyze.html',params)
    
    elif(NewLineRemove=="on"):
        NewLineRemoved=''
        for char in djtext:
            if char != '\n':
                NewLineRemoved=NewLineRemoved+char.upper()
        params={'purpose':'NewLineRemoved','analyzed_text':NewLineRemoved}
        return render(request,'analyze.html',params)
    
    elif(spaceremove=="on"):
        spaceremoved=''
        for char in djtext:
            if char != ' ':
                spaceremoved=spaceremoved+char
        params={'purpose':'Spaceremoved','analyzed_text':spaceremoved}
        return render(request,'analyze.html',params)

    elif(charcount=="on"):
        charcounter=0
        for char in djtext:
                if char != ' ' and char != '\n':
                 charcounter=charcounter+1
        params={'purpose':'Spaceremoved','analyzed_text':charcounter,'original_text': djtext}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error 404")
    


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
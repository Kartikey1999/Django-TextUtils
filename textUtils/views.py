
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    text = request.POST.get('text', 'default')

    # Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        text = analyzed
        # return render(request, "analyze.html", params)

    if fullcaps == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to Upper Case',
                  'analyzed_text': analyzed}
        text = analyzed
        # return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char!="\r":
                analyzed = analyzed+char
        params = {'purpose': 'Removed new lines',
                  'analyzed_text': analyzed}

        text = analyzed
        # return render(request, "analyze.html", params)

    if charcounter == "on":
        analyzed = 0
        for char in text:
            analyzed = analyzed+1
        params = {'purpose': 'Total  Char Count',
                  'analyzed_text': analyzed}
        text = analyzed

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and charcounter!="on" ):
        return HttpResponse("please select seitch")
        # return render(request, "analyze.html", params)

    return render(request, "analyze.html", params)

    # else:
    #     return HttpResponse("ERROR")

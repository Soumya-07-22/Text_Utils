from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return render(request, 'Analyze2.html')

def analyze(request):
    djText = request.POST.get('text', 'default')
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    print(removepunc)
    print(djText)
    analyze = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on" and fullcaps == "off":
        for char in djText:
            if char not in punctuations:
                analyze = analyze + char
        params = {'Purpose': 'Remove Punctuations', 'analyzed_text': analyze}
        return render(request, 'Analyze.html', params)

    elif(fullcaps == "on" and removepunc == "off"):
        for char in djText:
            analyze = analyze + char.upper()
        params = {'Purpose': 'Full Capitalize', 'analyzed_text': analyze}
        return render(request, 'Analyze.html', params)

    elif(fullcaps == "on" and removepunc == "on"):
        for char in djText:
            if char not in punctuations:
                analyze = analyze + char
        analyze = analyze.upper()
        params = {'Purpose': 'Remove Punctuations & capitalize', 'analyzed_text': analyze}
        return render(request,'Analyze.html', params)
    elif(newlineremove == "on"):
        for char in djText:
            if char != "\n":
                analyze = analyze + char
        params = {'Purpose':'New Line Remover', 'analyzed_text': analyze}
        return render(request, 'Analyze.html', params)
    else:
        return HttpResponse("Error!!!")

from django.shortcuts import render


def mainpage(request):
    context = {}
    return render(request, "fastai_image/mainpage.html", context)
from django.shortcuts import render
from fastai_image.models import Classification


def mainpage(request):
    list_obj = Classification.objects.all()
    context = {
        "list_obj": list_obj
    }
    return render(request, "fastai_image/mainpage.html", context)


def detailpage(request, pk):
    obj = Classification.objects.get(pk=pk)
    context = {
        "obj": obj
    }
    return render(request, "fastai_image/detailpage.html", context)

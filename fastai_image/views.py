from django.core.files.storage import default_storage, FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from fastai_image.models import Classification

from fastai.vision.all import load_learner


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


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image uploaded'}, status=400)
        
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        image_path = fs.path(filename)

        id = request.POST['id']

        try:
            obj = Classification.objects.get(pk=id)
            learn_inf = load_learner(obj.file)

            # Predict the result
            result = learn_inf.predict(image_path)
            label = result[0]
            confidence = max(result[2]).item()
            confidence_percentage = round(confidence * 100)

            formatted_result = f"{label} ({confidence_percentage}%)"

            # Clean up the temporary file
            fs.delete(filename)

            return JsonResponse({'formatted_result': formatted_result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

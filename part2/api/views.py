import os
from pathlib import Path
from django.http import JsonResponse, Http404, HttpResponse
from part2.serializers import ImageSerializer
from part2.models import Image

def images(request):
    if request.method == 'GET':
        images = Image.objects.all().order_by('id')
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return Http404()

def image_meta(request, pk):
    if request.method == 'GET':
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        return Http404()

def download_image(request, pk):
    if request.method == 'GET':
        file_path = os.path.join(Path(__file__).resolve().parent.parent, 'data/')
        image_path = file_path + str(pk) + '.jpg'
        try:
            with open(image_path, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
    else:
        return Http404()
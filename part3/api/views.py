from django.http import JsonResponse
from part3.api.api import *

def components(request):
    components = get_components()
    return JsonResponse(components, safe=False)
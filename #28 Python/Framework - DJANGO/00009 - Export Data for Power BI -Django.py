from django.http import JsonResponse
from .models import YourModelName

def data_for_power_bi(request):
    data = list(YourModelName.objects.values())  # Convert queryset to list of dicts
    return JsonResponse(data, safe=False)

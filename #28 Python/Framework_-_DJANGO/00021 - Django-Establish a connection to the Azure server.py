from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import YourModelName
from .forms import YourModelForm

@csrf_exempt
def dashboard(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = YourModelForm()
        return render(request, 'dashboard.html', {'form': form})

def data_for_dashboard(request):
    data = list(YourModelName.objects.values())  # Convert queryset to list of dicts
    return JsonResponse(data, safe=False)

from django.shortcuts import render

# Create your views here.
def data_output(request):
    return render(request, 'index.html')
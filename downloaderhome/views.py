from django.shortcuts import render


def home(request):
    return render(request=request, template_name='home.html')

def download(request):
    render(request=request, template_name='home.html', context={
        'object1': 'eae'
    })
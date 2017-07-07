from django.shortcuts import render

# Create your views here.


def analysis(request):
    template_name = 'analysis/analysis_index.html'
    response = render(request, template_name)
    return response

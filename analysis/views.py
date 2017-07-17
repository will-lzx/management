from django.shortcuts import render

# Create your views here.


def analysis(request):
    template_name = 'analysis/analysis_index.html'
    context = {
        'menu_selected': 'data_analysis'
    }
    response = render(request, template_name, context)
    return response

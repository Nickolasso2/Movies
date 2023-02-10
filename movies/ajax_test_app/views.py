from django.shortcuts import render
from django.views.generic.base import View
from time import time
from django.http import JsonResponse
from .forms import ContactForm


class AjaxHandlerView(View):
    def get(self, request):
        from_ajax = request.GET.get('button_text')
                
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            t = time()
            
            return JsonResponse({'seconds':t}, status=200)
        return render(request, 'ajax_test_app/index.html', {'form': ContactForm()})

    def post(self, request):
        card_text = request.POST.get('text')
        result = 'I\'ve got' + card_text
        return JsonResponse({'data':result}, status=200)

def contact(request):
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            return JsonResponse({
                'message' : 'success'
            })
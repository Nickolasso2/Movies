from django.shortcuts import render, redirect
from contact_app.forms import ContactForm
from django.views.generic import CreateView, View
from .models import Contact
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


class ContactView(CreateView):

    form_class = ContactForm
    success_url = '/'
    template_name = 'contact_app/clone_current_page.html'

    # def form_invalid(self, form):
    #     # for message in messages.error:
    #     #     print('_____----_--', messages.error)
    #     return redirect (self.request.META.get('HTTP_REFERER'))
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contentBlock'] = self.request.POST.get('contentBlock')
        return context

def contact_def(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        print(request.META.get('HTTP_REFERER'))
        if form.is_valid():
            form.save()            
            return JsonResponse({'result':'Ви підписані.Дякуємо.', 'is_valid':'true'}, status=200)
    
        else:
            return JsonResponse({'result':'Помилка валідації'}, status=200)

def contact_def3(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        print(request.META.get('HTTP_REFERER'))
        if form.is_valid():
            form.save()            
            return redirect('/')
        else:
            return redirect(request.META.get('HTTP_REFERER'))


class Contact2View(CreateView):

    form_class = ContactForm
    success_url = '/'
    # template_name = 'contact_app/clone_current_page.html'

    def form_invalid(self, form):
        # for message in messages.error:
        #     print('_____----_--', messages.error)
        return redirect (self.request.META.get('HTTP_REFERER'))
    


# just testing redirect method

# def redirect1(request):
#     form = ContactForm(request.POST)
#     return render(request, 'contact_app/redirect1.html', {'form':form})

# def redirect2(request):
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         return redirect('/')
#     else:
#         return render(request, 'contact_app/redirect2.html', {'form':form})
    
  

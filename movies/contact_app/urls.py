# path('contact/', include('contact_app.urls'))
from django.urls import path
from .views import ContactView, contact_def, contact_def3, Contact2View

urlpatterns = [
    path('', ContactView.as_view(), name='add_contact'),
    path('def/', contact_def, name='add_contact2'),
    path('def_red/', contact_def3, name='add_contact3'),
    path('add', Contact2View.as_view(), name='add_contact4'),

    # path('redirect1/', redirect1, name='redirect1'),
    # path('redirect2/', redirect2, name='redirect2'),
  

]
from django.urls import path
from app.hustle_api.views import *
from app.views import create_checkout_session, PaymentSuccessView, paymentfailed
from django.views.generic import RedirectView

urlpatterns = [
    
    path('', EventAPIView.as_view(), name="event-list"),
    path('gallery-list/', GalleryListView.as_view(), name="gallery-list"),
    path('create-contact/', Contact_create.as_view(), name="create-contact"),
    path('counter-items/<int:pk>', CounterItemAPI.as_view(), name="counter-items"),
    path('home-counter/', HomeCounterAPI.as_view(), name="home-counter"),
    path('<slug:slug>', EventDetailAPI.as_view(), name="event-detail"),
    # payment urls
    path("payment/<int:id>", create_checkout_session, name='api_checkout_session'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', paymentfailed , name='failed'),
    
    path('redirect/', RedirectView.as_view(url='http://52.194.244.220/success')),
]
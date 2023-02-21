from django.shortcuts import redirect, get_object_or_404
import stripe
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.generic import TemplateView, View
from django.urls import reverse
import datetime
from django.conf import settings
from django.template.loader import render_to_string
from app.models import PAYMENT, EventRegisterForm, Event
from app.hustle_api.serializers import EventRegisterSerializer, PaymentSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def create_checkout_session(request, id):
    
    event_instance = Event.objects.filter(id=id).last()
    
    try:
        serializer = EventRegisterSerializer(data=request.data)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if serializer.is_valid():
        print(serializer.data, request.POST)
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        contact = serializer.validated_data['contact']
        persons = serializer.validated_data['number_of_persons']
        # total_price = serializer.validated_data['totalprice']
        total_price = 34.0
        register_instance = EventRegisterForm.objects.create(name=name,
                                                            email=email,
                                                            contact=contact,
                                                            number_of_persons = persons,
                                                            event=event_instance)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': 'Package',
                    },
                    'unit_amount': int(total_price * 100),
                },
                'quantity': 1,
            }
        ],
        
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + f"?id={id}" + "&session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )
    
    if name:
        
        PAYMENT.objects.create(eventregister=register_instance,
                               total_price = total_price,
                               status = 'Created',
                               stripe_payment_intent = checkout_session['payment_intent'],)
        
        return Response({'sessionId': checkout_session.id, 'home': False}, status=status.HTTP_200_OK)
    
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


class PaymentSuccessView(APIView):
    
    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        prodid = request.GET.get('id')
        prodid = int(prodid)
        if session_id is None or PAYMENT.objects.filter(session_id=session_id, status='Purchased').exists(): return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        try: session = stripe.checkout.Session.retrieve(session_id)
        except: return HttpResponseNotFound()
        service_order = get_object_or_404(PAYMENT, stripe_payment_intent=session.payment_intent)
        
        if service_order:
            service_order.status = 'Purchased'
            service_order.session_id = session_id
            service_order.save()
            
            
            return Response(status=status.HTTP_200_OK, data="Payment is Successfull")
        
        return Response(data="Something went wrong with Stripe. Please try again.")

def paymentfailed(request):
    return JsonResponse(data="Something went wrong with Stripe. Please try again.")
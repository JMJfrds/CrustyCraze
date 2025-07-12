from django.urls import path
from bv1.views import HomeView, AboutView, ServiceView, ProductView, TeamView, TestimonialView, ContactView, SuccessView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about_url'),
    path('service/', ServiceView.as_view(), name = 'service_url'),
    path('product/', ProductView.as_view(), name = 'product_url'),
    path('team/', TeamView.as_view(), name = 'team_url'), 
    path('testimonial/', TestimonialView.as_view(), name = 'testimonial_url'),
    path('contact/', ContactView.as_view(), name = 'contact_url'),
    path('success/', SuccessView.as_view(), name = 'success'),
]

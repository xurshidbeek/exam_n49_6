from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('popular/', views.popular, name='popular'),
    path('expensive/', views.expensive, name='popular'),
    path('cheap/', views.cheap, name='popular'),
    path('likes/', views.likes, name='likes'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('all_products/', views.all_products, name='all_products'),
    path('sale/', views.for_sale, name='sale'),
    path('top_news/', views.new_arr, name='top_news'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
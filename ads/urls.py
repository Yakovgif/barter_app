from . import views
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('', include('ads.urls')),
    path('api/', include('ads.api_urls')),
    path('', views.ad_list, name='ad_list'),
    path('ads/create/', views.ad_create, name='ad_create'),
    path('ads/<int:pk>/edit/', views.ad_edit, name='ad_edit'),
    path('ads/<int:pk>/delete/', views.ad_delete, name='ad_delete'),
    path('proposals/', views.proposal_list, name='proposal_list'),
    path('proposals/create/', views.proposal_create, name='proposal_create'),
]

schema_view = get_schema_view(
   openapi.Info(title="Barter API", default_version='v1'),
   public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
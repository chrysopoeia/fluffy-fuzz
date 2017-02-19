from rest_framework import routers
from django.conf.urls import url, include
from . import views


router = routers.DefaultRouter()
router.register('forecast', views.WeatherForecastViewSet)


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^forecast/$', views.Forecast.as_view(), name='forecast'),
    url(r'^api/', include(router.urls)),
]

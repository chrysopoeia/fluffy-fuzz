from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import WeatherForecastSerializer
from .models import WeatherForecast


class Home(TemplateView):
    template_name = 'forecast/index.html'


class Forecast(LoginRequiredMixin, ListView):
    template_name = 'forecast/forecast.html'
    queryset = WeatherForecast.objects.order_by('date')
    paginate_by = 3


class WeatherForecastViewSet(viewsets.ModelViewSet):
    queryset = WeatherForecast.objects.order_by('date')
    serializer_class = WeatherForecastSerializer
    permission_classes = (IsAuthenticated,)

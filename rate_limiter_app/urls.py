from rate_limiter_app.views import SetRateLimit,HandleTransaction
from django.urls import path

urlpatterns = [
    path('transaction/', HandleTransaction.as_view(), name='set_rate_limit'),
    path('set_rate_limit/', SetRateLimit.as_view(), name='set_rate_limit'),
]

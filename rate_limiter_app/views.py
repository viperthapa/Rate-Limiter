from django.http import JsonResponse
from .models import Merchant, RateLimit
from .utils import token_bucket_algorithm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import status


class SetRateLimit(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = ()
    http_method_names = [
        "post",
    ]

    def post(self, request, *args, **kwargs):
        merchant_id = request.data.get('merchant_id')
        limit_per_minute = int(request.data.get('limit_per_minute'))
        burst_limit = int(request.data.get('burst_limit'))
        
        merchant, _ = Merchant.objects.get_or_create(merchant_id=merchant_id)
        rate_limit, _ = RateLimit.objects.get_or_create(merchant=merchant)
        
        rate_limit.limit_per_minute = limit_per_minute
        rate_limit.burst_limit = burst_limit
        rate_limit.save()
        return Response(
                {"message": "Rate Limit has been set."}, status=status.HTTP_201_CREATED
            )


class HandleTransaction(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = ()
    http_method_names = [
        "post",
    ]

    def post(self, request, *args, **kwargs):
        merchant_id = request.POST.get('merchant_id')
        request_count = int(request.POST.get('request_count', 1))
        
        try:
            merchant = Merchant.objects.get(merchant_id=merchant_id)
            rate_limit = RateLimit.objects.get(merchant=merchant)
            
            if token_bucket_algorithm(rate_limit, request_count):
                rate_limit.save()
                return Response({'message': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'rate limit exceeded'}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        
        except Merchant.DoesNotExist:
            return Response({'message': 'merchant not found'}, status=status.HTTP_404_NOT_FOUND
)

       

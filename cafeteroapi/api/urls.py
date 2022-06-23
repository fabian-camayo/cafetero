from django.urls import path
from .views import Batchs, BatchUpdate, Notify, UserUpdate
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
urlpatterns = [
    path('api/v1/auth/access_token', obtain_jwt_token),
    path('api/v1/auth/refresh_token', refresh_jwt_token),
    path('api/v1/batchs', Batchs.as_view()),
    path('api/v1/update-batch/<int:item_id>', BatchUpdate.as_view()),
    path('api/v1/notify', Notify.as_view()),
    path('api/v1/update-user/<int:item_id>', UserUpdate.as_view()),
]

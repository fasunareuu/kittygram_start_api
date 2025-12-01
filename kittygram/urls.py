from django.urls import path, include

from cats.views import CatViewSet, OwnerViewSet, AchievementViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
   path('', include(router.urls)),
   # path('cats/<int:pk>/', CatViewSet.as_view()),
]

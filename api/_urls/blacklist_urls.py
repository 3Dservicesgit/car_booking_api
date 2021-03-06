import api._views.blacklist_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'create/', views.CreateBlacklistViewSet.as_view({'post': 'create'})),
    path('', views.ViewBlacklistsListViewSet.as_view(
        {'get': 'list'}), name="blacklist_endpoints"),
    path(r'<str:id>/', views.RetrieveBlacklistViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    # path(r'<str:id>/update/',
    #      views.UpdateBlacklistViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteBlacklistViewSet.as_view({'delete': 'destroy'})),
]

import api._views.passenger_notitification_views as views
from django.urls import path


urlpatterns = [
    path(r'', views.ViewPassengerNotificationsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreatePassengerNotificationViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrievePassengerNotificationViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdatePassengerNotificationViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeletePassengerNotificationViewSet.as_view({'delete': 'destroy'})),
]

from django.shortcuts import render
from api.models import Department
from rest_framework import viewsets
from api._serializers.department_serializers import DepartmentSerializer, CreateDepartmentSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateDepartmentViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = CreateDepartmentSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewDepartmentsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'departments' in cache:
            # get results from cache
            departments = cache.get('departments')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [department.to_json() for department in queryset]
            # store data in cache
            cache.set('departments', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveDepartmentViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateDepartmentViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteDepartmentViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

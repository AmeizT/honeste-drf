from apps.people.serializers import (
    AttendanceSerializer,
    AttendanceRegisterSerializer,
    HCAttendanceSerializer,
    HomecellSerializer,
    KindredSerializer,
    CreateKindredSerializer,
    MemberSerializer,
)
from django.shortcuts import render
from rest_framework.response import Response
from apps.people.permissions import IsAdminOrOverseer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, pagination, status
from apps.people.models import Attendance, AttendanceRegister, HCAttendance, Homecell, Kindred, Member


class StandardPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 1000000


class AttendanceView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Attendance.objects.filter(church=self.request.user.church)  # type: ignore
    
    

class AttendanceRegisterView(viewsets.ModelViewSet):
    queryset = AttendanceRegister.objects.all()
    serializer_class = AttendanceRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AttendanceRegister.objects.filter(branch=self.request.user.church)  # type: ignore


class HomeCellView(viewsets.ModelViewSet):
    queryset = Homecell.objects.all()
    serializer_class = HomecellSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Homecell.objects.filter(church=self.request.user.church)  # type: ignore


class HCAttendanceView(viewsets.ModelViewSet):
    queryset = HCAttendance.objects.all()
    serializer_class = HCAttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "slug"

    def get_queryset(self):
        return HCAttendance.objects.filter(church=self.request.user.church)  # type: ignore


class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "member_id"

    def get_queryset(self):
        return Member.objects.filter(church=self.request.user.church)  # type: ignore
    
    

class CreateKindredView(viewsets.ModelViewSet):
    queryset = Kindred.objects.all()
    serializer_class = CreateKindredSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "member_id"

    def get_queryset(self):
        return Kindred.objects.filter(church=self.request.user.church)  # type: ignore

    
        
class KindredView(viewsets.ModelViewSet):
    queryset = Kindred.objects.all()
    serializer_class = KindredSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "member_id"

    def get_queryset(self):
        return Kindred.objects.filter(church=self.request.user.church)  # type: ignore


class CreateMemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    http_method_names = ["post", "put", "patch"]
    permission_classes = [permissions.AllowAny]


class AttendanceAdminView(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["church__name"]
    pagination_class = StandardPagination


class MemberAdminView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["church__name"]
    pagination_class = StandardPagination

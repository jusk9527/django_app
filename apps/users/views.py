from rest_framework import mixins, viewsets
from rest_framework import permissions
from rest_framework.mixins import Response, status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

from .serializers import UserRegSerializer, UserDetailSerializer

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class UserViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        return []

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer
        return UserDetailSerializer

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()





from django.contrib import auth

from django.contrib.auth import get_user_model

User = get_user_model()






from users.models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
class StartDemo(APIView):
    def get(self,request):
        username = "admin123456"
        password = "admin123456"
        try:
            query_result = User(username=username,password=password, is_active=True,is_staff=True,is_superuser=True)


            # 设置密码
            query_result.set_password(password)
            query_result.save()


            from db_tools.test import Demo

        except:
            pass
        return Response("导入数据大概需要十分钟----正在导入数据")



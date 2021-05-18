from rest_framework import serializers  # 시리얼라이저 가져오기
from .models import User, Video


# Video 모델로 만든 데이터를 json 형태로 바꿔준다.
class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField(use_url=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Video
        fields = ['id', 'user_id', 'object', 'video', 'thumbnail']  # id는 pk로 쓰이는 자동 생성 필드


# User 모델로 만든 데이터를 json 형태로 바꿔준다.
class UserSerializer(serializers.ModelSerializer):
    user = VideoSerializer(many=True, read_only=True)   # 외래키

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'user', 'token']  # id는 pk로 쓰이는 자동 생성 필드




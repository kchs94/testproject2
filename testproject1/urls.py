from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # urls 간 연결해주는 함수
from loginapp import views, fcm  # 모델 가져오기

urlpatterns = [
    # 테스트

    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('users/', views.user_list),
    path('users/<int:pk>', views.user),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', views.update_token),

    path('videos/', views.video_list),
    path('videos/<int:pk>', views.video),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

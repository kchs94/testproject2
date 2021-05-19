from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import User, Video
from .serializers import UserSerializer, VideoSerializer


# 1-1.user_list - 계정 전체 조회(GET), 회원가입(POST)
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        query_set = User.objects.order_by('create_date')  # 모델에 있는 데이터를 query_set으로 다 담기
        serializer = UserSerializer(query_set, many=True)  # User 데이터를 json으로 변환
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # request에 있는 새로운 데이터를 data에 넣기
        serializer = UserSerializer(data=data)  # UserSerializer로 Json으로 변환
        if serializer.is_valid():  # 형식이 맞으면
            serializer.save()  # 저장
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# 1-2.user - pk로 특정 계정 조회(GET), 수정(PUT), 삭제(DELETE)
def user(request, pk):

    obj = User.objects.get(pk=pk)  # obj에 한 사용자 넣기

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


# 1-3.login - 로그인(POST)
@csrf_exempt
def login(request):
    if request.method == 'POST': # post로 받기
        data = JSONParser().parse(request)  # request json화 해서 data넣기
        search_email = data['email']        # email 변수에다가 request email 필드 값 넣기
        obj = User.objects.get(email=search_email)  #

        if data['password'] == obj.password:
            return HttpResponse(obj.id, status=200)
        else:
            return HttpResponse("400", status=400)

# 2-1.video_list
@csrf_exempt
def video_list(request):
    if request.method == 'GET':
        query_set = Video.objects.all()  # 모델에 있는 데이터를 query_set으로 다 담기
        serializer = VideoSerializer(query_set, many=True)  # User 데이터를 json으로 변환
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        video = Video()
        video.user_id = User.objects.get(id=request.POST['id'])
        video.object = request.POST['object']
        video.video = request.FILES['video']
        video.thumbnail = request.FILES['thumbnail']
        video.dateTime = request.POST['dateTime']
        video.save()
        return HttpResponse("OK")


# 2-2.user - pk로 특정 계정 조회(GET), 수정(PUT), 삭제(DELETE)
def video(request, pk):

    obj = User.objects.get(pk=pk)  # obj에 한 사용자 넣기

    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def update_token(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST["id"])
        user.token = request.POST["token"]
        user.save()
        return HttpResponse("OK", status=200)



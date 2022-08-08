import os
from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.settings import MEDIA_ROOT
from user.models import User


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # 회원가입
        #AJAX 로 데이터를 받아 DB 에 CREATE
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        password = request.data.get('password', None)
        name = request.data.get('name', None)

        User.objects.create(
                            email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.jpg"
                            )
        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None :
            #  로그인 실패
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):
            #  로그인 성공 세션 or 쿠키
            request.session['email'] = email
            return Response(status=200)
        else:
            #  로그인 실패
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")



class UploadProfile(APIView):
    def post(self, request):

        #파일 저장 기능
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex #이미지가 특수문자등 난해 할수 있어 uuid 로 생성된 이름 사용
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        #main.html의 AJAX 로 부터 데이터 받기
        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()


        return Response(status=200)

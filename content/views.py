import os
from uuid import uuid4

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from instagram.settings import MEDIA_ROOT
from user.models import User
from .models import Feed, Reply, Like, Bookmark


class Main(APIView):
    def get(self, request):
        # Feed 모든 데이터를 가져옴 -> select * from content_feed -> feed 를 최신부터 보여주기위해 order_by 사용
        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list=[]
        # 세션을 활용해 로그인한 사용자 데이터 받기
        email = request.session.get('email', None)

        user = User.objects.filter(email=email).first()
        user_info = User.objects.filter(email=email).first()
        print(user_info)

        # 세션에 이메일이 존재하지않을떄
        if email is None:
            render(request,"user/login.html")



        # 이메일 주소가 회원이 아닐떄
        if user is None:
            render(request, "user/login.html")


        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()

            #댓글 불러오기
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []

            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(
                                        reply_content=reply.reply_content,
                                        nickname=user.nickname,
                ))


            like_count=Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            is_marked = Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()

            feed_list.append(dict(
                                    id = feed.id,
                                    image=feed.image,
                                    content=feed.content,
                                    like_count=like_count,
                                    profile_image=user.profile_image,
                                    nickname=user.nickname,
                                    reply_list=reply_list,
                                    is_liked=is_liked,
                                    is_marked=is_marked,
                                    ))



        return render(request, "instagram/main.html", context=dict(feed=feed_list, user=user_info))


class UploadFeed(APIView):
    def post(self, request):

        #파일 저장 기능
        file = request.FILES['file']
        uuid_name = uuid4().hex #이미지가 특수문자등 난해 할수 있어 uuid 로 생성된 이름 사용
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        #main.html의 AJAX 로 부터 데이터 받기
        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email', None)

        #Feed.objects.create(image=image,content=content,user_id=user_id,profile_image=profile_image,like_count=0)
        Feed.objects.create(image=image,content=content, email=email)

        return Response(status=200)

class Profile(APIView):
    def get(self, request):
        # 세션을 활용해 로그인한 사용자 데이터 받기
        email = request.session.get('email')

        # 세션에 이메일이 존재하지않을떄
        if email is None:
            render(request,"user/login.html")

        user = User.objects.filter(email=email).first()

        # 이메일 주소가 회원이 아닐떄
        if user is None:
            render(request, "user/login.html")

        feed_list = Feed.objects.filter(email=email).all()
        my_like_list = list(Like.objects.filter(email=email, is_like=True).values_list('feed_id', flat=True))
        like_feed_list = Feed.objects.filter(id__in=my_like_list)

        bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id', flat=True))
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)

        return render(request, 'content/profile.html', context=dict(feed_list= feed_list,
                                                                    like_feed_list=like_feed_list,
                                                                    bookmark_feed_list=bookmark_feed_list,
                                                                    user=user))


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

        return Response(status=200)



class ToggleLike(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        favorite_text = request.data.get('favorite_text', True)
        email = request.session.get('email', None)

        if favorite_text == 'favorite_border':
            is_like = True
        else:
            is_like = False

        like = Like.objects.filter(feed_id=feed_id, email=email).first()
        if like:
            like.is_like =is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

        return Response(status=200)

class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)
        email = request.session.get('email', None)

        if bookmark_text == 'bookmark_border':
            is_marked = True
        else:
            is_marked = False

        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()
        if bookmark:
            bookmark.is_marked =is_marked
            bookmark.save()
        else:
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

        return Response(status=200)
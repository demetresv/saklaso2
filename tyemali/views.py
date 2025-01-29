from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post,Category
from .serializer import PostSerializer
import datetime

@api_view(['GET', 'POST'])
def post_list_and_create(request):
    
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()  # წიგნის შექმნა
            return Response(
                {"message": "წიგნი წარმატებით შექმნილია!", "post": PostSerializer(post).data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_update_and_detail(request, pk):

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"message": "post ვერ მოიძებნა."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=False)
        if serializer.is_valid():
            updated_post = serializer.save()
            return Response(
                {"message": "post წარმატებით განახლდა!", "post": PostSerializer(updated_post).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response({"message": "post წარმატებით წაიშალა."}, status=status.HTTP_204_NO_CONTENT)

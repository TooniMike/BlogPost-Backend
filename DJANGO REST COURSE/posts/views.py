from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

posts=[
    {"id": 1, "title": "Why is it difficult to learn Programming?", "content": "This is not soo hard"},
    {"id": 2, "title": "Why is it difficult to learn chess?", "content": "Try Chess.com stupid"},
    {"id": 3, "title": "Why is it difficult to learn drum?", "content": "Ask Nifemi"},
]

@api_view(http_method_names=['GET', 'POST'])
def homepage(request: Request):
    
    if request.method == 'POST':
        data = request.data
        response = {"message":"Hello World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def list_posts(request:Request):
    return Response(data=posts, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def post_detail(request:Request, post_index:int):
    post = posts[post_index]
    
    if post:
        return Response(data=post, status=status.HTTP_200_OK)
    return Response(data={"error":"Post not found"}, status=status.HTTP_404_NOT_FOUND)
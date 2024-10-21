from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

#  Create post and Get all the posts available in the database
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def create(self, request, *args, **kwargs):
        # Check if user is authenticated
        if request.user.is_authenticated:
            return super().create(request, *args, **kwargs)  # Call the original create method
        else:
            # Return a custom error response if the user is not authenticated
            return Response(
                {"error": "Authentication credentials were not provided or are invalid."},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def perform_create(self, serializer):
        # Set the user only if authenticated, as checked in `create`
        serializer.save(user=self.request.user)
        
        # to delete all of the post
    def delete(self, request, *args, **kwargs):
        # only the super user is allowed to delete all posts
        if request.user.is_superuser:
            num_deleted, _ = BlogPost.objects.all().delete()
            return Response({"message": f"Successfully deleted {num_deleted} posts."}, status= status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
    
    
# Get the list of a specific user blog posts
class UserBlogPost(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return BlogPost.objects.filter(user = user)
    


# Update and delete class for each user's post
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    
    def get_queryset(self):
        # Limit queryset to blog posts created by the authenticated user
        return BlogPost.objects.filter(user=self.request.user)
    
    # This is the APIView class for all blog posts
class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get the title from the query parameters (if none, default to empty string)
        title = request.query_params.get("title", "")
        
        if title:
            # filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # If no title is provided, return all blog posts
            blog_posts = BlogPost.objects.all()
            
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from rest_framework.permissions import AllowAny, IsAuthenticated


# # # Public View (no login required)
# # class PublicView(APIView):
# #     permission_classes = [AllowAny]

# #     def get(self, request):
# #         return Response({
# #             "message": "This is a public endpoint"
# #         })


# # # Private View (login required)
# # class PrivateView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         return Response({
# #             "message": "This is a private endpoint",
# #             "user": str(request.user)
# #         })


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Blog
# from .serializers import BlogSerializer
# from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt

# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
        
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)



from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

#api Only for authenticated users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        "username":user.username,
        "email": user.email,
        "is_staff": user.is_staff,
    })

#api Only for admin users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])  # Use IsAdminUser instead of IsAuthenticated
def admin_panel(request): 
    return Response({"message": f"Welcome to the admin panel, {request.user.username}."})                
        
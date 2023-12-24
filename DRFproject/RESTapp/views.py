from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student 
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


# Create your views here.



@api_view(['GET'])
def get_book(request):
    book_objs=Book.objects.all()
    serializers = Bookserializer(book_objs,many=True)
    return Response({'status':200,'payload':serializers.data})


class RegisterUser(APIView):
    def post(self,request):
        serializers = UserSerializer(data = request.data)

        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
        serializers.save()

        user = User.objects.get(username = serializers.data['username'])
        token_objs , _ = Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializers.data,'token':str(token_objs),'message':'your data is saved..'})    







class studentAPI(APIView):
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = studentSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    



    def post(self,request):
        serializers=studentSerializer(data=request.data)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
        serializers.save()
        return Response({'status':200,'payload':serializers.data,'message':'your data is saved..'})    


    def put(self,request):
        try:
            student_objs=Student.objects.get(id=id)
            serializers=studentSerializer(student_objs,data=request.data,partial=True)
            if not serializers.is_valid():
                print(serializers.errors)
                return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
            serializers.save()
            return Response({'status':200,'payload':serializers.data,'message':'your data is saved..'}) 
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})   


    def patch(self,request):
        def update_student(request,id):
            try:
                student_objs=Student.objects.get(id=id)
                serializers=studentSerializer(student_objs,data=request.data,partial=True)
                if not serializers.is_valid():
                    print(serializers.errors)
                    return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
                serializers.save()
                return Response({'status':200,'payload':serializers.data,'message':'your data is saved..'}) 
            except Exception as e:
                print(e)
                return Response({'status':403,'message':'invalid id'})   




    def delete(self,request):
        try:
            student_objs = Student.objects.get(id=id)
            student_objs.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})


# @api_view(['GET' ])
# def home(request):
#     student_objs=Student.objects.all()
#     serializers=studentSerializer(student_objs,many=True)
#     return Response({'status':200,'payload':serializers.data})

# @api_view(['POST' ])
# def post_student(request):
#     serializers=studentSerializer(data=request.data)

#     if not serializers.is_valid():
#         print(serializers.errors)
#         return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
#     serializers.save()
#     return Response({'status':200,'payload':serializers.data,'message':'your data is saved..'})    


# @api_view(['PUT' ])
# def update_student(request,id):
#     try:
#         student_objs=Student.objects.get(id=id)
#         serializers=studentSerializer(student_objs,data=request.data,partial=True)
#         if not serializers.is_valid():
#             print(serializers.errors)
#             return Response({'status':200,'errors':serializers.errors,'message':"something is wrong"})
#         serializers.save()
#         return Response({'status':200,'payload':serializers.data,'message':'your data is saved..'}) 
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})   



# @api_view(['DELETE' ])
# def delete_student(request,id):
#     try:
#         student_objs = Student.objects.get(id=id)
#         student_objs.delete()
#         return Response({'status':200,'message':'deleted'})
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})



     
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import serializers
from .models import Book
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['waga'] = 'some other token content'
        # ...
        return token




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def index(req):
    return Response('hello')


@api_view(['GET','POST','DELETE','PUT'])
def Books(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_task=Book.objects.get(id=id)
                return Response (BookSerializer(temp_task,many=False).data)
            except Book.DoesNotExist:
                return Response ("not found")
        all_tasks=BookSerializer(Book.objects.all(),many=True).data
        return Response ( all_tasks)
    if req.method =='POST':
        tsk_serializer = BookSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_task=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_task.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_task=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")
        ser = BookSerializer(data=req.data)
        old_task = Book.objects.get(id=id)
        res = ser.update(old_task, req.data)
        return Response('updated.....')
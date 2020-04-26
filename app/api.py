from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class Clients(APIView):
	#get api logic
	def get(self,request):
		#getting all the clients available in db
		data = clients.objects.all()
		serializer = ClientSerializer(data,many=True)
		return Response(serializer.data)
	#post api logic
	def post(self, request):
		serializer = ClientSerializer(data=request.data)
		print (request.data)
		#if req valid
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
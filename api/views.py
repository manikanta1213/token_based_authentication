from gzip import READ
from django.shortcuts import render
from rest_framework.response import Response
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import logging as Logger  
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class MessageView(APIView):
    permission_classes = (IsAuthenticated,)             
    def post(self, request):
        user = str(request.user)
        user = User.objects.get(username=user)
        body = request.data['body']

        #filters user requests in the last 1hour
        this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
        one_hour_later = this_hour + timedelta(hours=1)
        message_count = Message.objects.filter(created__range=(this_hour, one_hour_later)).filter(user=user.id)
        #no more than 10 requests per user are allowed within an hour
        if message_count.count()>10:
            print(message_count.count())
            return Response("Only 10 messages allowed per hour. Please try after 1 hour")

        #addind the message in the table Message
        message = Message.objects.create(
            user = request.user,
            body = body
        )
        output = {
            "id": message.id,
            "message":message.body,
            "created_at": message.created,
            "updated_at": message.updated,
            "created_by":{
                "id": user.id,
                "username":user.username,
                "email": user.email
                }
            }
        return  Response(output)


class MessageUpdateView(APIView):
    permission_classes = (IsAuthenticated,)             
    def post(self, request, id):
        user = str(request.user)
        user = User.objects.get(username=user)
        body = request.data['body']

        #filters user requests in the last 1hour
        this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
        one_hour_later = this_hour + timedelta(hours=1)
        message_count = Message.objects.filter(updated__range=(this_hour, one_hour_later)).filter(user=user.id)
        #no more than 10 requests per user are allowed within an hour
        if message_count.count()>10:
            print(message_count.count())
            return Response("Only 10 messages allowed per hour. Please try after 1 hour")

        #addind the message in the table Message
        message = Message.objects.get(id=id)
        message.body=body
        message.save()
        output = {
            "id": message.id,
            "message":message.body,
            "created_at": message.created,
            "updated_at": message.updated,
            "created_by":{
                "id": user.id,
                "username":user.username,
                "email": user.email
                }
            }
        return  Response(output)

class MessageDeleteView(APIView):
    permission_classes = (IsAuthenticated,)             
    def delete(self, request, id):
        user = str(request.user)
        user = User.objects.get(username=user)

        #filters user requests in the last 1hour
        this_hour = timezone.now().replace(minute=0, second=0, microsecond=0)
        one_hour_later = this_hour + timedelta(hours=1)
        message_count = Message.objects.filter(created__range=(this_hour, one_hour_later)).filter(user=user.id)
        #no more than 10 requests per user are allowed within an hour
        if message_count.count()>10:
            print(message_count.count())
            return Response("Only 10 messages allowed per hour. Please try after 1 hour")

        #addind the message in the table Message
        message = Message.objects.get(id=id)
        message.delete()

        return  Response("Message Deleted")

class MessageGetView(APIView):
    permission_classes = (IsAuthenticated,)             
    def get(self, request, id):
        user = str(request.user)
        user = User.objects.get(username=user)

        #addind the message in the table Message
        try:
            message = Message.objects.get(id=id)
        except Exception as e:
            return Response("No records Found for the message id : {}".format(id))
        output = {
            "id": message.id,
            "message":message.body,
            "created_at": message.created,
            "updated_at": message.updated,
            "created_by":{
                "id": user.id,
                "username":user.username,
                "email": user.email
                }
            }
        return  Response(output)


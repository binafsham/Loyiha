from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, ReytingSerializer, MockTestSerializer, UniversitetSerializer, SozlamalarSerializer, YutuqSerializer
from .models import User, Reyting, MockTest, Universitet, Sozlamalar, Yutuq

# Create your views here.

class UserListAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer_data = UserSerializer(user, many=True).data
        data = {
            "status": f"Returned{len(user)} user",
            "user": serializer_data
        }
        return Response(data)

class UserCreateAPIView(APIView):
    def post(self, request):
        user = User.objects.all()
        serializer_data = UserSerializer(user, many=True).data
        data = {
            "status": f"Returned{len(user)} user",
            "user": serializer_data
        }
        return Response(data)


class UserUpdateAPIView(APIView):
    def put(self, request):
        user = User.objects.all()
        serializer_data = UserSerializer(user, many=True).data
        data = {
            "status": f"Returned{len(user)} user",
            "user": serializer_data
        }
        return Response(data)

class UserDeleteAPIView(APIView):
    def delete(self, request):
        user = User.objects.all()
        serializer_data = UserSerializer(user, many=True).data
        data = {
            "status": f"Returned{len(user)} user",
            "user": serializer_data
        }
        return Response(data)

class UserRetrieveAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer_data = UserSerializer(user, many=True).data
        data = {
            "status": f"Returned{len(user)} user",
            "user": serializer_data
        }
        return Response(data)




class ReytingListAPIView(APIView):
    def get(self, request):
        reyting = Reyting.objects.all()
        serializer_data = ReytingSerializer(reyting, many=True).data
        data = {
            "status": f"Returned{len(reyting)} reyting",
            "reyting": serializer_data
        }
        return Response(data)

class ReytingCreateAPIView(APIView):
    def post(self, request):
        reyting = Reyting.objects.all()
        serializer_data = ReytingSerializer(reyting, many=True).data
        data = {
            "status": f"Returned{len(reyting)} reyting",
            "reyting": serializer_data
        }
        return Response(data)


class ReytingUpdateAPIView(APIView):
    def put(self, request):
        reyting = Reyting.objects.all()
        serializer_data = ReytingSerializer(reyting, many=True).data
        data = {
            "status": f"Returned{len(reyting)} reyting",
            "reyting": serializer_data
        }
        return Response(data)


class ReytingDeleteAPIView(APIView):
    def delete(self, request):
        reyting = Reyting.objects.all()
        serializer_data = ReytingSerializer(reyting, many=True).data
        data = {
            "status": f"Returned{len(reyting)} reyting",
            "reyting": serializer_data
        }
        return Response(data)


class ReytingRetrieveAPIView(APIView):
    def get(self, request):
        reyting = Reyting.objects.all()
        serializer_data = ReytingSerializer(reyting, many=True).data
        data = {
            "status": f"Returned{len(reyting)} reyting",
            "reyting": serializer_data
        }
        return Response(data)




class MockTestListAPIView(APIView):
    def get(self, request):
        mocktest = MockTest.objects.all()
        serializer_data = MockTestSerializer(mocktest, many=True).data
        data = {
            "status": f"Returned{len(mocktest)} mocktest",
            "mocktest": serializer_data
        }
        return Response(data)


class MockTestCreateAPIView(APIView):
    def post(self, request):
        mocktest = MockTest.objects.all()
        serializer_data = MockTestSerializer(mocktest, many=True).data
        data = {
            "status": f"Returned{len(mocktest)} mocktest",
            "mocktest": serializer_data
        }
        return Response(data)

class MockTestUpdateAPIView(APIView):
    def put(self, request):
        mocktest = MockTest.objects.all()
        serializer_data = MockTestSerializer(mocktest, many=True).data
        data = {
            "status": f"Returned{len(mocktest)} mocktest",
            "mocktest": serializer_data
        }
        return Response(data)

class MockTestDeleteAPIView(APIView):
    def delete(self, request):
        mocktest = MockTest.objects.all()
        serializer_data = MockTestSerializer(mocktest, many=True).data
        data = {
            "status": f"Returned{len(mocktest)} mocktest",
            "mocktest": serializer_data
        }
        return Response(data)


class MockTestRetrieveAPIView(APIView):
    def get(self, request):
        mocktest = MockTest.objects.all()
        serializer_data = MockTestSerializer(mocktest, many=True).data
        data = {
            "status": f"Returned{len(mocktest)} mocktest",
            "mocktest": serializer_data
        }
        return Response(data)




class UniversitetListAPIView(APIView):
    def get(self, request):
        universitet = Universitet.objects.all()
        serializer_data = UniversitetSerializer(universitet, many=True).data
        data = {
            "status": f"Returned{len(universitet)} universitet",
            "universitet": serializer_data
        }
        return Response(data)

class UniversitetCreateAPIView(APIView):
    def post(self, request):
        universitet = Universitet.objects.all()
        serializer_data = UniversitetSerializer(universitet, many=True).data
        data = {
            "status": f"Returned{len(universitet)} universitet",
            "universitet": serializer_data
        }
        return Response(data)


class UniversitetUpdateAPIView(APIView):
    def put(self, request):
        universitet = Universitet.objects.all()
        serializer_data = UniversitetSerializer(universitet, many=True).data
        data = {
            "status": f"Returned{len(universitet)} universitet",
            "universitet": serializer_data
        }
        return Response(data)

class UniversitetDeleteAPIView(APIView):
    def delete(self, request):
        universitet = Universitet.objects.all()
        serializer_data = UniversitetSerializer(Universitet, many=True).data
        data = {
            "status": f"Returned{len(universitet)} universitet",
            "universitet": serializer_data
        }
        return Response(data)

class UniversitetRetrieveAPIView(APIView):
    def get(self, request):
        universitet = Universitet.objects.all()
        serializer_data = UniversitetSerializer(universitet, many=True).data
        data = {
            "status": f"Returned{len(universitet)} universitet",
            "universitet": serializer_data
        }
        return Response(data)



class SozlamalarListAPIView(APIView):
    def get(self, request):
        sozlamalar = Sozlamalar.objects.all()
        serializer_data = SozlamalarSerializer(sozlamalar, many=True).data
        data = {
            "status": f"Returned{len(sozlamalar)} sozlamalar",
            "sozlamalar": serializer_data
        }
        return Response(data)

class SozlamalarCreateAPIView(APIView):
    def post(self, request):
        sozlamalar = Sozlamalar.objects.all()
        serializer_data = SozlamalarSerializer(sozlamalar, many=True).data
        data = {
            "status": f"Returned{len(sozlamalar)} sozlamalar",
            "sozlamalar": serializer_data
        }
        return Response(data)

class SozlamalarUpdateAPIView(APIView):
    def put(self, request):
        sozlamalar = Sozlamalar.objects.all()
        serializer_data = SozlamalarSerializer(sozlamalar, many=True).data
        data = {
            "status": f"Returned{len(sozlamalar)} sozlamalar",
            "sozlamalar": serializer_data
        }
        return Response(data)

class SozlamalarDeleteAPIView(APIView):
    def delete(self, request):
        sozlamalar = Sozlamalar.objects.all()
        serializer_data = SozlamalarSerializer(sozlamalar, many=True).data
        data = {
            "status": f"Returned{len(sozlamalar)} sozlamalar",
            "sozlamalar": serializer_data
        }
        return Response(data)

class SozlamalarRetrieveAPIView(APIView):
    def get(self, request):
        sozlamalar = Sozlamalar.objects.all()
        serializer_data = SozlamalarRetrieveAPIView(sozlamalar, many=True).data
        data = {
            "status": f"Returned{len(sozlamalar)} sozlamalar",
            "sozlamalar": serializer_data
        }
        return Response(data)



class YutuqListAPIView(APIView):
    def get(self, request):
        yutuq = Yutuq.objects.all()
        serializer_data = YutuqSerializer(yutuq, many=True).data
        data = {
            "status": f"Returned{len(yutuq)} yutuq",
            "yutuq": serializer_data
        }
        return Response(data)

class YutuqCreateAPIView(APIView):
    def post(self, request):
        yutuq = Yutuq.objects.all()
        serializer_data = YutuqSerializer(yutuq, many=True).data
        data = {
            "status": f"Returned{len(yutuq)} yutuq",
            "yutuq": serializer_data
        }
        return Response(data)


class YutuqUpdateAPIView(APIView):
    def put(self, request):
        yutuq = Yutuq.objects.all()
        serializer_data = YutuqSerializer(yutuq, many=True).data
        data = {
            "status": f"Returned{len(yutuq)} yutuq",
            "yutuq": serializer_data
        }
        return Response(data)


class YutuqDeleteAPIView(APIView):
    def delete(self, request):
        yutuq = Yutuq.objects.all()
        serializer_data = YutuqSerializer(yutuq, many=True).data
        data = {
            "status": f"Returned{len(yutuq)} yutuq",
            "yutuq": serializer_data
        }
        return Response(data)


class YutuqRetrieveAPIView(APIView):
    def get(self, request):
        yutuq = Yutuq.objects.all()
        serializer_data = YutuqSerializer(yutuq, many=True).data
        data = {
            "status": f"Returned{len(yutuq)} yutuq",
            "yutuq": serializer_data
        }
        return Response(data),                                                                                                                                                                                                                    Vievsga

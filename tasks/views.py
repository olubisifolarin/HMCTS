from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from rest_framework.exceptions import ValidationError

class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            task = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as exc:
            return Response({'errors': exc.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({'error': 'Server error', 'detail': str(exc)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

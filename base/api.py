from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from .models import LearningData
from base.models import User
from .serializers import LearningDataSerializer

@csrf_exempt
@require_http_methods(["GET"])
def learning_data_list(request):
    """
    List all learning data for the logged-in user.
    """
    if request.method == 'GET':
        # Filter the learning data by the logged-in user's ID
        learning_data = LearningData.objects.filter(user=request.user)
        serializer = LearningDataSerializer(learning_data, many=True)
        data_attribute_list = [item['data'] for item in serializer.data if 'data' in item]

        print(data_attribute_list)
        return JsonResponse(data_attribute_list, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def learning_data_create(request):
    """
    Append to or create learning data instance.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        # Retrieve the authenticated user from the request
        user = request.user if request.user.is_authenticated else None
        if not user:
            return JsonResponse({'error': 'User not authenticated.'}, status=401)

        # Try to retrieve the existing LearningData instance for the user
        try:
            learning_data = LearningData.objects.get(user=user)
            # If found, append the new data object to the existing array
            if not isinstance(learning_data.data, list):
                learning_data.data = []  # Initialize as list if it's not

            learning_data.data.append(data)
            learning_data.save()
            return JsonResponse({'message': 'Data updated successfully'}, status=200)

        except LearningData.DoesNotExist:
            # If not found, create a new instance with the data as a list
            serializer = LearningDataSerializer(data={'user': user.id, 'data': [data]})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def learning_data_detail(request, pk):
    """
    Retrieve, update or delete a learning data instance.
    """
    try:
        learning_data = LearningData.objects.get(pk=pk)
    except LearningData.DoesNotExist:
        return JsonResponse({'message': 'The learning data does not exist'}, status=404)

    if request.method == 'GET':
        serializer = LearningDataSerializer(learning_data)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LearningDataSerializer(learning_data, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        learning_data.delete()
        return JsonResponse({'message': 'Learning data was deleted successfully'}, status=204)

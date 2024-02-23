import json
from django.http import JsonResponse
from utils import chat_char

david = chat_char.Character("You are a helpful assistant", "David")

# Create your views here.
def index(request):
    return JsonResponse({"Message": "Success"})

def message(request):
    try:
        content = json.loads(request.body)
        message = content.get("content")
        bot_response = david.cont(message)
        return JsonResponse({"Response": bot_response})
    
    except json.JSONDecodeError:
        return JsonResponse({"Error": "Something went wrong"})
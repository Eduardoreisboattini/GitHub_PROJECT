import os
import json
import azure.identity
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class AzureAuthBackend(ModelBackend):
    def authenticate(self, request, token=None):
        try:
            credential = azure.identity.DefaultAzureCredential()
            client = azure.identity.AzureCliCredential(credential)
            token_acquired = client.get_token("https://graph.microsoft.com/.default")
            if token_acquired and token_acquired.token:
                headers = {'Authorization': f'Bearer {token_acquired.token}'}
                response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers).json()
                user = User.objects.get_or_create(username=response['userPrincipalName'])[0]
                user.email = response['mail']
                user.first_name = response['givenName']
                user.last_name = response['surname']
                user.save()
                return user
        except Exception as e:
            print(e)
        return None

@csrf_exempt
def azure_auth(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        user = AzureAuthBackend().authenticate(request, token)
        if user:
            return JsonResponse({'detail': 'Authenticated successfully.'})
        return JsonResponse({'detail': 'Authentication failed.'}, status=401)
    return JsonResponse({'detail': 'Invalid request.'}, status=400)
<<<<<<<  7c51aad0-8264-4375-a89e-4251f19fba87  >>>>>>>
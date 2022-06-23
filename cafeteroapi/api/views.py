from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from .models import Batch
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import datetime
from passlib.hash import django_pbkdf2_sha256 as handler
import telnyx


@method_decorator(csrf_exempt, name='dispatch')
class Batchs(APIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        print("DATA BATCHS>>>", data)

        code = data.get('code')
        weight = data.get('weight')
        contact_name = data.get('contact_name')
        contact = data.get('contact')
        coffe_type = data.get('coffe_type')
        varieties = data.get('varieties')
        features = data.get('features')
        state = data.get('state')
        history = {
            state: {
                "weight": weight,
                "features": features,
                "created_date": timezone.now
            }
        }

        print("HISTORY>>", history)

        batch_data = {
            'code': code,
            'weight': weight,
            'contact_name': contact_name,
            'contact': contact,
            'coffe_type': coffe_type,
            'varieties': varieties,
            'features': features,
            'history_recoleccion': str(history),
            'state': state
        }

        item = Batch.objects.create(**batch_data)

        data = {
            "message": f"Nuevo Lote agregado con ID: {item.code}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        count = Batch.objects.count()
        items = Batch.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'id': item.id,
                'code': item.code,
                'weight': item.weight,
                'contact_name': item.contact_name,
                'contact': item.contact,
                'coffe_type': item.coffe_type,
                'varieties': item.varieties,
                'features': item.features,
                'state': item.state,
                'created_date': item.created_date,
                'update_date': item.update_date,
                'history_recoleccion': item.history_recoleccion,
                'history_despulpado': item.history_despulpado,
                'history_fermentacion': item.history_fermentacion,
                'history_lavado': item.history_lavado,
                'history_secado': item.history_secado,
                'history_trillado': item.history_trillado,
                'history_almacenado': item.history_almacenado,
                'history_tostado': item.history_tostado,
                'history_etiquetado': item.history_etiquetado
            })

        data = {
            'items': items_data,
            'count': count,
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class BatchUpdate(APIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = Batch.objects.get(id=item_id)
        item.code = data.get('code')
        item.weight = data.get('weight')
        item.coffe_type = data.get('coffe_type')
        item.varieties = data.get('varieties')
        item.features = data.get('features')

        history_new = {
            "weight": item.weight,
            "features": item.features,
            "created_date": timezone.now
        }
        state_old = item.state
        if (state_old == "RECOLECCION"):
            item.state = "DESPULPADO"
            item.history_despulpado = {
                item.state: history_new}

        if (state_old == "DESPULPADO"):
            item.state = "FERMENTACION"
            item.history_fermentacion = {
                item.state: history_new}
        if (state_old == "FERMENTACION"):
            item.state = "LAVADO"
            item.history_lavado = {
                item.state: history_new}
        if (state_old == "LAVADO"):
            item.state = "SECADO"
            item.history_secado = {
                item.state: history_new}
        if (state_old == "SECADO"):
            item.state = "TRILLADO"
            item.history_trillado = {
                item.state: history_new}
        if (state_old == "TRILLADO"):
            item.state = "ALMACENADO"
            item.history_almacenado = {
                item.state: history_new}
        if (state_old == "ALMACENADO"):
            item.state = "TOSTADO"
            item.history_tostado = {
                item.state: history_new}
        if (state_old == "TOSTADO"):
            item.state = "ETIQUETADO"
            item.history_etiquetado = {
                item.state: history_new}
        if (state_old == "ETIQUETADO"):
            item.state = "ETIQUETADO"
            item.history_etiquetado = {
                item.state: history_new}

        item.save()

        data = {
            'message': f'Se actualizó el elemento {item_id}'
        }

        return JsonResponse(data)

    def delete(self, request, item_id):
        item = Batch.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Se eliminó el elemento {item_id}'
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class Notify(APIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))

        telnyx.api_key = "YOU_KEY"

        your_telnyx_number = "YOU_NUMBER"
        destination_number = data['contact']

        telnyx.Message.create(
            from_=your_telnyx_number,
            to=destination_number,
            text=data['message'],
        )
        data = {
            "message": f"El mensaje fue enviado"
        }
        return JsonResponse(data, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdate(APIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def put(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = User.objects.get(id=item_id)
        item.username = data.get('username')
        item.password = handler.hash(data.get('password'))
        print(item.password)
        item.save()

        data = {
            'message': f'Se actualizó el elemento {item_id}'
        }

        return JsonResponse(data)

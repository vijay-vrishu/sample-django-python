import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from api.models import Inventory


class InventoriesView(View):

    def get(self, request):

        invs = list(Inventory.objects.all().values())
        return JsonResponse(invs, safe=False)

    def post(self, request):
        values = json.loads(request.body)
        inv = Inventory(**values)
        inv.save()
        return JsonResponse(None, safe=False, status=201)


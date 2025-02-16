from django.http import HttpResponse
from uploader.models import Page, Zine 
from uploader.serializers import ZineSerializer, PageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import pdb

from rest_framework import viewsets

class ZineViewSet(viewsets.ModelViewSet):
    queryset = Zine.objects.all().order_by('name')
    serializer_class = ZineSerializer

class PageViewSet(viewsets.ModelViewSet):
    model = Page
    queryset = Page.objects.all().order_by('id')
    serializer_class = PageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = self.queryset
        if self.request.query_params.get('zine'):
            zine = self.request.query_params.get('zine')
            return queryset.filter(zine=zine) 
        return queryset

    def partial_update(self, request, *args, **kwargs):
        # TODO: This is probably not going to scale well. Replace this with a
        # smarter way to represent and swap ordered pages.
        index = int(request.data['index'])
        current_pk = int(kwargs['pk'])
        zine = Page.objects.get(pk=current_pk).zine

        try:
            page_at_index = Page.objects.get(index=index, zine=zine)
            page_at_index.index = request.data['current_index']
            page_at_index.save()
        except Page.DoesNotExist:
            pass

        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

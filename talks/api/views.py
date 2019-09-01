from rest_framework import generics
from ..models import Talk
from ..search import search
from .serializers import TalkSerializer


class TalkList(generics.ListAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q is not None:
            return search(q)
        return super().get_queryset()

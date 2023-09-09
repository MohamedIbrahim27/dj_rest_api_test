from.models import Proucts
from.serializer import ProuctsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from django.http import HttpResponse

# this is api decomation
# http://127.0.0.1:6589/api-documentation/



class ProuctsAPiList(ListCreateAPIView):
    queryset=Proucts.objects.all()
    serializer_class = ProuctsSerializers
    permission_classes = [IsAuthenticated]
    
class ProuctsAPiList_by_filter(ListCreateAPIView):
    serializer_class = ProuctsSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        gender_filter = self.request.query_params.get('gender', None)

        if gender_filter:
            queryset = Proucts.objects.filter(gender=gender_filter)
        return queryset


class ProuctsAPiDetail(RetrieveUpdateDestroyAPIView):
    queryset=Proucts.objects.all()
    serializer_class = ProuctsSerializers
    permission_classes = [IsAuthenticated]


def home(request):
    return HttpResponse("hello")

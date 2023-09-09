from rest_framework import serializers
from.models import Proucts


class ProuctsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Proucts
        fields = "__all__"
    
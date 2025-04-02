from rest_framework import serializers
from services.models import Subscription

class SubscriptionSerializers(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name', read_only=True)
    email = serializers.CharField(source='client.user.email', read_only=True)
    
    
    class Meta:
        model = Subscription
        fields = '__all__'

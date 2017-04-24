from BangazonAPI.bangazon.models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """Convert Customer model to JSON"""
    class Meta:
        """Global options for Customer class"""
        model = Customer
        fields = ('firstname', 'lastname', 'status', 'date_created', 'date_last_active')


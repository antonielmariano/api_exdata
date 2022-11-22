from rest_framework import serializers
from billing.models import Billing
import ipdb


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = "__all__"
        read_only_fields = ["id"]

class BillingValueQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ["quantity", "value_billing"]




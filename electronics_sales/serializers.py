from rest_framework import serializers

from electronics_sales.models import Factory, RetailNetwork, IndividualEntrepreneur


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = '__all__'
        read_only_fields = ['debt']


class RetailNetworkSerializer(serializers.ModelSerializer):
    # provider_url = serializers.SerializerMethodField()

    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ['debt']


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
        read_only_fields = ['debt']

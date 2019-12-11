from rest_framework import serializers
from .models import Algorithm

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ('id', 'prob_num', 'prob_source', 'prob_name', 'prob_diff', 'prob_category', 'code_url',)        
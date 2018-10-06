from rest_framework import serializers
from .models import Scrip, INDEX_CHOICES



class ScripSerializer(serializers.ModelSerializer):
    my_field = serializers.SerializerMethodField('named_bar')

    def named_bar(self, foo):
      return foo.name

    class Meta:
        model = Scrip
        fields = ("ticker", "name", "index", "my_field")

# class ScripSerializer(serializers.ModelSerializer):
#     ticker = serializers.CharField(required=True, allow_blank=False, max_length=200)
#     name = serializers.CharField(required=True, allow_blank=False, max_length=200)
#     index = serializers.ChoiceField(choices=INDEX_CHOICES, default='Nifty')

    # def create(self, validated_data):
    #     return Scrip.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.ticker = validated_data.get('ticker', instance.ticker)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.index = validated_data.get('index', instance.index)
    #     instance.save()

    #     return instance
    # class Meta:
    #     model = Scrip
    #     fields = ("ticker", "name", "index")
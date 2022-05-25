from dataclasses import dataclass
from rest_framework import serializers
from entries.models import Entry

class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.DateTimeField()

    def create(self, validated_data):
        # Voy a salvar a validated dataclass
        instance = Entry(
            datetime=validated_data.get("datetime"),
            concept=validated_data.get("concept"),
            amount=validated_data.get("amount")
        )

        instance.save()
        return instance


    def update(self, instance, validated_data):
        # Voy a modificar instancia con validated data
        pass
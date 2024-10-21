from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 50)
    content = serializers.CharField()
    created = serializers.DateTimeField(read_only = True)
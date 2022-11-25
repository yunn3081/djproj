from rest_framework import serializers
from musics.models import Music
from rest_framework import serializers

# class MusicSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     song = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     singer = serializers.CharField(required=True)
#     release_date = serializers.CharField(required=False)

#     class Meta:
#         model = Music
#         fields = ('id', 'song', 'singer', 'release_date')

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__' #這一行跟下面一行是一樣的意思
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')

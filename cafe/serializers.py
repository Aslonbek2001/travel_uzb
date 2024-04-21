from .models import Cafe, CafeImages, Foods
from rest_framework.serializers import Serializer, ModelSerializer



class FoodsSerializer(ModelSerializer):
    class Meta:
        model = Foods
        fields = ('cafe', 'name', 'price', 'type', 'image', 'description')


class CafeSerializer(ModelSerializer):
    class Meta:
        model = Cafe
        fields = ('id', 'user','name', 'address', 'info', 'image', 'phone')

class CafeImagesSerializer(ModelSerializer):
    class Meta:
        model = CafeImages
        fields = ('image',)

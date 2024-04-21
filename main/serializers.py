from .models import Qadamjo, AboutUs, AboutImages, FotoPlus
from rest_framework.serializers import Serializer, ModelSerializer

class QadamjoSeralizer(ModelSerializer):
    class Meta:
        model = Qadamjo
        fields = ('title', 'short_title', 'image', 'status', 'description')


class QadamjoFotoSerial(ModelSerializer):
    class Meta:
        model = FotoPlus
        fields = ('image')

class AboutImagesSeralizer(ModelSerializer):
    class Meta:
        model = AboutImages
        fields = ('about', 'image')

class AboutUsSeralizer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('title', 'image', 'status', 'description')

        
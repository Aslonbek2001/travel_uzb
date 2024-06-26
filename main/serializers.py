from .models import Qadamjo, AboutUs, AboutImages, FotoPlus
from rest_framework.serializers import Serializer, ModelSerializer

class QadamjoSeralizer(ModelSerializer):
    class Meta:
        model = Qadamjo
        fields = "__all__"


class QadamjoFotoSerial(ModelSerializer):
    class Meta:
        model = FotoPlus
        fields = "__all__"

class AboutImagesSeralizer(ModelSerializer):
    class Meta:
        model = AboutImages
        fields = "__all__"

class AboutUsSeralizer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("id", 'title', 'image', 'status', 'description')

        
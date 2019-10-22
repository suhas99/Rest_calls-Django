from rest_framework import routers, serializers, viewsets
from .models import personDetails


class personDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = personDetails
        fields = ['firstName', 'email', 'github']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = personDetails.objects.all()
    serializer_class = personDetailsSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

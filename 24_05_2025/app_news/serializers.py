from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import News

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsListSerializer(ModelSerializer):
    list=SerializerMethodField('get_list')
    class Meta:
        model=News
        fields=('title','description','views_count','created_at','list',)

    def get_list(self,obj):
        return f'http://127.0.0.1:8000/news/{obj.id}'
from rest_framework import serializers
from application.api.models import Store, Article


class ArticleSerializer(serializers.ModelSerializer):
    store_name = serializers.PrimaryKeyRelatedField(source='store', queryset=Store.objects.all())

    class Meta:
        model = Article
        fields = ('id', 'name', 'price', 'description', 'store_name', 'total_in_shelf', 'total_in_vault')


class StoreSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Store


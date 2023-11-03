from rest_framework import serializers
from backend.models import Shop, Category, Products, ProductInfo, ProductParameter, User, Contact, Order, OrderItem


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }


class UserSerializer(serializers.ModelSerializer):
    # contacts = ContactSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts')
        read_only_fields = ('id',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'url', 'filename')


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    shops = ShopCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'shops',)


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductsSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Products
        fields = ('name', 'category',)


class ProductInfoShopAndProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('name',)

    class Meta:
        model = Products
        fields = ('name',)


class ProductInfoSerializer(serializers.ModelSerializer):
    shop = ProductInfoShopAndProductSerializer()
    name = ProductInfoShopAndProductSerializer()

    class Meta:
        model = ProductInfo
        fields = ('shop', 'name', 'quantity', 'price', 'price_rrc')


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = ('parameter', 'value',)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product_info', 'quantity', 'order',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'order': {'write_only': True}
        }


class OrderItemCreateSerializer(OrderItemSerializer):
    product_info = ProductInfoSerializer(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemCreateSerializer(read_only=True, many=True)

    total_sum = serializers.IntegerField()
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'ordered_items', 'state', 'dt', 'total_sum', 'contact',)
        read_only_fields = ('id',)




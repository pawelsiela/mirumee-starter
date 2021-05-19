
import graphene

from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant


class ProductCreateInput(graphene.InputObjectType):
    price = graphene.Decimal(Required=True)
    description = graphene.String(Required=True)
    quantity = graphene.Int()


class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)


class ProductVariantCreateInput(graphene.InputObjectType):
    product = graphene.String(required=True)
    name = graphene.String(required=True)
    sku = graphene.String(required=True)
    price = graphene.Decimal(required=True)


class ProductVariantCreate(graphene.Mutation):
    product_variant = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput(required=True)
        product_id = graphene.ID(required=True)

    @classmethod
    def clean_input(cls, data):
        return data
    @classmethod
    def mutate(cls, root, info, input, product_id):
        cleaned_input = cls.clean_input(input)

        product = Product.objects.create(product=product_id,**cleaned_input)

        return ProductCreate(product=product)

        
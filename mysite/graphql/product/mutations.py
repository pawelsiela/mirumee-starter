from itertools import product
from typing_extensions import Required
import graphene

from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant

class ProductCreateInput(graphene.InputObjectType):
    name = graphene.String(Required=True)
    price = graphene.Decimal(Required=True)
    description = graphene.String(Required=True)
    quantity = graphene.Int()

class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)


class ProductVariantCreateInput(graphene.InputObjectType):
    product = graphene.String(Required=True)
    name = graphene.String(Required=True)
    sku = graphene.String(Required=True)
    price = graphene.Decimal(Required=True)

class ProductVariantCreate(graphene.Mutation):
    product_variant = graphene.Field(ProductType)

    class Agguments:
        input = ProductCreateInput(Required=True)
        input = ProductVariantCreateInput(Required=True)

    def clean_input(self, input):
        return input

    def mutate(self, root, info, input):
        cleaned_input = self.clean_input(input)

        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)
from itertools import product
from mysite.graphql.product.mutations import ProductCreate, ProductVariantCreate
import graphene
from graphene.types.objecttype import ObjectType

from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant



class ProductQueries(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.Argument(graphene.ID, description="ID of product."))

    products = graphene.List(ProductType)

    def resolve_product(self, _info, id):
        product = Product.objects.filter(id=id).first()
        return product
    
    def resolve_products(self, _info):
        return  Product.objects.all()

class ProductMutations(graphene.ObjectType):
    product_create = ProductCreate.Field()
    product_variant_create = ProductVariantCreate.Field()
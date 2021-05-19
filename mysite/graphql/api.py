import graphene

from ..graphql.product.schema import ProductMutations, ProductQueries

class Query(ProductQueries):
   pass


class Mutations(ProductMutations):
   pass


schema = graphene.Schema(query=Query, mutation=Mutations)
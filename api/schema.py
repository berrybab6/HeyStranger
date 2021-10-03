import graphene
from django.db.models import query
from graphene.types.objecttype import ObjectType
from graphene_django import DjangoObjectType
from .models import Users
from graphql_auth import mutations

from graphql_auth.schema import UserQuery, MeQuery


# class UserType(DjangoObjectType):
#     class Meta:
#         model = Users
#         fields = "__all__"
        #   (  'id',
        #     'password',
        #     'last_login',
        #     'is_superuser',
        #     'username',
        #     'first_name',
        #     'last_name',
        #     'is_staff',
        #     'is_active',
        #     'date_joined',
        #     'email',
        #     'profile_url',
        #     'groups',
        #     'user_permissions'
        # )        
            

# class Query(graphene.ObjectType):
#     users = graphene.List(UserType)
#     user = graphene.Field(UserType, user_id=graphene.Int())

#     def resolve_users(self, info, **kwargs):
#         return Users.objects.all()
#     def resolve_user(self, info, user_id):
#         return Users.objects.get(id=user_id)
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass
class Mutation(AuthMutation, graphene.ObjectType):
    pass    
schema = graphene.Schema(query=Query, mutation=Mutation)

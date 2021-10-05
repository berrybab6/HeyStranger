import graphene
from django.db.models import query
from graphene.types.objecttype import ObjectType
from graphene_django import DjangoObjectType
from .models import Secret, Users
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
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    password_change = mutations.PasswordChange.Field()



class SecretType(DjangoObjectType):
    class Meta:
        model = Secret
        fields = "__all__"

class Query(UserQuery, MeQuery, graphene.ObjectType):
    secrets = graphene.List(SecretType)
    secret = graphene.Field(SecretType, secret_id = graphene.Int())

    def resolve_secrets(self, info, **kwargs):
        return Secret.objects.all()
    def resolve_secret(self, info, secret_id):
        return Secret.objects.get(id=secret_id)
class SecretInputType(graphene.InputObjectType):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    postedOn = graphene.DateTime()
class CreateSecret(graphene.Mutation):  
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    postedOn = graphene.DateTime()
    class Arguments:
        title = graphene.String()
        description = graphene.String()
       
        postedOn = graphene.Date()
        # secret_data = SecretInputType(required=True)
    # secret = graphene.Field(SecretType)

    @staticmethod
    def mutate(self, info, title, description,user, postedOn,secret_data=None, ):
        user = Users.objects.get(id=1)
        secret_inistance = Secret(title=title,user=user, description=description, posted_on=postedOn)
        secret_inistance.save()
        return CreateSecret(id=secret_inistance.id,user=secret_inistance.user, title=secret_inistance.title, description=secret_inistance.description)
       
      

class Mutation(AuthMutation, graphene.ObjectType):
   create_secret = CreateSecret.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

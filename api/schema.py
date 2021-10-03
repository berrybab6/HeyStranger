import graphene
from graphene_django import DjangoObjectType
from .models import Users


class UserType(DjangoObjectType):
    class Meta:
        model = Users
        fields = (
            'id',
            'password',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
            'email',
            'profile_url',
            'groups',
            'user_permissions'
        )        
            

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(root, info, **kwargs):
        return Users.objects.all()
    
schema = graphene.Schema(query=Query)

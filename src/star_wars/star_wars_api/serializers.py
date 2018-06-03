from rest_framework import serializers
from models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    """Handles the serialization of the UserProfile class"""

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'email',
            'name',
            'password',
            'url',
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        """User creation method overwrite in order to hash the password"""

        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

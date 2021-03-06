from requests import request, HTTPError
from django.core.files.base import ContentFile
from hackathon.models import User_Profile
from settings import MEDIA_ROOT

def save_profile_picture(backend, user, response, details, is_new=False,
                         *args, **kwargs):
    # Save Facebook profile photo into a user profile, assuming a profile model
    # with a profile_photo file-type attribute
    if  backend.__class__.__name__ == 'FacebookOAuth2':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            fileName = 'avatar/{0}_social.jpg'.format(user.pk)
            saveName = MEDIA_ROOT + '{0}_social.jpg'.format(user.pk)
            localFile = open(saveName, 'w')
            localFile.write(response.content)
            localFile.close()
            user_profiles = User_Profile.objects.filter(user_id=user.pk)
            if user_profiles:
                user_profile = user_profiles[0]
                user_profile.avatar = fileName
                user_profile.save()
            else:
                User_Profile.objects.create(user=user, avatar=fileName)



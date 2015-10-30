from requests import request, HTTPError
from django.core.files.base import ContentFile
from hackathon.models import User_Profile

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
            saveName = 'LorR/avatar/{0}_social.jpg'.format(user.pk)
            localFile = open(saveName, 'w')
            localFile.write(response.content)
            localFile.close()

            user_profile = User_Profile.objects.get(id=user.pk)
            user_profile.avatar = fileName
            user_profile.save()

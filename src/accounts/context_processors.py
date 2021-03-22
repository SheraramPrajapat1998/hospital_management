from django.contrib.auth.models import Group

def hasGroup(user, groupName):
    """
    input: user and groupName
    return: True if user exists in any group else False
    """
    try:
        group = Group.objects.get(name=groupName)
        return True if group in user.groups.all() else False
    except:
        return False

# def 
from app.app_models.other_model import Album


def get_all_image():
    """
    Get all image object

    Args:
    """
    return Album.objects.all()


def create_image(name, img):
    """
    Create an image

    Args:
        name: (str): write your description
        img: (array): write your description
    """
    return Album.objects.create(name=name, img=img)


def get_image_by_id(id):
    """
    Get an image by id.

    Args:
        id: (str): write your description
    """
    try:
        return Album.objects.get(id=id)
    except:
        return None


def filter_image_by_start_name(name):
    """
    Filter image by name

    Args:
        name: (str): write your description
    """
    return Album.objects.filter(img__startswith=name)

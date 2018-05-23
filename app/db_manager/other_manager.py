from app.app_models.other_model import Album


def get_all_image():
    return Album.objects.all()


def create_image(name, img):
    return Album.objects.create(name=name, img=img)


def get_image_by_id(id):
    try:
        return Album.objects.get(id=id)
    except:
        return None


def filter_image_by_start_name(name):
    return Album.objects.filter(img__startswith=name)

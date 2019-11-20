from django.db.models import ImageField
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext as _
from django.forms.forms import ValidationError
from django.conf import settings

from imagekit.models import ProcessedImageField

class ValidateImageFile(ProcessedImageField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """

    def __init__(self, *args, **kwargs):
        self.content_types = settings.CONTENT_TYPES
        self.max_upload_size = settings.MAX_UPLOAD_SIZE

        super(ValidateImageFile, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ValidateImageFile, self).clean(*args, **kwargs)
        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise ValidationError(
                        _('Veuillez garder la taille du fichier sous {}. Taille de fichier actuelle {}'.format(
                            filesizeformat(self.max_upload_size), filesizeformat(file._size))))
            else:
                raise ValidationError(_('Type de fichier non supporté.'))
        except AttributeError:
            pass

        return data

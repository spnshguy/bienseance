from parler.forms import TranslatableModelForm

from apps.blogs.models import Blog, Tag


class BlogAdminForm(TranslatableModelForm):
    model = Blog
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].required = False


class TagAdminForm(TranslatableModelForm):
    model = Tag
    fields = 'translations__name', 'image'

    def __init__(self, *args, **kwargs):
        super(TagAdminForm, self).__init__(*args, **kwargs)

class ImageUtils:
    @classmethod
    def representation(self, value):
        return dict(
            pk=value.pk,
            url=value.file.url
        )

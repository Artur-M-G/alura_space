from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from photography_api.models import Photography
from photography_api.serializers import PhotographySerializer
from pathlib import Path

class SerializersTestCase(TestCase):
    def setUp(self):
        self.test_image_path = Path(__file__).resolve().parent / "media/test_image.jpg"
        self.photo = SimpleUploadedFile(name='test_image.jpg', content=open(self.test_image_path, 'rb').read(), content_type='image/jpeg')

        self.photography = Photography(
            name='O pálido ponto azul',
            subtitle='O astrônomo Carl Sagan descreveu a visão como um \"pálido ponto azul\"',
            description="""Sabe aquele pontinho azul no meio da foto? É a Terra. Esta é a primeira foto do 
            nosso Sistema Solar,divulgada em junho de 1990. A imagem faz parte de um mosaico de fotos 
            capturadas pela sonda Voyager 1,a 6 bilhões de quilômetros do planeta.""",
            category=4,
            photo=self.photo,
            date='2024-02-28 19:24:07',
            published = True,
        )

        self.serializer = PhotographySerializer(instance=self.photography)
        self.data = self.serializer.data
    
    def test_serializers_fields(self):
        self.assertEqual(set(self.data.keys()), set(['id', 'name', 'subtitle', 'description', 'category', 'photo', 'date', 'published']))
    
    def test_serializers_content(self):
        choices = Photography.CategoryChoices.choices
        def check_choices(choices, category_number, index=0):
            if index >= len(choices):
                return None
            if category_number == choices[index][0]:
                return choices[index][1]
            return check_choices(choices, category_number, index + 1)

        self.assertEqual(self.data['name'], self.photography.name)
        self.assertEqual(self.data['subtitle'], self.photography.subtitle)
        self.assertEqual(self.data['description'], self.photography.description)
        self.assertEqual(self.data['category'], check_choices(choices, self.photography.category))
        self.assertEqual(Path(self.data['photo']).name, self.photography.photo.name)
        self.assertEqual(self.data['published'], self.photography.published)

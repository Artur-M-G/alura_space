from django.test import TestCase
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile
from photography_api.models import Photography

class ModelsTestCase(TestCase):
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
        )

    def test_models(self):
        self.assertEqual(self.photography.name, 'O pálido ponto azul')
        self.assertEqual(self.photography.subtitle, 'O astrônomo Carl Sagan descreveu a visão como um \"pálido ponto azul\"')
        self.assertEqual(
            self.photography.description, 
            """Sabe aquele pontinho azul no meio da foto? É a Terra. Esta é a primeira foto do 
            nosso Sistema Solar,divulgada em junho de 1990. A imagem faz parte de um mosaico de fotos 
            capturadas pela sonda Voyager 1,a 6 bilhões de quilômetros do planeta."""
        )
        self.assertEqual(self.photography.category, 4)
        self.assertTrue(self.photography.photo, self.photo)
        self.assertEqual(self.photography.date, '2024-02-28 19:24:07')
        self.assertEqual(self.photography.published, True)

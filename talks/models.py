from pyexcel import get_sheet
from django.db import models


class Talk(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    speaker = models.CharField(max_length=200)
    url = models.URLField()
    number_of_views = models.PositiveIntegerField()
    transcript = models.TextField()

    def __str__(self):
        return self.name

    @classmethod
    def populate(cls):
        cls.objects.all().delete()

        url_to_talk_data = {}

        ted_sheet = get_sheet(
            file_name='ted_main.csv',
            name_columns_by_row=0
        )
        for name, description, speaker, url, number_of_views in zip(
            ted_sheet.column['name'],
            ted_sheet.column['description'],
            ted_sheet.column['main_speaker'],
            ted_sheet.column['url'],
            ted_sheet.column['views'],
        ):
            url = url.strip()
            url_to_talk_data[url] = {
                'name': name,
                'description': description,
                'speaker': speaker,
                'url': url,
                'number_of_views': number_of_views,
                'transcript': '',
            }

        transcripts_sheet = get_sheet(
            file_name='transcripts.csv',
            name_columns_by_row=0
        )
        for transcript, url in zip(
            transcripts_sheet.column['transcript'],
            transcripts_sheet.column['url'],
        ):
            url = url.strip()
            if url in url_to_talk_data:
                url_to_talk_data[url].update({
                    'transcript': transcript,
                })

        cls.objects.bulk_create([
            cls(
                name=talk_data['name'],
                description=talk_data['description'],
                speaker=talk_data['speaker'],
                url=talk_data['url'],
                number_of_views=talk_data['number_of_views'],
                transcript=talk_data['transcript'],
            )
            for talk_data in url_to_talk_data.values()
        ])

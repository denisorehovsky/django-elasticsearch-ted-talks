from django_elasticsearch_dsl import DocType, Index
from .models import Talk

talks = Index('talks')
talks.settings(number_of_shards=1, number_of_replicas=0)


@talks.doc_type
class TalkDocument(DocType):
    class Meta:
        model = Talk
        fields = (
            'name',
            'description',
            'speaker',
            'number_of_views',
            'transcript',
        )

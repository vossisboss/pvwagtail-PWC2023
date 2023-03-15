# Generated by Django 4.1.1 on 2022-10-13 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.models.collections


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0077_alter_revision_user"),
        ("custom_media", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.AddField(
            model_name="customimage",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="collection",
            field=models.ForeignKey(
                default=wagtail.models.collections.get_root_collection_id,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.collection",
                verbose_name="collection",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text=None,
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="customdocument",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="customrendition",
            unique_together={("image", "filter_spec", "focal_point_key")},
        ),
    ]

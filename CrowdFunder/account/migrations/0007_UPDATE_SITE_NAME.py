from django.db import migrations
from django.conf import settings


def update_site_name(apps, schema_editor):
    SiteModel = apps.get_model('sites', 'Site')
    domain = '127.0.0.1:8000'

    SiteModel.objects.update_or_create(
        pk=settings.SITE_ID,
        defaults={'domain': domain,
                  'name': domain}
    )


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_birthdate_user_country_user_profile'),
        ('sites', '0002_alter_domain_unique'), # Required to reference `sites` in `apps.get_model()`
    ]

    operations = [
        migrations.RunPython(update_site_name),
    ]

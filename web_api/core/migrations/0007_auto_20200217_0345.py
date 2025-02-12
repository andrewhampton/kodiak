# Generated by Django 3.0.3 on 2020-02-17 03:45

import uuid

from django.contrib.postgres.operations import CreateExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_account_payload"),
    ]

    operations = [
        CreateExtension("uuid-ossp"),
        migrations.CreateModel(
            name="PullRequestActivity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(db_index=True)),
                ("total_opened", models.IntegerField()),
                ("total_merged", models.IntegerField()),
                ("total_closed", models.IntegerField()),
                ("kodiak_approved", models.IntegerField()),
                ("kodiak_merged", models.IntegerField()),
                ("kodiak_updated", models.IntegerField()),
                ("github_installation_id", models.IntegerField(db_index=True)),
            ],
            options={"db_table": "pull_request_activity",},
        ),
        migrations.AddConstraint(
            model_name="pullrequestactivity",
            constraint=models.UniqueConstraint(
                fields=("date", "github_installation_id"),
                name="unique_pull_request_activity",
            ),
        ),
    ]

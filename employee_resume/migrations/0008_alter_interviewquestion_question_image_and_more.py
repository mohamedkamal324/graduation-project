# Generated by Django 5.0.4 on 2024-05-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_resume", "0007_job_job_preferred_qualifications_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interviewquestion",
            name="question_image",
            field=models.FileField(
                blank=True, null=True, upload_to="interviewer/images"
            ),
        ),
        migrations.AlterField(
            model_name="interviewquestion",
            name="question_image_des",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="interviewquestion",
            name="question_text_des",
            field=models.TextField(blank=True, null=True),
        ),
    ]

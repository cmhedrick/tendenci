# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tendenci.apps.base.fields
import django.db.models.deletion
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('renewal', models.BooleanField(default=False)),
                ('renew_dt', models.DateTimeField(null=True, verbose_name='Renew Date Time')),
                ('join_dt', models.DateTimeField(verbose_name='Join Date Time')),
                ('expiration_dt', models.DateTimeField(null=True, verbose_name='Expiration Date Time', blank=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('approved_denied_dt', models.DateTimeField(null=True, verbose_name='Approved or Denied Date Time')),
                ('admin_notes', models.TextField(null=True, verbose_name='Admin notes', blank=True)),
                ('total_passes_allowed', models.PositiveIntegerField(default=0, verbose_name='Total Passes Allowed', blank=True)),
            ],
            options={
                'verbose_name': 'Corporate Member',
                'verbose_name_plural': 'Corporate Members',
                'permissions': (('view_corpmembership', 'Can view corporate membership'),),
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=155, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=155, verbose_name='URL Path')),
                ('authentication_method', models.CharField(default=b'admin', help_text='Define a method for individuals to be bound to their corporate memberships when signing up.', max_length=50, verbose_name='Authentication Method', choices=[(b'admin', 'Admin Approval'), (b'email', 'E-mail Domain'), (b'secret_code', 'Secret Code')])),
                ('description', tinymce.models.HTMLField(help_text='Will display at the top of the application form.', null=True, verbose_name='Description', blank=True)),
                ('notes', models.TextField(help_text='Notes for editor. Will not display on the application form.', null=True, verbose_name='Notes', blank=True)),
                ('confirmation_text', models.TextField(null=True, verbose_name='Confirmation Text', blank=True)),
                ('include_tax', models.BooleanField(default=False)),
                ('tax_rate', models.DecimalField(default=0, help_text='Example: 0.0825 for 8.25%.', max_digits=5, decimal_places=4, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Corporate Membership Application',
                'verbose_name_plural': 'Corporate Membership Applications',
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipAppField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=0, null=True, verbose_name='Position', blank=True)),
                ('label', models.CharField(max_length=2000, verbose_name='Label')),
                ('field_name', models.CharField(default=b'', max_length=30, verbose_name='Field Name', blank=True)),
                ('field_type', models.CharField(default=b'CharField', choices=[(b'CharField', 'Text'), (b'CharField/django.forms.Textarea', 'Paragraph Text'), (b'BooleanField', 'Checkbox'), (b'ChoiceField', 'Select One from a list (Drop Down)'), (b'ChoiceField/django.forms.RadioSelect', 'Select One from a list (Radio Buttons)'), (b'MultipleChoiceField', 'Multi select (Drop Down)'), (b'MultipleChoiceField/django.forms.CheckboxSelectMultiple', 'Multi select (Checkboxes)'), (b'CountrySelectField', 'Countries Drop Down'), (b'EmailField', 'Email'), (b'FileField', 'File upload'), (b'DateField/django.forms.extras.SelectDateWidget', 'Date'), (b'DateTimeField', 'Date/time'), (b'section_break', 'Section Break')], max_length=80, blank=True, null=True, verbose_name='Field Type')),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('display', models.BooleanField(default=True, verbose_name='Show')),
                ('admin_only', models.BooleanField(default=False, verbose_name='Admin Only')),
                ('help_text', models.CharField(default=b'', max_length=2000, verbose_name='Help Text', blank=True)),
                ('choices', models.CharField(help_text='Comma separated options where applicable', max_length=1000, null=True, verbose_name='Choices', blank=True)),
                ('field_layout', models.CharField(default=b'1', choices=[(b'1', 'One Column'), (b'2', 'Two Columns'), (b'3', 'Three Columns'), (b'0', 'Side by Side')], max_length=50, blank=True, null=True, verbose_name='Choice Field Layout')),
                ('size', models.CharField(default=b'm', choices=[(b's', 'Small'), (b'm', 'Medium'), (b'l', 'Large')], max_length=1, blank=True, null=True, verbose_name='Field Size')),
                ('default_value', models.CharField(default=b'', max_length=100, verbose_name='Default Value', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=50, verbose_name='CSS Class Name', blank=True)),
                ('description', models.TextField(default=b'', max_length=200, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('position',),
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='CorpMembershipAuthDomain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_file', models.FileField(upload_to=b'imports/corpmemberships/3a5df3a8', max_length=260, verbose_name='Upload File')),
                ('override', models.IntegerField(default=0, choices=[(0, 'Blank Fields'), (1, 'All Fields (override)')])),
                ('key', models.CharField(default=b'name', max_length=50, verbose_name='Key')),
                ('bind_members', models.BooleanField(default=False, verbose_name='Bind members to corporations by their company names')),
                ('total_rows', models.IntegerField(default=0)),
                ('num_processed', models.IntegerField(default=0)),
                ('summary', models.CharField(default=b'', max_length=500, null=True, verbose_name='Summary')),
                ('status', models.CharField(default=b'not_started', max_length=50, choices=[(b'not_started', 'Not Started'), (b'preprocessing', 'Pre_processing'), (b'preprocess_done', 'Pre_process Done'), (b'processing', 'Processing'), (b'completed', 'Completed')])),
                ('complete_dt', models.DateTimeField(null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipImportData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row_data', tendenci.apps.base.fields.DictField(verbose_name='Row Data')),
                ('row_num', models.IntegerField(verbose_name='Row #')),
                ('action_taken', models.CharField(max_length=20, null=True, verbose_name='Action Taken')),
            ],
        ),
        migrations.CreateModel(
            name='CorpMembershipRep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_dues_rep', models.BooleanField(default=True, verbose_name='is dues rep?')),
                ('is_member_rep', models.BooleanField(default=True, verbose_name='is member rep?')),
            ],
        ),
        migrations.CreateModel(
            name='CorporateMembershipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
                ('position', models.IntegerField(default=0, null=True, verbose_name='Position', blank=True)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', verbose_name='Price')),
                ('renewal_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', null=True, verbose_name='Renewal Price')),
                ('admin_only', models.BooleanField(default=False, verbose_name='Admin Only')),
                ('apply_threshold', models.BooleanField(default=False, verbose_name='Allow Threshold')),
                ('individual_threshold', models.IntegerField(default=0, null=True, verbose_name='Threshold Limit', blank=True)),
                ('individual_threshold_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='All individual members applying under or equal to the threshold limit\nreceive the threshold prices. Additional employees can join but will be\ncharged the full individual corporate membership rate.\n', null=True, verbose_name='Threshold Price')),
                ('number_passes', models.PositiveIntegerField(default=0, verbose_name='Number Passes', blank=True)),
            ],
            options={
                'ordering': ('position',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CorpProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
                ('guid', models.CharField(max_length=50)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('address', models.CharField(default=b'', max_length=150, verbose_name='Address', blank=True)),
                ('address2', models.CharField(default=b'', max_length=100, verbose_name='Address2', blank=True)),
                ('city', models.CharField(default=b'', max_length=50, verbose_name='City', blank=True)),
                ('state', models.CharField(default=b'', max_length=50, verbose_name='State', blank=True)),
                ('zip', models.CharField(default=b'', max_length=50, verbose_name='Zipcode', blank=True)),
                ('country', models.CharField(default=b'', max_length=50, verbose_name='Country', blank=True)),
                ('phone', models.CharField(default=b'', max_length=50, verbose_name='Phone', blank=True)),
                ('email', models.CharField(default=b'', max_length=200, verbose_name='Email', blank=True)),
                ('url', models.CharField(default=b'', max_length=100, verbose_name='URL', blank=True)),
                ('secret_code', models.CharField(default=b'', max_length=50, blank=True)),
                ('number_employees', models.IntegerField(default=0)),
                ('chapter', models.CharField(default=b'', max_length=150, verbose_name='Chapter', blank=True)),
                ('tax_exempt', models.BooleanField(default=False, verbose_name='Tax exempt')),
                ('annual_revenue', models.CharField(default=b'', max_length=75, verbose_name='Annual revenue', blank=True)),
                ('annual_ad_expenditure', models.CharField(default=b'', max_length=75, blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('expectations', models.TextField(default=b'', blank=True)),
                ('notes', models.TextField(default=b'', verbose_name='Notes', blank=True)),
                ('referral_source', models.CharField(default=b'', max_length=150, blank=True)),
                ('referral_source_other', models.CharField(default=b'', max_length=150, blank=True)),
                ('referral_source_member_name', models.CharField(default=b'', max_length=50, blank=True)),
                ('referral_source_member_number', models.CharField(default=b'', max_length=50, blank=True)),
                ('ud1', models.TextField(default=b'', null=True, blank=True)),
                ('ud2', models.TextField(default=b'', null=True, blank=True)),
                ('ud3', models.TextField(default=b'', null=True, blank=True)),
                ('ud4', models.TextField(default=b'', null=True, blank=True)),
                ('ud5', models.TextField(default=b'', null=True, blank=True)),
                ('ud6', models.TextField(default=b'', null=True, blank=True)),
                ('ud7', models.TextField(default=b'', null=True, blank=True)),
                ('ud8', models.TextField(default=b'', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='Contact first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Contact last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Contact e-mail address')),
                ('hash', models.CharField(default=b'', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='FreePassesStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndivEmailVerification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50)),
                ('verified_email', models.CharField(max_length=200, verbose_name='email')),
                ('verified', models.BooleanField(default=False)),
                ('verified_dt', models.DateTimeField(null=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndivMembershipRenewEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_detail', models.CharField(default=b'pending', max_length=50, choices=[(b'pending', 'Pending'), (b'approved', 'Approved'), (b'disapproved', 'Disapproved')])),
                ('corp_membership', models.ForeignKey(to='corporate_memberships.CorpMembership')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('notice_name', models.CharField(max_length=250, verbose_name='Name')),
                ('num_days', models.IntegerField(default=0)),
                ('notice_time', models.CharField(max_length=20, verbose_name='Notice Time', choices=[(b'before', 'Before'), (b'after', 'After'), (b'attimeof', 'At Time Of')])),
                ('notice_type', models.CharField(max_length=20, verbose_name='For Notice Type', choices=[(b'approve_join', 'Approval Date'), (b'disapprove_join', 'Disapproval Date'), (b'approve_renewal', 'Renewal Approval Date'), (b'disapprove_renewal', 'Renewal Disapproval Date'), (b'expiration', 'Expiration Date')])),
                ('system_generated', models.BooleanField(default=False, verbose_name='System Generated')),
                ('subject', models.CharField(max_length=255)),
                ('content_type', models.CharField(default=b'html', max_length=10, verbose_name='Content Type', choices=[(b'html', b'HTML')])),
                ('sender', models.EmailField(max_length=255, null=True, blank=True)),
                ('sender_display', models.CharField(max_length=255, null=True, blank=True)),
                ('email_content', tinymce.models.HTMLField(verbose_name='Email Content')),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('creator_username', models.CharField(max_length=50, null=True)),
                ('owner_username', models.CharField(max_length=50, null=True)),
                ('status_detail', models.CharField(default=b'active', max_length=50, choices=[(b'active', 'Active'), (b'admin_hold', 'Admin Hold')])),
                ('status', models.BooleanField(default=True)),
                ('corporate_membership_type', models.ForeignKey(blank=True, to='corporate_memberships.CorporateMembershipType', help_text="Note that if you             don't select a corporate membership type,             the notice will go out to all members.", null=True)),
                ('creator', models.ForeignKey(related_name='corporate_membership_notice_creator', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='corporate_membership_notice_owner', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('notice_sent_dt', models.DateTimeField(auto_now_add=True)),
                ('num_sent', models.IntegerField()),
                ('notice', models.ForeignKey(related_name='logs', to='corporate_memberships.Notice')),
            ],
        ),
        migrations.CreateModel(
            name='NoticeLogRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(max_length=50, editable=False)),
                ('action_taken', models.BooleanField(default=False)),
                ('action_taken_dt', models.DateTimeField(null=True, blank=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('corp_membership', models.ForeignKey(related_name='log_records', to='corporate_memberships.CorpMembership')),
                ('notice_log', models.ForeignKey(related_name='log_records', to='corporate_memberships.NoticeLog')),
            ],
        ),
    ]
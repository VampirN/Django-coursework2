from django.contrib import admin

from mailing_service.models import Message, Client, Mailing, MailingAttempt


#admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject_of_letter', 'body_of_letter', 'creator')
    list_filter = ('subject_of_letter',)
    search_fields = ('subject_of_letter', 'creator')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('frequency', 'status',)
    list_filter = ('status', 'frequency',)
    search_fields = ('status', 'frequency',)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ('date_and_time','mailing', 'attempt_status')
    list_filter = ('date_and_time','attempt_status')
    search_fields = ('date_and_time','attempt_status')


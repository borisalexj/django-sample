from django.views.generic.edit import FormView

from students.views import ContactForm, send_mail


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/email-sent/'

    def from_valid(self, form):
        """ This method is called for valid data """
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, ['bo-a@yandex.ru'])

        return super(ContactView, self).form_valid(form)

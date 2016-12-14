from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Invoice, Product, Partner, InvoiceLine

InvoiceLineFormSet = inlineformset_factory(
    Invoice, InvoiceLine, can_delete=True, fields=[
        'product_id', 'quantity', 'description'], exclude=[
        'created_at'
    ])



class InvoiceForm(ModelForm):
    created_at = forms.DateTimeField()

    class Meta:
        model = Invoice
        fields = ['number', 'partner_id', 'comment', 'currency_id']

class PartnerForm(ModelForm):
    created_at = forms.DateTimeField()

    class Meta:
        model = Partner
        fields = ['name', 'vat_payer', 'vat_number', 'reg_number']


# def post_form_upload(request):
#     if request.method == 'GET':
#         form = ModelForm()
#     else:
#         # A POST request: Handle Form Upload
#         form = PostForm(
#             request.POST)  # Bind data from request.POST into a PostForm
#
#         # If data is valid, proceeds to create a new post and redirect the user
#         if form.is_valid():
#             content = form.cleaned_data['content']
#             created_at = form.cleaned_data['created_at']
#             post = m.Post.objects.create(content=content,
#                                          created_at=created_at)
#             return HttpResponseRedirect(reverse('post_detail',
#                                                 kwargs={'post_id': post.id}))
#
#     return render(request, 'post/post_form_upload.html', {
#         'form': form,
#     })
from django.contrib.auth.views import LogoutView, LoginView
from .forms import CustomUserCreationForm,  AddressFormSet
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('pastas:index')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['address_formset'] = AddressFormSet(self.request.POST, prefix='address')
        else:
            data['address_formset'] = AddressFormSet(prefix='address')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address_formset = context['address_formset']
        self.object = form.save()
        if address_formset.is_valid():
            for form in address_formset:
                address = form.save(commit=False)
                address.user = self.object # Asegúrate de asignar el usuario correctamente
                address.save()
        return super().form_valid(form)



class Logout(LogoutView):
    next_page = 'pastas:index'




class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('pastas:index')
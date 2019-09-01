from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ReservationForm

class ReservationPageView(View):
    form_class      = ReservationForm
    template_name   = "reservation/reservation_form.html"

    def get(self, request):
        """
        """
        return render(request, self.template_name, {"form":self.form_class()})

    def post(self, request):
        """
        """
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent = bound_form.send_mail()
            if mail_sent:
                # shortcut for add_message 
                success(request, "Email successfully send!")
                return redirect("")
        return render(request, self.template_name, {"form":bound_form})



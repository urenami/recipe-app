from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = '/accounts/login/'  # where to redirect after logout

    # Override to allow GET requests
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

from django.contrib import admin
from .models import AdminAccount, WalkinBooking, AdminReportLogs

# Register your models here.
admin.site.register(AdminAccount)
admin.site.register(WalkinBooking)
admin.site.register(AdminReportLogs)
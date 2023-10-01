from django.contrib import admin
from .models import AdminAccountModel, WalkinBookingModel, AdminReportLogsModel

# Register your models here.
admin.site.register(AdminAccountModel)
admin.site.register(WalkinBookingModel)
admin.site.register(AdminReportLogsModel)
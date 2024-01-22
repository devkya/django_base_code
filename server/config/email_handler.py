from django.utils.log import AdminEmailHandler
from django.template.loader import render_to_string


class CustomAdminEmailHandler(AdminEmailHandler):
    def emit(self, record):
        try:
            subject = f"{record.levelname} ERROR occurred in {record.name}"
            view_name = getattr(record, "view_name", None)
            message = record.getMessage()
            context = {
                "message": message,
                "view_name": view_name,
            }
            html_message = render_to_string("email_template.html", context)
            self.send_mail(
                subject=subject,
                message=message,
                html_message=html_message,
                fail_silently=True,
            )

        except Exception as e:
            print(">>>>> error:", e)
            self.handleError(record)

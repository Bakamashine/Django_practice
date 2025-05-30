from main.models import Forms

def header_data(req):
    return {
        "document_forms": Forms.objects.all()
    }
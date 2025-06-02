from main.models import Forms
from datetime import datetime

def header_data(req):
    today_year = datetime.now().year
    years = [n for n in range(1995, today_year+1)]
    return {
        "document_forms": Forms.objects.all(),
        "today_year": today_year,
        "years": years
    }
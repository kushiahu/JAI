from django.contrib import admin
from factura.models import *
# Register your models here.
admin.site.register(Emisor)
admin.site.register(Receptor)
admin.site.register(Documento)
admin.site.register(Servicio)
admin.site.register(Sucursal)
admin.site.register(Folio)
admin.site.register(Factura)
admin.site.register(Ticket)




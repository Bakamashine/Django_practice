from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from products.models import Product, Category
import aspose.threed as a3d
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from io import BytesIO
import tempfile

admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Product)
class AdminProducts(admin.ModelAdmin):
    model = Product

    # def save_model(self, file):
    #     filename = file.name.lower()
    #     name, ext = os.path.splitext(filename)
        

    #     if ext == ".stl":
    #         scene = a3d.Scene.from_file(file)
    #         saved_name = f"{name}.glb"
    #         saved_path = default_storage.save(f"products/{saved_name}", file)
    #         scene.save(saved_path)
    #     elif ext == ".glb":
    #         saved_path = default_storage.save(f"products/{filename}", file)

    def save_model(self, request: HttpRequest, obj, form: ModelForm, change: bool) -> None:
        super().save_model(request, obj, form, change)
        if 'file' in request.FILES:
            file = request.FILES['file']
            saved_path = self.upload_file(file)
            obj.file_path = saved_path  
            obj.save() 
        
    def upload_file(self, file) -> (str|None):
        name, ext = os.path.splitext(file.name.lower())
        ext = ext.lstrip(".")

        tmp_input_file_path = tempfile.mktemp(suffix = f'.{ext}')
        with open(tmp_input_file_path, 'wb') as tmp_input_file:
            for chunk in file.chunks():
                tmp_input_file.write(chunk)
        
        if ext == 'stl':
            scene = a3d.Scene.from_file(tmp_input_file_path)

            tmp_output_file_path = tempfile.mktemp(suffix=".glb")
            scene.save(tmp_output_file_path)

            with open (tmp_output_file_path, 'rb') as tmp_output_file:
                glb_data = tmp_output_file.read()

            saved_name = f'products/models/{name}.glb'
            saved_path = default_storage.save(saved_name, ContentFile(glb_data))

            os.remove(tmp_input_file_path)
            os.remove(tmp_output_file_path)

            return saved_path
        elif ext == "glb":
            saved_name = f"product/models/{file.name}"
            saved_path = default_storage.save(saved_name, file)
            return saved_path
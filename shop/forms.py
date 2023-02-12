from django import forms

from utilities.utils import send_sms

from .models import Shop


class ShopChangeForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"

    def save(self, commit=True):
        data = super().save(commit=False)
        if "is_active" in self.changed_data:
            if self.data.get("is_active") == "on":
                text = f"{data.first_name + data.last_name} عزیز\n فروشگاه: {data.name} تایید شد.\nجهت ثبت محصول از طریق پنل فروشگاه خود اقدام فرمایید.\nپلاست‌اپ\nplastapp.ir"
                try:
                    send_sms(phone=data.user, message=text)
                except Exception as e:
                    raise e
        if commit:
            data.save()
        return data

from django import forms
from django.contrib import admin
from .models import Machine, BottleSlot, MachineIssue, Ingredient

class BottleSlotInlineForm(forms.ModelForm):
    class Meta:
        model = BottleSlot
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'position' in self.fields:
            self.fields['position'].widget.attrs['readonly'] = True
        self.fields['ingredient'].queryset = Ingredient.objects.all()

class BottleSlotInline(admin.TabularInline):
    model = BottleSlot
    form = BottleSlotInlineForm
    extra = 0
    max_num = 0
    can_delete = False
    readonly_fields = ('position', 'last_refilled')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'store', 'slots')
    inlines = [BottleSlotInline]

@admin.register(MachineIssue)
class MachineIssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'machine', 'severity', 'is_resolved', 'created_at', 'resolved_at')
    list_filter = ('severity', 'is_resolved', 'machine')
    search_fields = ('title', 'description', 'machine__serial_number')

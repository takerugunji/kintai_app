from django import forms
from .models import SubmitAttendance # models.pyからclassを読み込む

# 最初のページで出勤場所と出退勤打刻を表示させる
class SubmitAttendanceForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['in_out'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = SubmitAttendance
        fields = ('place', 'in_out')
        
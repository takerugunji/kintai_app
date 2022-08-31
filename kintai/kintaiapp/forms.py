from django import forms
from .models import SubmitAttendance # models.pyからclassを読み込む

# 最初のページで出勤場所と出退勤打刻を表示させる
class SubmitAttendanceForm(forms.ModelForm):

    class Meta:
        model = SubmitAttendance
        fields = ('place', 'in_out')
        
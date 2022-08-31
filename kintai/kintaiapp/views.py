import calendar
from tkinter.tix import Form
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubmitAttendance
from .forms import SubmitAttendanceForm
from datetime import date, datetime, timedelta

# index用ビュー
class IndexView(LoginRequiredMixin, View): # LoginRequiredMixinでログインしていないと特定のページに遷移

    def get(self, request):
        form = SubmitAttendanceForm
        context = {
            'form': form,
            'user': request.user,
        }
        return render(request, 'kintaiapp/index.html', context)

index = IndexView.as_view()

# result用ビュー
class ResultView(View):

    def post(self, request):
        form = SubmitAttendanceForm(request.POST)
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        obj = form.save(commit=False)
        obj.place = request.POST["place"]
        obj.in_out = request.POST["in_out"]
        obj.staff = request.user
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        obj.save()
        if request.POST["in_out"] == '1':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
        elif request.POST["in_out"] == '2':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした(^-^)！"
        elif request.POST["in_out"] == '3':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "休憩に入りました。"
        elif request.POST["in_out"] == '4':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "休憩から戻りました。"
                
        context = {
            'place': SubmitAttendance.PLACES[int(obj.place)-1][1],
            'comment': comment,
        }
        return render(request, 'kintaiapp/result.html', context)    
result = ResultView.as_view()

class AttendanceListView(LoginRequiredMixin, View):
    '''DBから勤怠登録情報を取得して一覧表示する'''
    def get(self, request):
        now = datetime.now()
        year = now.year
        month = now.month

        '''タイトル月表示'''
        kintaibo_date_month = str(month)
        
        '''当月範囲計算'''
        kintaibo_date_end = date(year, month, calendar.monthrange(year, month)[1]) # 月末日付取得
        date_list = [date(year, month, 1) + timedelta(days=i) for i in range(0, kintaibo_date_end.day)]

        '''勤務場所取得'''
        kintaibo_place = SubmitAttendance.objects.filter(staff=request.user).order_by('place').first() #出勤場所が複数ある場合は変更

        '''打刻時間取得'''
        kintaibo_in_time = SubmitAttendance.objects.filter(in_out=1, staff=request.user).order_by('date', 'time') # 保留
        kintaibo_out_time = SubmitAttendance.objects.filter(in_out=2, staff=request.user).order_by('date', 'time')
        kintaibo_rest_in_time = SubmitAttendance.objects.filter(in_out=3, staff=request.user).order_by('date', 'time')
        kintaibo_rest_out_time = SubmitAttendance.objects.filter(in_out=4, staff=request.user).order_by('date', 'time')
        
        params = {
            'kintaibo_date_month': kintaibo_date_month,
            'date_list': date_list,
            'kintaibo_place': kintaibo_place,
            'kintaibo_in_time': kintaibo_in_time,
            'kintaibo_out_time': kintaibo_out_time,
            'kintaibo_rest_in_time': kintaibo_rest_in_time,
            'kintaibo_rest_out_time': kintaibo_rest_out_time,
        }
        return render(request, 'kintaiapp/attendance_list.html', params)

list = AttendanceListView.as_view()
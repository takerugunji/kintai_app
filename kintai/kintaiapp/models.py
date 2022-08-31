from django.db import models
from django.contrib.auth import get_user_model # カスタムユーザーモデルを使用する

class SubmitAttendance(models.Model): # models.Modelを継承したクラスを定義

    class Meta:
        db_table = 'attendance' # データベースに格納された時のメタデータとしてテーブル名を与える      
        '''重複打刻回避'''
        constraints = [
            models.UniqueConstraint(
                fields=["staff", "in_out", "date"],
                name="kintai_unique",
            ),
        ]

    PLACES = (
        (1, 'NES Tokyo'),
        (2, 'Dest A'),
        (3, 'Dest B'),
        (4, 'Dest C'),
    )
    IN_OUT = (
        (1, '出勤'),
        (2, '退勤'),
        (3, '休憩入り'),
        (4, '休憩戻り'),
    )

    # staff:ログイン中のユーザー名
    # place:PLACESタプルから選ぶ
    # in_out:IN_OUTタプルから選ぶ
    # time:打刻した時間
    # date:打刻した日付
    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')
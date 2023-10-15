import logging
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm
import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo
import pytz
import calendar
from calendar import Calendar, HTMLCalendar
from .models import Lesson


jst = pytz.timezone('Asia/Tokyo')
cst = pytz.timezone('Asia/Shanghai')
utc = pytz.timezone('Etc/UTC')

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dt_now = datetime.datetime.now().astimezone(jst)
        year = dt_now.year
        month = dt_now.month
        my_date = dt_now.day
        month_number = dt_now.month + 1
        cal = Calendar(firstweekday=0).monthdatescalendar(year, month)
        cal_html = HTMLCalendar(firstweekday=0).formatmonth(year, month)
        cal_year_html = HTMLCalendar(firstweekday=0).formatyear(year)
        week = []
        my_time = []
        just_my_time = []
        base_time = datetime.datetime(year, month, my_date)
        for i in range(7):
            theday = dt_now + datetime.timedelta(days=i)
            week.append(theday)

        for i in range(48):
            thetime = base_time + datetime.timedelta(minutes=i%2*30, hours=i//2)
            my_time.append(thetime)

        for item in my_time:
            tmp = []
            for item2 in week:
                daytime = datetime.datetime(year=int(item2.strftime('%Y')),
                                             month=int(item2.strftime('%m')),
                                             day=int(item2.strftime('%d')),
                                             hour=int(item.strftime('%H')),
                                             minute=int(item.strftime('%M'))).astimezone(jst)
                daytime2 = daytime + datetime.timedelta(minutes=30)
                if daytime <= dt_now and daytime2 > dt_now:
                    i_class = 'bg-primary text-light'
                elif daytime2 <= dt_now:
                    i_class = 'bg-secondary text-dark'
                else:
                    i_class = ''
                lessons = Lesson.objects.filter(time__gte=daytime, time__lt=daytime2)

                tmp.append({'i_day': item2.strftime('%Y/%m/%d'), 'i_time': item.strftime('%H:%M'), 'i_daytime': daytime, 'i_class': i_class, 'i_lessons': lessons})
            just_my_time.append(tmp)
        ## all_lessons = Lesson.objects.filter(student=self.request.user)
        all_lessons = Lesson.objects.all()


        '''
        for day in week:
            print(day.strftime('%Y/%m/%d (%a)'))
        for time in my_time:
            print(time.strftime('%H:%M'))
        '''

        context['CST_ex'] = datetime.datetime(2023, 10, 7, 12, 0, 0, 0, tzinfo=ZoneInfo('Asia/Shanghai'))

        context['dbg_1'] = datetime.datetime(2023, 10, 10, 12, 0, 0, 0, tzinfo=ZoneInfo('Asia/Tokyo'))

        context['general_date'] = dt_now
        context['cal'] = cal
        context['cal_html'] = cal_html
        context['cal_year_html'] = cal_year_html
        context['week'] = week
        context['my_time'] = my_time
        context['just_my_time'] = just_my_time
        context['all_lessons'] = all_lessons
        return context


class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('app1:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Message was sent.')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


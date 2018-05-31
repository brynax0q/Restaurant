from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import JsonResponse

from demo.models import Table, WalkIn, Reservation, Customer

from datetime import datetime

date_ = {
    "18:00": "0",
    "18:30": "1",
    "19:00": "2",
    "19:30": "3",
    "20:00": "4",
    "20:30": "5",
    "21:00": "6",
    "21:30": "7",
    "22:00": "8",
    "22:30": "9",
    "23:00": "10",
    "23:30": "11"
}
time_ = {
    "0.5": "1",
    "1": "2",
    "1.5": "3",
    "2": "4",
    "2.5": "5",
    "3": "6",
    "3.5": "7",
    "4": "8"
}

class IndexView(View):
    def get(self, request):
        tables = Table.objects.all()

        time = request.GET.get("date", datetime.now().strftime('%Y-%m-%d'))
        reservations = Reservation.objects.filter(day=time)
        set_list = [
            [0] * 22,
            [0] * 22,
            [0] * 22,
            [0] * 22,
            [0] * 22,
            [0] * 22,
        ]
        for item in reservations:
            index = 2 * int(item.date) + 1
            long = int(item.time) * 2
            table_id = int(item.table.id)
            i = 0
            while long > 0:
                set_list[table_id - 1][index + i] = 1
                i += 1
                long -= 1

        walk_in = WalkIn.objects.filter(day=time)
        for item in walk_in:
            index = 2 * int(item.date) + 1
            long = int(item.time) * 2
            table_id = int(item.table.id)
            i = 0
            while long > 0:
                set_list[table_id - 1][index + i] = 1
                i += 1
                long -= 1

        return render(request, "index.html", {
            "tables": tables,
            "set_list": set_list,
            "reservations": reservations,
            "time": time
        })

    def post(self, request):
        time = request.POST.get("date", "")
        response = {}
        response['date'] = str(time)
        response['status'] = 'success'
        return JsonResponse(response)


# 预定
class ReservationView(View):
    def post(self, request):
        response = {}
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        num = request.POST.get("num", "")
        day = request.POST.get("day", "")
        date = request.POST.get("arrival", "")
        time = request.POST.get("time", "")
        table = request.POST.get("table", "")

        if name == "":
            response["status"] = 0
            response["msg"] = "出错"
            return JsonResponse(response)

        customer = Customer.objects.filter(name=name)
        if not customer.exists():
            customer = Customer()
            customer.name = name
            customer.phone = phone
            customer.save()

        else:
            customer = Customer.objects.get(name=name)

        table = Table.objects.get(id=int(table))
        reservation = Reservation()
        reservation.name = customer
        reservation.people_num = num
        reservation.day = day
        reservation.table = table
        reservation.date = date_[date]
        reservation.time = time_[time]
        reservation.save()

        response["status"] = 1
        response["msg"] = "预约成功"
        response["day"] = day

        return JsonResponse(response)


# 取消预约
class CancelReservationView(View):
    def post(self, request):
        response = {}
        name = request.POST.get("name", "")
        day = request.POST.get("day", "")
        if name == "":
            response['status'] = 0
            response['msg'] = '出错'
            return JsonResponse(response)
        customer = Customer.objects.filter(name=name)

        reservation = Reservation.objects.filter(name=customer, day=day)

        if reservation:
            reservation.delete()
            response['status'] = 1
            response['msg'] = "取消成功"
            response['day'] = day
        else:
            response['status'] = 2
            response['msg'] = "预约不存在"
        return JsonResponse(response)


# 换桌
class ChangeTableView(View):
    def post(self, request):
        response = {}
        name = request.POST.get("name", "")
        day = request.POST.get("day", "")
        new_table = request.POST.get("new_table", "")

        customer = Customer.objects.filter(name=name)
        reservation = Reservation.objects.filter(name=customer, day=day)

        if reservation:
            reservation = Reservation.objects.get(name=customer, day=day)
            new_table = Table.objects.get(id=new_table)
            reservation.table = new_table
            reservation.save()
            response['status'] = 1
            response['msg'] = "换桌成功"
            response['day'] = day
        else:
            response['status'] = 2
            response['msg'] = "失败"
        return JsonResponse(response)


# 就餐
class WalkInView(View):
    def post(self, request):
        response = {}
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        num = request.POST.get("num", "")
        day = datetime.now().strftime('%Y-%m-%d')
        date = request.POST.get("arrival", "")
        time = request.POST.get("time", "")
        table = request.POST.get("table", "")

        if name == "":
            response["status"] = 0
            response["msg"] = "出错"
            return JsonResponse(response)

        customer = Customer.objects.filter(name=name)
        if not customer.exists():
            customer = Customer()
            customer.name = name
            customer.phone = phone
            customer.save()

        else:
            customer = Customer.objects.get(name=name)

        walk_in = WalkIn()
        walk_in.name = customer
        walk_in.people_num = num
        walk_in.day = day
        table = Table.objects.get(id=int(table))
        walk_in.table = table
        walk_in.date = date_[date]
        walk_in.time = time_[time]
        walk_in.save()

        response["status"] = 1
        response["msg"] = "就餐成功"
        response["day"] = day
        return JsonResponse(response)

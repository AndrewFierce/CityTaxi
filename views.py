from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from django.core.mail import send_mail

def index(request):
	return render(
		request,
		'index.html',
	)

def sentinfo(request):
	if request.method == 'POST':
		fio = request.POST.get('fio', '')
		tel = request.POST.get('tel', '')
		driver = request.POST.get('driver', '')
		passport = request.POST.get('passport', '')
		auto = request.POST.get('auto', '')
		sts = request.POST.get('sts', '')
		licence = request.POST.get('licence', '')
		addinfo = request.POST.get('addinfo', '')
		email = "radugaug@mail.ru"
		print(fio)
		print(tel)
		print(driver)
		print(passport)
		print(auto)
		print(sts)
		print(licence)
		print(addinfo)
		print(email)
		# send_mail('Driver form', 'Фамилия Имя Отчество: '+fio+'.\n Телефон: '+tel+'.\n Водительское улостоверение: '+driver+'.\n Паспорт: '+passport+'.\n Автомобиль: '+auto+'.\n Серия и номер СТС: '+sts+'.\n Номер лицензии, если есть: '+licence+'.\n Дополнительные сведения: '+addinfo, None, [email], fail_silently=False)
		return redirect('index')
	else:
		return redirect('index')
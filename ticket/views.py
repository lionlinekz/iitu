from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from ticket.models import Sura, Ayat, Word

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'suras': Sura.objects.all().order_by('-index')}
    context_dict['ayats'] = Ayat.objects.all()

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return HttpResponseRedirect('/114/1')

def sura(request, sura):
    surah = Sura.objects.filter(index=int(sura))
    ayats = Ayat.objects.filter(sura=surah)
    context_dict = {'ayats': ayats}
    return render(request, 'index.html', context_dict)

def complete_ayat(request):
    if request.method =='POST':
        aya = request.POST['ayat']
        ayat = Ayat.objects.get(index_to_quran=int(aya))
        ayat.completed = True
        ayat.save()
    return HttpResponseRedirect('/%s/1' % ayat.sura.index)

def complete_sure(request):
    if request.method =='POST':
        sure = request.POST['sure']
        sura = Sura.objects.get(index = int(sure))
        sura.completed = True
        sura.save()
    return HttpResponseRedirect('/%s/1' % sura.index)



def ayat(request, sura, ayat):
    context_dict = {'suras': Sura.objects.all().order_by('-index')}
    sura = Sura.objects.get(index=int(sura))
    ayat = Ayat.objects.filter(sura=sura).get(index_to_surah=int(ayat))
    ayat.russian = ayat.russian.partition("[[")[0]
    ayat.save()
    ayahs = Ayat.objects.filter(sura=sura)
    context_dict['ayat'] = ayat
    context_dict['ayahs'] = ayahs
    words = Word.objects.filter(ayat=ayat)
    context_dict['words'] = words


    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict['words'] =  words
    if request.method =='POST':
        kazakh = request.POST['kazakh']
        russian = request.POST['russian']
        word_index = request.POST['word_index']
        print word_index
        word = Word.objects.get(index_to_quran=int(word_index))
        word.qazaq = kazakh.strip()
        word.rus = russian.strip()
        word.save()
    return render(request, 'index.html', context_dict)


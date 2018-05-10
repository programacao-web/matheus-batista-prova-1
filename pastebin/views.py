from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from pastebin.forms import PasteForm
from pastebin.models import Paste
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def index(request):
    form = PasteForm()
    ctx = {'title': 'Bem vindo ao Pastebin'}

    if request.method == 'GET':
        ctx['form'] = form
        return render(request, 'pastebin/index.jinja2', ctx)
    elif request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            return redirect('pastebin:pastebin-detail', id=paste.id)
        else:
            return render(request, 'pastebin/index.jinja2', {'form': form})


def highlight_code(paste):

    lexer = get_lexer_by_name(paste.language, stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="highlight")
    highlighted = highlight(paste.code, lexer, formatter)

    return highlighted


def paste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    ctx = {'title': paste.title, 'paste': paste}


    ctx['highlighted'] = highlight_code(paste)
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    if language == "python" or language == "js":
        pastes = Paste.objects.filter(language=language)
    else:
        pastes = Paste.objects.all().exclude(language='python').exclude(language='js')

    ctx = {'language': language, 'pastes': pastes}
    return render(request, 'pastebin/paste-language.jinja2', ctx)
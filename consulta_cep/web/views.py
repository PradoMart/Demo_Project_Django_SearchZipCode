from django.shortcuts import render
import requests

def consulta_cep(request):
    dados = None
    erro = None

    if request.method == 'POST':
        cep = request.POST.get('cep')
        if not cep:
            erro = 'Por favor, insira um CEP válido.'
        else:
            url = f'https://brasilapi.com.br/api/cep/v1/{cep}'
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                dados = response.json()
            except requests.exceptions.RequestException:
                erro = 'Erro ao consultar o CEP. Verifique e tente novamente.'
    return render(request,'consulta_cep.html',{'dados': dados, 'erro': erro})
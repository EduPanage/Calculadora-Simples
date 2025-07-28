from django.shortcuts import render

def index(request):
    resultado = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
            operacao = request.POST['operacao']

            if operacao == 'soma':
                resultado = num1 + num2
            elif operacao == 'subtrai':
                resultado = num1 - num2
            elif operacao == 'multiplica':
                resultado = num1 * num2
            elif operacao == 'divide':
                resultado = num1 / num2
        
        except Exception as e:
            resultado = f"Erro: {e}" 

    return render(request, 'index.html', {'resultado': resultado})

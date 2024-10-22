from django.shortcuts import render, HttpResponse

def home(request):
    if request.method == "POST":
        numero = float(request.POST.get("numero", 0).replace(",", "."))
        base = float(request.POST.get("base", 0))
        base_desejada = float(request.POST.get("base_desejada", 0))
        valor_ope_1 = float(request.POST.get("valor_ope_1", 0))
        valor_ope_2 = float(request.POST.get("valor_ope_2", 0))
        base_opera = float(request.POST.get("base_opera", 0))
        operacoes = request.POST.get("operacoes")
        return render(request, "home.html", {"Resultado": Resultado})

    return render(request, "home.html")

def calcular(request):
    if request.method=="POST":
        numero = float(request.POST.get("numero",0).replace(",","."))
        base = int(request.POST.get("base",0))
        base_desejada = int(request.POST.get("base_desejada",0))

        if "." in str(numero):
            numero_str = str(numero)
            parte_inteira , parte_decimal = numero_str.split(".")
            dec = len(parte_decimal)
            parte_inteira = int(numero)
            parte_decimal = int((numero - parte_inteira) * 10**dec)
            Resultado = str(calcula_base(parte_inteira, base, base_desejada)) + "," + str(calcula_base(parte_decimal, base, base_desejada))


        else:
            numero = int(numero)
            Resultado = calcula_base(numero, base, base_desejada)

        Resultado_opera = request.POST.get("Resultado_opera", "")
        return render(request, "home.html", {"Resultado": Resultado, "Resultado_opera": Resultado_opera})

    return HttpResponse("Requisição invalida")

def operacoes(request):
    if request.method == "POST":
        valor_ope_1 = float(request.POST.get("valor_ope_1", 0).replace(",","."))
        valor_ope_2 = float(request.POST.get("valor_ope_2", 0).replace(",","."))
        base_opera = int(request.POST.get("base_opera", 0))
        operacoes = request.POST.get("operacoes")

        if "." in str(valor_ope_1) or str(valor_ope_2):
            numero_str_1 = str(valor_ope_1)
            numero_str_2 = str(valor_ope_2)
            parte_inteira_1 , parte_decimal_1 = numero_str_1.split(".")
            parte_inteira_2, parte_decimal_2 = numero_str_2.split(".")
            dec_1 = len(parte_decimal_1)
            dec_2 = len(parte_decimal_2)
            parte_inteira_1 = int(valor_ope_1)
            parte_inteira_2 = int(valor_ope_2)
            parte_decimal_1 = int((valor_ope_1 - parte_inteira_1) * 10**dec_1)
            parte_decimal_2 = int((valor_ope_2 - parte_inteira_2) * 10 ** dec_2)
            if operacoes == "dividir":
                Resultado_opera = str(operacoes_operacoes(parte_inteira_1, parte_inteira_2, base_opera, operacoes)) + "," + "0"

            else:
                Resultado_opera = str(operacoes_operacoes(parte_inteira_1, parte_inteira_2, base_opera, operacoes)) + "," + str(operacoes_operacoes(parte_decimal_1, parte_decimal_2, base_opera, operacoes))

            Resultado = request.POST.get("Resultado", "")

            return render(request, "home.html", {"Resultado": Resultado, "Resultado_opera": Resultado_opera})
    return HttpResponse("Requisição inválida")


#calculadora de base

def operacoes_operacoes(valor_ope_1, valor_ope_2, base_opera, operacoes):
    if operacoes == "somar":
        return soma_de_base(valor_ope_1, valor_ope_2, base_opera)
    elif operacoes == "subtrair":
        return subtracao_de_base(valor_ope_1, valor_ope_2, base_opera)
    elif operacoes == "multiplicar":
        return multiplicacao_base(valor_ope_1, valor_ope_2, base_opera)
    elif operacoes == "dividir":
        return divisao_base(valor_ope_1, valor_ope_2, base_opera)
    else:
        return "Erro: Operação inválida"

def calcula_base(numero, base, base_desejada):
    numero = str(numero)
    Q = int(len(numero))
    Resultado = 0
    Q = Q-1
    T = 0
   
    while Q >= 0:
        parcial = soma_de_base(int(numero[T]),multiplicacao_base(Resultado,base,base_desejada),base_desejada)
        Resultado = parcial
        T += 1
        Q -= 1
    return Resultado
    
def multiplicacao_base(valor_1, valor_2, base):
    valor_1 = str(valor_1)[::-1]  
    valor_2 = str(valor_2)[::-1]
    
    resultado_parcial = [0] * (len(valor_1) + len(valor_2)) 

   
    for i in range(len(valor_1)):
        for j in range(len(valor_2)):
            multiplicacao = int(valor_1[i]) * int(valor_2[j])
            soma = multiplicacao + resultado_parcial[i + j]

            resultado_parcial[i + j] = soma % base
            resultado_parcial[i + j + 1] += soma // base

    
    while len(resultado_parcial) > 1 and resultado_parcial[-1] == 0:
        resultado_parcial.pop()

    resultado = ''.join(map(str, resultado_parcial[::-1])) 
    return int(resultado)


def soma_de_base(valor_1, valor_2, base):
    if valor_2 > valor_1:
        valor_1 , valor_2 = valor_2, valor_1
    loop_1 = len(str(valor_1))
    loop_2 = len(str(valor_2))
    valor_1 = (str(valor_1)[::-1])
    valor_2 = (str(valor_2)[::-1])
    R = 0
    Resultado_mut = 0
    while loop_1 > 0:
        if loop_2 < 1:
            primeiro_resultado = int(valor_1[R]) + 0
        elif loop_1 < 1:
            primeiro_resultado = 0 + int(valor_2[R])
        else:
            primeiro_resultado = int(valor_1[R]) + int(valor_2[R])
        if primeiro_resultado >= base:
            resto = primeiro_resultado % base
            quociente = primeiro_resultado // base 
            primeiro_resultado = str(quociente) + str(resto)
        Resultado_mut = Resultado_mut + int(primeiro_resultado)*(10**R)
        R += 1
        loop_1 -= 1
        loop_2 -= 1
    Resultado_mut = int(Resultado_mut)
    return Resultado_mut

def subtracao_de_base(valor_1, valor_2, base):
    if valor_2 > valor_1:
        valor_1, valor_2 = valor_2, valor_1
    loop_1 = len(str(valor_1))
    loop_2 = len(str(valor_2))
    valor_1 = (str(valor_1)[::-1])
    valor_2 = (str(valor_2)[::-1])
    R = 0
    Resultado_mut = 0
    emprestimo = 0
    while loop_1 > 0:
        if loop_2 < 1:
            primeiro_resultado = int(valor_1[R]) - 0 - emprestimo
        elif loop_1 < 1:
            primeiro_resultado = 0 - int(valor_2[R]) - emprestimo
        else:
            primeiro_resultado = int(valor_1[R]) - int(valor_2[R]) - emprestimo

        if primeiro_resultado < 0:
            primeiro_resultado += base
            emprestimo = 1
        else:
            emprestimo = 0

        Resultado_mut = Resultado_mut + int(primeiro_resultado) * (10 ** R)
        R += 1
        loop_1 -= 1
        loop_2 -= 1

    Resultado_mut = int(Resultado_mut)
    return Resultado_mut


def divisao_base(valor_1, valor_2, base):

    if valor_2 == 0:
        raise ValueError("Divisão por zero não é permitida!")


    valor_1_decimal = int(str(valor_1), base)
    valor_2_decimal = int(str(valor_2), base)


    quociente_decimal = valor_1_decimal // valor_2_decimal
    resto_decimal = valor_1_decimal % valor_2_decimal


    quociente = ''
    resto = ''


    while quociente_decimal > 0:
        quociente = str(quociente_decimal % base) + quociente
        quociente_decimal //= base


    while resto_decimal > 0:
        resto = str(resto_decimal % base) + resto
        resto_decimal //= base


    if quociente == '':
        quociente = '0'


    if resto == '':
        resto = '0'

    return quociente


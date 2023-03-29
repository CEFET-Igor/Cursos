let result = window.document.getElementById('detail')
result.style.display = 'none'
let select = window.document.getElementById('select')
var a = []

function addNumber() {
    result.style.display = 'none'
    result.innerHTML = ''
    var num = window.document.getElementById('number')
    if(num.value.length == 0){
        result.innerHTML = '<span>Por favor insira um número</span>'
    }else{
        let n = Number(num.value)
        if(n <= 0 || n > 100){
            result.innerHTML = '<span>Insira um número entre 1 -100 </span>'
        }else{
            if(a.indexOf(n) == -1){
                a.push(n)
                let option = window.document.createElement('option')
                option.text = `O número ${n} foi adicionado`
                option.value = a.length
                select.appendChild(option)
            }else{
                result.innerHTML = '<span>O analizador ja possui este número \nPor favor insira outro número ou finalize o teste </span>'
            }
            num.value = ''
            num.focus()
        }
    }
    result.style.display = 'block'
}

function seeDetail() {
    result.innerHTML = ''
    if(a.length == 0){
        result.innerHTML = '<span>Insira algum número para que avaliar-mos o resultado</span>'
    }else{
        var sum = 0
        var maior = a[0]
        var menor = a[0]
        for( let c in a){
            sum += a[c]
            if (a[c] > maior){
                maior = a[c]
            }
            if(a[c] < menor){
                menor = a[c]
            }
        }
        result.innerHTML += `<p>Ao todo foram cadastrados ${a.length} números</p>`
        result.innerHTML += `<p>O maior número cadastrado foi ${maior}</p>`
        result.innerHTML += `<p>O menor número cadastrado foi ${menor}</p>`
        result.innerHTML += `<p>O somatorio de todos os numeros é ${sum}</p>`
        result.innerHTML += `<p>A media de todos os números é ${sum/a.length}</p>`
    }
    result.style.display = 'block'
}
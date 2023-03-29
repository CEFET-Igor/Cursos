var res = window.document.getElementById('res')
res.style.display = 'none'
function gerarTabuada() {
    res.innerHTML = ''
    let num = window.document.getElementById('num').value
    if(num.length == 0){
        var span = window.document.createElement('spam')
        span.innerHTML = '<h3>Por Favor digite um numero</h3>'
        res.appendChild(span)
    }else{
        var n = Number(num)
        var select = window.document.createElement('select')
        select.setAttribute('name','tab')
        select.setAttribute('class','tab')
        select.setAttribute('size','11')
        
        for(var c = 0; c <= 10; c++){

            let option = window.document.createElement('option')
            option.text = `${n} X ${c} = ${n*c}`
            option.value = `tab${c}`
            select.appendChild(option)

        }
        res.appendChild(select)
    }
    res.style.display = 'block'
}

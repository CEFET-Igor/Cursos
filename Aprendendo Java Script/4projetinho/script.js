function contar() {
    var inicio = window.document.getElementById('inicio').value
    var fim = window.document.getElementById('fim').value
    var passo = window.document.getElementById('passo').value
    const resp = window.document.getElementById('resp')
    resp.innerHTML = ''

    if(inicio.length == 0 || fim.length == 0 || passo.length == 0){
        window.alert('[ERRRO] Faltam dados')
    }else{
        let i = Number(inicio)
        let f = Number(fim)
        let p = Number(passo)
        resp.innerHTML = 'Contando...<br>'
        if(i<f){
            for(var c = i; c <= f; c +=p){
                resp.innerHTML += `${c} \u{1F4A5} `
            }
        }else{
            for(var c = i; c >= f; c -=p){
                resp.innerHTML += `${c} \u{1F4A5} `
            }
        }
        resp.innerHTML += `\u{1F3C1}`
        console.log(resp)

    }


}
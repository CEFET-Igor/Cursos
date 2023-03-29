function load() {
    var im = window.document.querySelector('#photo')
    console.log(im)
    var msg = window.document.getElementById('msg')
    console.log(msg)
    var data = new Date()
    var horas = data.getHours()
    if (horas < 12){
        msg.innerHTML = `<p> Agora são ${horas} horas.</p>
        <strong><p>Bom dia</p></strong>`
        im.src = 'imgs/img-manha-250.png'
        im.alt = 'Foto de manhã'
        window.document.body.style.background = '#f1faff'
    } else if (horas >= 12 && horas <= 18){
        msg.innerHTML = `<p> Agora são ${horas} horas.</p>
        <strong><p>Boa Tarde</p></strong>`
        im.src = 'imgs/img-tarde-250.png'
        im.alt = 'Foto de tarde'
        window.document.body.style.background = '#eae6df'
    }else{
        msg.innerHTML = `<p> Agora são ${horas} horas.</p>
        <strong><p>Boa noite dia</p></strong>`
        im.src = 'imgs/img-noite-250.png'
        im.alt = 'Foto de noite'
        window.document.body.style.background = '#4d107b'
    }
}
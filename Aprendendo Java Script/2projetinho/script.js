const msg = window.document.getElementById('content')
const date = new Date()
var bday = window.document.getElementById('birth-date')
var today = date.toISOString().slice(0, 10);
bday.max = today

function verificar() {

    /* 
     * Verificação do idade 
    */

    var year = date.getFullYear()
    var date1 = new Date(bday.value)
    var byear = date1.getFullYear()
    var age = year - byear

    if( byear > year || bday == ''){
        msg.innerHTML = '<p>[ERRO] Preencha os dados corretamente</p>'
    }else{
        
        var sex = window.document.getElementsByName('choiceSex')
        var img = window.document.createElement('img')
        img.setAttribute('id','photo')
        
        /** 
         * Verificação de gẽnero
         * Adição das imagens 
         * Adição dos textos
         */

        if(sex[0].checked){
            if(age >= 0 && age < 4){''       
                img.setAttribute('src', 'imgs/bebe-menino-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é um bebe, do sexo masculino, com ${age} anos</p>`                
            }else if(age >=4 && age <10 ){
                img.setAttribute('src','imgs/adolescente-homem-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é uma criança, do sexo masculino, com ${age} anos</p>`
            }else if(age >= 10 && age < 21){  
                img.setAttribute('src','imgs/adolescente-homem-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é um jovem/adolecente, do sexo masculino, com ${age} anos</p>`
            }else if(age >= 21 && age < 60){
                img.setAttribute('src','imgs/adulto-homem-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é um adulto, do sexo masculino, com ${age} anos</p>`
            }else if (age >=60){
                img.setAttribute('src','imgs/idoso-homem-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é um idoso, do sexo masculino, com ${age} anos</p>`
            }else{
                msg.innerHTML = '<p>[ERRO] confira as informações da sua idade</p>'
            }
        
        }else {
            var img = window.document.createElement('img')
            img.setAttribute('id','photo')
            if(age >= 0 && age < 4){
                img.setAttribute('src', 'imgs/bebe-menina-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é um bebe, do sexo feminino, com ${age} anos</p>`
            }else if(age >=4 && age <10 ){
                img.setAttribute('src', 'imgs/adolescente-mulher-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é uma criança, do sexo feminino, com ${age} anos</p>`
            }else if(age >= 10 && age < 21){
                img.setAttribute('src', 'imgs/adolescente-mulher-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é uma jovem/adolecente, do sexo feminino, com ${age} anos</p>`
            }else if(age >= 21 && age < 60){
                img.setAttribute('src', 'imgs/adulta-mulher-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é uma adulta, do sexo feminino, com ${age} anos</p>`
            }else if (age >=60){
                img.setAttribute('src', 'imgs/idosa-mulher-250.png')
                msg.innerHTML = `<p>Pelas informações recebidas detectamos que você é uma idosa, do sexo feminino, com ${age} anos</p>`
            }else{
                msg.innerHTML = '<p>[ERRO] confira as informações da sua idade</p>'
            }
        }
        msg.appendChild(img) 
    }
}
 
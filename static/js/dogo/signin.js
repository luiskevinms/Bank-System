document.getElementById("btn-signin").addEventListener("click", login);

function login(){
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;


    if(email === "") {
        Swal.fire({
            title: 'Correo electrónico no ingresado',
            text: 'Debe ingresar su correo electrónico.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    if(password === "") {
        Swal.fire({
            title: 'Contraseña no ingresada',
            text: 'Debe ingresar una contraseña.',
            icon: 'warning',
            confirmButtonText: 'Aceptar'
        });
        return;
    }

    const fecha = new Date();
    let hora = fecha.getHours()
    
    switch(hora){

        case hora < 12:
            hora = 'Buenos dias'
    }

    
    const data = {
        email: email,
        password: password,
        hora_actual: hora
    }

    fetch('api/login', {
        method:"POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result =>  {
        if(result.success){
                window.location.href = "/welcome";
        } else {
            Swal.fire({
            title: 'Datos incorrectos',
            text: 'Sus datos de acceso no son correctos',
            icon:  'error',
            confirmButtonText: 'Aceptar'
            });
        }
    })
    .catch(error => {
        console.error(error);
    })
}
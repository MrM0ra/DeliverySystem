document.addEventListener('DOMContentLoaded', () =>{
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', () =>{
        socket.send("Estoy conectado");
    });

    socket.on('message', data => {
        console.log(`Mensaje recibido: ${data}`)
    });

})
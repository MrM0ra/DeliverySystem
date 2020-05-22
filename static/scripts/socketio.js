document.addEventListener('DOMContentLoaded', () =>{
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', () =>{
        socket.send("Estoy conectado");
    });

    socket.on('message', data => {
       const p = document.createElement('p'); //paragraph element
       const br = document.createElement('br'); //line break
       p.innerHTML = data;
       document.querySelector('#display-message-section').append(p);

    });

    socket.on('some_event', data=>{
        console.log(data);
    });

    document.querySelector('#send_message').onclick = () => {
        socket.send(document.querySelector('#user_message').value);
    };

})
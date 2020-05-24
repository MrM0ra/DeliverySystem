document.addEventListener('DOMContentLoaded', () => {
   let msg = docuemnt.querySelector('#user_message');
   msg.addEventListener('keyup', event => {
       event.preventDefault();
       if (event.keyCode === 13){
           documento.querySelector('#send_message').click();
       }
       
   }) 
})
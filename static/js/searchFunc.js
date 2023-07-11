document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        console.log('Submitted.')
        const query = document.querySelector('#searchIn').value;
        
        $.ajax({
            url:'/',
            type:'POST',
            data:{'query':query}
        })
    };
});





//sends search box content to python file when search submitted

            
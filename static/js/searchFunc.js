

//sends search box content to python file when search submitted
document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('form').onsubmit = function() {
            const query = document.querySelector('#searchIn').value;
            $.ajax({
                url:'/',
                type:'POST',
                data:{'query':query}
            })
        };

        
        });

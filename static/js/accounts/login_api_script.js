let loginForm = document.getElementById('loginForm');
let username = document.getElementById('username');
let password = document.getElementById('password');


loginForm.addEventListener('submit', (e) => {
    e.preventDefault();

    $.ajax({
        url: 'http://127.0.0.1:8000/accounts/login_api/',
        method: 'post',
        data: JSON.stringify({username: `${username.value}`, password: `${password.value}`}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response){localStorage.setItem('apiToken', response.token)},
        error: function(response){console.log(response);}
    });

    loginForm.submit();
})



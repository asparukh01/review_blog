let logoutBtn = document.getElementById('logouting')


logoutBtn.addEventListener('click', () => {
    e.preventDefault();
    $.ajax({
        url: 'http://127.0.0.1:8000/accounts/logout_api/',
        method: 'post',
        headers: {'Authorization': 'Token ' + `${localStorage.apiToken}`},
        dataType: 'json',
        success: function(response){localStorage.removeItem('apiToken');
        window.location.replace('http://127.0.0.1:8000/accounts/account/list/')},
        error: function(response){console.log(response);}
    });    
})


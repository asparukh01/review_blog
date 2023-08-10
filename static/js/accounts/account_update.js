let button_update = $('#button_update')[0];
button_update.addEventListener('click', (e) => {
    e.preventDefault()
    let account = $('#button_update').data('account-id')
    let first_name = document.getElementById('first_name')
    let last_name = document.getElementById('last_name')
    let email = document.getElementById('email')
    let phone = document.getElementById('phone')

    $.ajax({
        url: `http://127.0.0.1:8000/accounts/profile/update/${account}/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            'first_name': first_name.value,
            'last_name': last_name.value,
            'email': email.value,
            'phone': phone.value,
        }),
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            console.log(data)
            window.location.replace('http://127.0.0.1:8000/accounts/account/list/')
        },
        error: function (err) {
            console.log(err);
        }
    });
})
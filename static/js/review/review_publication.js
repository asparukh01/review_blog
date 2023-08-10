let buttonPublication = $('#publication')[0];
buttonPublication.addEventListener('click', (e) => {
    e.preventDefault()
    let review = $('#review_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/review/${review.innerText}/publication/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            status: 'Принят'
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});

let buttonUnpublication = $('#unpublication')[0];
buttonUnpublication.addEventListener('click', (e) => {
    e.preventDefault()
    let review = $('#review_id')[0];
    $.ajax({
        url: `http://127.0.0.1:8000/api/review/${review.innerText}/publication/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({
            status: 'Отклонен'
        }),
        dataType: "json",
        contentType: "application/json",
        success: (data) => {
                    console.log(data)
                    window.location.reload()
                },
        error: function (err) {
            console.log(err);
        }
    });
});
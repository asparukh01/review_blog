let delete_post = document.getElementById('delete_review')
delete_post.addEventListener('click', (e) => {
        e.preventDefault()
        let  review = $('#review_id')[0]
        $.ajax({
                url: `http://127.0.0.1:8000/api/review/delete/${review.innerText}/`,
                method: 'delete',
                headers: {'Authorization': `Token ${localStorage.apiToken}`},
                dataType: 'json',
                contentType: 'application/json',
                success: (data) => {
                    console.log(data)
                    window.location.replace('http://127.0.0.1:8000/')
                },
                error: function (err) {
                    console.log(err)
                }
            }
        )
    }
)



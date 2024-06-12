document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function () {
            const imageId = this.getAttribute('data-image-id');
            const likeButton = this;

            fetch('/like-image/' + imageId + '/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                likeButton.textContent = data.likes_count;
                if (data.liked) {
                    likeButton.classList.remove('btn-danger');
                    likeButton.classList.add('btn-success');
                } else {
                    likeButton.classList.remove('btn-success');
                    likeButton.classList.add('btn-danger');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
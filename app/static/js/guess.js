document.getElementById('guessForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const guessValue = document.getElementById('guessInput').value;
    const formData = new FormData();
    formData.append('guess', guessValue);
    
    fetch('/guess', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = data.message;
        messageDiv.style.display = 'block';
        
        if (data.correct) {
            messageDiv.innerHTML += '<br><button onclick="resetGame()" class="btn btn-primary btn-sm mt-2">Jogar Novamente</button>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function resetGame() {
    fetch('/guess/reset', {
        method: 'GET'
    })
    .then(() => {
        document.getElementById('message').style.display = 'none';
        document.getElementById('guessInput').value = '';
    });
}
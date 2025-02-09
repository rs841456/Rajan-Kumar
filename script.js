document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

async function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    if (userInput.value.trim() === '') return;

    // Display user message
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user');
    userMessage.innerHTML = `<p>${userInput.value}</p>`;
    chatBox.appendChild(userMessage);

    // Send user message to the backend
    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput.value }),
        });

        const data = await response.json();

        // Display bot response
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot');
        botMessage.innerHTML = `<p>${data.message}</p>`;
        chatBox.appendChild(botMessage);
    } catch (error) {
        console.error('Error:', error);
        const errorMessage = document.createElement('div');
        errorMessage.classList.add('message', 'bot');
        errorMessage.innerHTML = `<p>Sorry, something went wrong. Please try again.</p>`;
        chatBox.appendChild(errorMessage);
    }

    // Clear input field
    userInput.value = '';
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}
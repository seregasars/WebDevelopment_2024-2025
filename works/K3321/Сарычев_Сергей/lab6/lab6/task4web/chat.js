// chat.js

const ws = new WebSocket('ws://localhost:8765')
const chat = document.getElementById('chat')
const msgInput = document.getElementById('msg')

let nicknameSet = false

ws.onmessage = (event) => {
  const msg = event.data

  if (!nicknameSet && msg === 'Введите никнейм:') {
    const nickname = prompt('Введите ваш никнейм:')
    ws.send(nickname)
    nicknameSet = true
    return
  }

  if (msg.includes('Никнейм уже занят')) {
    alert(msg)
    ws.close()
    return
  }

  chat.innerHTML += msg + '<br>'
  chat.scrollTop = chat.scrollHeight
}

function sendMessage() {
  const text = msgInput.value
  if (text !== '') {
    ws.send(text)
    msgInput.value = ''
  }
}

msgInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage()
})

import { login } from './api.js'

const validEmail = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase())
}

const setup = () => {
    document.querySelector('#login').addEventListener('click', async () => {
        const username = document.getElementById('user-name').value
        const password = document.getElementById('password').value

        if (username.length && password.length) {
            const error = await login(username, password)

            if (error) {
                document.getElementById('error').innerText = error
            }
        } else {
            document.getElementById('error').innerText = 'Insufficient account information provided.'
        }
    })
}

window.onload = setup
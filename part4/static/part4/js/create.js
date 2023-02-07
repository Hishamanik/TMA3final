import { createUser } from './api.js'

const validEmail = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase())
}

const setup = () => {
    document.querySelector('#create').addEventListener('click', () => {
        const firstName = document.getElementById('first-name').value
        const lastName = document.getElementById('last-name').value
        const userName = document.getElementById('user-name').value
        const email = document.getElementById('email').value
        const password = document.getElementById('password').value

        if (firstName.length && lastName.length && userName.length && validEmail(email) && password.length) {
            createUser({
                firstName,
                lastName,
                userName,
                email,
                password
            })
        } else {
            document.getElementById('error').innerText = 'Insufficient account information provided.'
        }
    })
}

window.onload = setup
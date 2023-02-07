import { removeFromCart, placeOrder } from './api.js'

const setup = () => {
    document.querySelectorAll('.remove').forEach(btn => btn.addEventListener('click', () => {
        const computerId = btn.parentElement.parentElement.id
        removeFromCart(computerId)
    }))

    document.getElementById('order').addEventListener('click', () => {
        const current = document.querySelectorAll('.computer-list-item')
        if (current.length > 0) {
            placeOrder()
        }
    })
}

window.onload = setup
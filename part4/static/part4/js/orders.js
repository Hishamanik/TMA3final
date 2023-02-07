import { cancelOrder, placeOrder } from './api.js'

const setup = () => {
    document.querySelectorAll('.remove').forEach(btn => btn.addEventListener('click', () => {
        const computerId = btn.parentElement.parentElement.id
        cancelOrder(computerId)
    }))

}

window.onload = setup
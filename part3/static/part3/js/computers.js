import { loadCart } from "./main.js"
import { addToCart } from "./helpers.js"

const setup = () => {
    document.querySelectorAll('.computer-list-btn.add').forEach(btn => btn.addEventListener('click', (event) => {
        const computers = JSON.parse(document.getElementById('computers').textContent)
        const selectedId = btn.parentElement.parentElement.id
        addToCart(computers.find(c => c.id === parseInt(selectedId)))
        loadCart()
    }))
}

window.onload = setup
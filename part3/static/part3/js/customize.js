import { clearlist, buildComponentList, addToCart } from './helpers.js'
import { loadCart } from './main.js'

let computer, allComponents

const updateComponents = () => {
    const items = document.querySelectorAll('.store-selected-item')
    const selectedComponents = Object.entries(computer.components)
    selectedComponents.forEach((entry, idx) => {
        const [category, id] = entry
        const componentName = allComponents[category].find(c => c.id === id).name
        items[idx].firstElementChild.innerText = componentName
    })
    document.querySelector('#store-cart-btn').disabled = false
}

const calculatePrice = () => {
    const priceDiv = document.querySelector('.store-price')
    let newPrice = 0
    const selectedComponents = Object.entries(computer.components)
    selectedComponents.forEach((entry, idx) => {
        const [category, id] = entry
        const componentPrice = allComponents[category].find(c => c.id === id).price
        newPrice += componentPrice
    })
    priceDiv.firstElementChild.innerText = newPrice.toFixed(0) - 0.01
}

const selectComponent = (component) => {
    const category = document.querySelector('#category-select').value
    if (computer.components[category] != component.id) {
        computer.components[category] = component.id
    }
    calculatePrice()
    updateComponents()
}

const buildInfoUI = (component) => {
    const name = document.createElement('div')
    name.classList.add('component-name')
    const price = document.createElement('div')
    price.classList.add('component-price')
    const btn = document.createElement('button')
    btn.classList.add('component-select')

    btn.addEventListener('click', () => selectComponent(component))

    name.innerText = component.name
    price.innerText = `$${component.price}`
    btn.innerText = 'Select'
    return [name, price, btn]
}

const setup = () => {
    document.querySelector('#fetch-components-btn')
        .addEventListener('click', () => buildComponentList(buildInfoUI))
    
    document.querySelector('#store-cart-btn')
        .addEventListener('click', (event) => {
            addToCart(computer)
            loadCart()     
        })
        
    buildComponentList(buildInfoUI)

    computer = JSON.parse(document.getElementById('computer').textContent)
    allComponents = JSON.parse(document.getElementById('all_components').textContent)
}

window.onload = setup
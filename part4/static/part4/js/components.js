import { clearlist, buildComponentList } from './helpers.js'

const buildInfoUI = (component) => {
    const name = document.createElement('div')
    name.classList.add('component-name')
    const price = document.createElement('div')
    price.classList.add('component-price')

    name.innerText = component.name
    price.innerText = `$${component.price}`
    return [name, price]
}

const setup = () => {
    document.querySelector('#fetch-components-btn')
        .addEventListener('click', () => buildComponentList(buildInfoUI))
        
    buildComponentList(buildInfoUI)
}

window.onload = setup
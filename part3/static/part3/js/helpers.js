import { getComponents } from './api.js'

export const clearlist = (list) => {
    while (list.firstChild) {
        list.removeChild(list.firstChild);
    }
}

export const buildComponentList = async (buildInfoUIFn) => {
    const components = await getComponents()
    const category = document.querySelector('#category-select').value
    const componentsToDisplay = components[category]
    const compList = document.querySelector('.store-selector-components')

    clearlist(compList)

    componentsToDisplay.forEach(component => {
        const root = document.createElement('div')
        root.classList.add('component')
        const compinfo = document.createElement('div')
        compinfo.classList.add('component-info')
        const name = document.createElement('div')
        name.classList.add('component-name')
        const price = document.createElement('div')
        price.classList.add('component-price')
        const btn = document.createElement('button')
        btn.classList.add('component-select')
        const desc = document.createElement('div')
        desc.classList.add('component-description')

        desc.innerText = component.description

        const infoComps = buildInfoUIFn(component)
        infoComps.forEach(infoComp => compinfo.appendChild(infoComp))
        root.appendChild(compinfo)
        root.appendChild(desc)
        compList.appendChild(root)
    })
}

export const addToCart = (computer) => {
    const cookie = getCookie('cart')
    let cart
    if (!cookie) {
        cart = []
        computer.index = 0
    } else {
        cart = JSON.parse(cookie)
        computer.index = cart.length + 1
    }
    
    cart.push(computer)
    setCookie('cart', JSON.stringify(cart), 365)
}

export const removeFromCart = (id) => {
    const cookie = getCookie('cart')
    if (!cookie) {
        return
    }

    let cart = JSON.parse(cookie)
    const newCart = []
    cart.forEach(c => {
        if (c.index !== id) {
            newCart.push(c)
        }
    })
    setCookie('cart', JSON.stringify(newCart), 365)
}

export const setCookie = (cname, cvalue, exdays) => {
    const d = new Date()
    d.setTime(d.getTime() + (exdays*24*60*60*1000))
    let expires = 'expires='+ d.toUTCString()
    document.cookie = cname + '=' + cvalue + ';' + expires + ';path=/'
}

export const getCookie = (cname) => {
    let name = cname + '='
    let decodedCookie = decodeURIComponent(document.cookie)
    let ca = decodedCookie.split(';')
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i]
        while (c.charAt(0) == ' ') {
            c = c.substring(1)
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length)
        }
    }
}
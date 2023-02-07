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
const BACKEND_URL = 'http://localhost:8000'

const getComponents = async () => {
    const url = new URL(`${BACKEND_URL}/part4/api/components`)
    const resp = await fetch(url)
    if (resp.ok) {
        return resp.json()
    } else {
        console.log(resp)
        alert('Backend error')
    }
}

const createUser = async (params) => {
    const url = new URL(`${BACKEND_URL}/part4/api/auth/create`)
    const resp = await fetch(url, {
        method: 'POST',
        type: 'application/json',
        body: JSON.stringify(params)
    })

    if (resp.ok) {
        window.location.assign(resp.url)
    } else {
        alert('Backend error occured.')
        console.error(resp, resp.status)
    }
}

const login = async (username, password) => {
    const url = new URL(`${BACKEND_URL}/part4/api/auth/login`)
    url.searchParams.append('username', username)
    url.searchParams.append('password', password)
    const resp = await fetch(url)

    if (resp.ok) {
        window.location.assign(resp.url)
    } else if (resp.status === 403) {
        return 'Incorrect username or password.'
    } else {
        console.error(resp, resp.status)
        return 'Unable to log in.'
    }
}

export const addToCart = async (computer) => {
    const url = new URL(`${BACKEND_URL}/part4/api/cart/add`)
    const resp = await fetch(url, {
        method: 'POST',
        type: 'application/json',
        body: JSON.stringify(computer)
    })

    if (resp.ok) {
        window.location.assign(resp.url)
    } else {
        console.error(resp, resp.status)
    }
}

export const removeFromCart = async (id) => {
    const url = new URL(`${BACKEND_URL}/part4/api/cart/remove`)
    url.searchParams.append('id', id)
    const resp = await fetch(url)

    if (resp.ok) {
        window.location.assign(resp.url)
    } else {
        console.error(resp, resp.status)
    }
}

export const placeOrder = async () => {
    const url = new URL(`${BACKEND_URL}/part4/api/orders/create`)
    const resp = await fetch(url)

    if (resp.ok) {
        window.location.assign(resp.url)
    } else {
        console.error(resp, resp.status)
    }
}

export const cancelOrder = async (id) => {
    const url = new URL(`${BACKEND_URL}/part4/api/orders/cancel`)
    url.searchParams.append('id', id)
    const resp = await fetch(url)

    if (resp.ok) {
        window.location.assign(resp.url)
    } else {
        console.error(resp, resp.status)
    }
}

export { getComponents, createUser, login }
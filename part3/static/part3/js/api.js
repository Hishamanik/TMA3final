const BACKEND_URL = 'http://localhost:8000'

const getComponents = async () => {
    const url = new URL(`${BACKEND_URL}/part3/api/components`)
    const resp = await fetch(url)
    if (resp.ok) {
        return resp.json()
    } else {
        console.log(resp)
        alert('Backend error')
    }
}

export { getComponents, BACKEND_URL }
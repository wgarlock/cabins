/* global csrftoken */

export default function request (obj) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest()
        xhr.open(obj.method || 'POST', 'http://127.0.0.1:8000/api')
        if (obj.headers) {
            Object.keys(obj.headers).forEach(key => {
                xhr.setRequestHeader(key, obj.headers[key])
            })
        }
        xhr.onload = () => {
            if (xhr.status >= 200 && xhr.status < 300) {
                resolve(xhr.response)
            } else {
                reject(xhr.statusText)
            }
        }
        xhr.onerror = () => reject(xhr.statusText)
        const body = JSON.stringify({
            query: `
                query{
                    get${obj.endpoint.getAttribute('data-content')}ById(id: ${obj.endpoint.getAttribute('data-src')}){
                        id
                        title
                        description
                        heroImage{
                            jpeg400
                            jpeg800
                            jpeg1960
                        }
                        ogImage{
                            jpeg400
                            jpeg800
                            jpeg1960
                        }
                    }
                }`,
            csrfmiddlewaretoken: csrftoken
        })
        xhr.send(body)
    })
}

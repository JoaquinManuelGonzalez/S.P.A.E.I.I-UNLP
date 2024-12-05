function postUrl(url, payload) {
    const init = {
        method: 'POST'
    };
    if (!!payload) {
        init.headers = {
            'Content-Type': 'application/json'
        };
        init.body = JSON.stringify(payload)
    }
    return fetch(url, init)
        .then(response => response.json())
        .catch(error => console.error('Error:', error));
}

function deleteUrl(url) {
    const init = {
        method: 'DELETE'
    };
    return fetch(url, init)
        .then(response => response.json())
        .catch(error => console.error('Error:', error));
}
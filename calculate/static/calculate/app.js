
// Add event listener
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#problem1-form").addEventListener('submit', sampleSubmit);
});


// Submit function
function sampleSubmit(event) {
    event.preventDefault();

    let resultHeader = document.querySelector("#result1");
    let x = document.querySelector("#x").value;
    let n = document.querySelector("#n").value;
    
    let requestBody = {
        "x": x,
        "n": n
    };

    sendHttpAsync("result/", "POST", requestBody)
        
        .then(response => {
            resultHeader.innerText = response.body.answer;
        });
}


// JavaScript wrapper function to send HTTP requests using Django's "X-CSRFToken" request header
function sendHttpAsync(path, method, body) {
    let props = {
        method: method,
        headers: {
            "X-CSRFToken": csrftoken
        },
        mode: "same-origin",
    }

    if (body !== null && body !== undefined) {
        props.body = JSON.stringify(body);
    }

    return fetch(path, props)
        .then(response => {
            return response.json()
                .then(result => {
                    return {
                        ok: response.ok,
                        body: result
                    }
                });
        })
        .then(resultObj => {    
            return resultObj;
        })
        .catch(error => {
            throw error;
        });
}
let data = document.getElementById("client_form");
console.log(data);

data.onsubmit = async (e) => {
    console.log("testing number 2!!");
    e.preventDefault();

    let clientData = {};
    let fd = new FormData(data);
    fd.forEach( (v,k) => {clientData[k] = v;});
    console.log(JSON.stringify(clientData));


    const options = {
        method: 'POST',
        body: JSON.stringify(clientData),
        headers: { 'Content-Type': 'application/json' }
    }

    fetch('/postData', options)
        .then(res => res.json())
};

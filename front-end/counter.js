let counter = document.querySelector('.counter');

async function viewsCounter() {
    let response = await fetch('https://n2ssi4tgkrb6gk5jovgfeesu6i0cfcuf.lambda-url.us-east-1.on.aws/');
    if(response.ok){
        let data = await response.json();
        counter.innerHTML = 'Views: ${data}';
    }
    else{
        console.log("HTTP-Error: " + response.status);
    }
}

viewsCounter();

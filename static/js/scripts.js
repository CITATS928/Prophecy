document.getElementById("ask-button").addEventListener("click",function(){
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
.then(response => response.json())
.then(data =>{
    document.getElementById("prediction-result").innerText = data.prediction;
})
.catch(error => console.error('Error: ', error));
});
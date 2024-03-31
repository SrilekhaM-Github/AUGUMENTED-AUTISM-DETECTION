
const form = document.querySelector('form') 
form.addEventListener('submit' , e => {
    e.preventDefault()
    const file = form['img'].files[0]
    const formData = new FormData() 
    formData.append('file' , file) 
    fetch('upload' , {
        "method" : "POST" , 
        "body" : formData
    })
    .then(response => response.json())
    .then(data => {
        const leaf_type = data['tea leaves']
        document.querySelector('.output').textContent = ` ${leaf_type}`
        form.remove()
    }) 
    

})
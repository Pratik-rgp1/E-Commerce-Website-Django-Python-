var updateBtns = document.getElementsByClassName('update-cart')//is in store.html add to cart update

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product //this keyword refers to the current clicked element
        var action = this.dataset.action// on click different action are taken such as adding or  removing
        console.log('productId:', productId, 'action:', action )

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data...')

    var url ='/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json', // request body is in JSON format. 
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId' :productId, 'action':action})
    })

    .then((response) =>{ //promise chain. It waits for the response from the server and processes it when it arrives
        return response.json() //extracts the JSON data from the response.
    })

    .then((data) =>{ //This part of the promise chain processes the data received from the server after parsing it as JSON.
        console.log('data:', data) //logs the received data to the console which contains  information about the updated cart or related information.
        location.reload()
    })
}
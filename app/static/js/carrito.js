document.addEventListener("DOMContentLoaded", function() {
    var cartQuantity = parseInt(document.getElementById("cart-quantity").textContent) || 0;
   
    window.addToCart = function() {
        cartQuantity += 1;
        document.getElementById("cart-quantity").innerHTML = cartQuantity;
    }
});
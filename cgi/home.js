document.addEventListener('DOMContentLoaded', () => {
    const authButton = document.getElementById('auth-button');
    // if(authButton) authButton.addEventListener('click', authButtonClick);
    const infoButton = document.getElementById('info-button');
    if(infoButton) infoButton.addEventListener('click', infoButtonClick);
    const productButton = document.getElementById('product-button');
    if(productButton) productButton.addEventListener('click', productButtonClick);
})

function authButtonClick() {
    const userLogin = document.getElementById('user-login').value;
    if (!userLogin) {
        throw "Element with id 'user-login' not found"
    }
    const userPassword = document.getElementById('user-password').value;
    if (!userPassword) {
        throw "Element with id 'user-password' not found"
    }
    const credentials = btoa(`${userLogin}:${userPassword}`);
    // fetch(`/auth?login=${userLogin}&password=${userPassword}`)
    fetch(`/auth`, {
        headers: {
            'Authorization': `Basic ${credentials}`,
        }
    })
    .then(r=>r.text()).then(r=>console.log(r));
}

function infoButtonClick() {
    const userToken = document.getElementById('user-token').value;
    
    fetch(`/auth`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${userToken}`,
            'My-Header': 'My-Value'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Authentication failed");
        }

        return response.json();
    })
    .then(data => {
        // Успішна автентифікація
        document.getElementById('user-token').value = data;
        console.log("Authentication successful");
    })
    .catch(error => {
        // Помилка під час автентифікації
        document.getElementById('user-token').value = "";
        console.error(`Authentication error: ${error.message}`);
    });
}

function productButtonClick() {
    fetch("/products", {
        method: "POST",
        body: JSON.stringify({
            name: document.getElementById('product-name').value,
            price: document.getElementById('product-price').value,
            image_url: document.getElementById('product-image').value,
        })
    }).then(r=>r.json()).then(r=>console.log(r));
}



// Path: cgi/products.js      


angular
.module('app', [])
.directive('products', function() {
    return {
      restrict: 'E',
      transclude: true,
      scope: {},
      controller: function($scope, $http) {
        $scope.authToken = "";
        $scope.userLogin    = "user";
        $scope.userPassword = "123";
        $scope.products = [];
        $http.get('/products')
        .then( r => $scope.products = r.data.data );

        $scope.addCartClick = (id) => {
            $http({
                url: '/cart',
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${$scope.authToken}`,
                },
                data:  { 'id_product': id }
            }).then( r => console.log(r) );
            // console.log('cart ' + id + ' ' + $scope.authToken);
        }
        $scope.authClick = () => {
            const credentials = btoa(`${$scope.userLogin}:${$scope.userPassword}`);
            // console.log($scope.userLogin + ' ' + $scope.userPassword);
            $http.get(`/auth`, {
                headers: {
                    'Authorization': `Basic ${credentials}`,
                }
            }).then(r=>$scope.authToken = r.data.token);
        }
      },
      templateUrl: `/tpl/product.html`,
      replace: true
    };
  });
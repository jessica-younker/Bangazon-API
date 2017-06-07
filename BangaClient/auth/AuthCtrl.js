$scope.login = function() {
  $http({
    url: `${apiUrl}/api-token-auth/`,
    method: "POST",
    data: {
      "username": $scope.user.username,
      "password": $scope.user.password
    }
  }).then(
    res => {
      RootFactory.setToken(res.data.token);
      if (res.data.token !== "") {
        $location.path('/products');
      }
    },
    console.error
  );
};
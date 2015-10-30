'use static';

var app = angular.module('LoR', ['ngRoute', 'gajus.swing']);

app.config(function($routeProvider) {
	$routeProvider.when('/', {
		controller: 'HomeController',
		templateUrl: '/static/views/home.html'
	})
	.when('/me', {
		controller: 'MeController',
		templateUrl: '/static/views/me.html'
	})
	.when('/create', {
		controller: 'NewQuestionController',
		templateUrl: '/static/views/newQuestion.html'
	});
});

app.controller('HomeController', function($scope) {
	$scope.user = {
		name: 'test'
	};

	$scope.cards = [{
			body: 'this is the first question',
			answered: true
		}, {
			body: 'this is the second question',
			answered: false
		}, {
			body: 'this is the third question',
			answered: false
		}];

	$scope.remove = function(index, obj) {
		console.log($scope.cards[index]);
		$scope.cards[index].answered = true;
        $scope.cards.splice(index, 1);
	};

	$scope.throwoutleft = function(event, obj) {
		// console.log(event);
		// console.log(obj);
	};

	$scope.throwoutright = function(event, obj) {

	};

    $scope.options = {
        throwOutConfidence: function (offset, elementWidth) {
            return Math.min(Math.abs(offset) / 160, 1);
        },
        isThrowOut: function (offset, elementWidth, throwOutConfidence) {
            console.log('isThrowOut', offset, elementWidth, throwOutConfidence);
            return throwOutConfidence === 1;
        }
    };
});

app.controller('MeController', function($scope) {

});

app.controller('NewQuestionController', function($scope) {

});

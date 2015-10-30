'use static';

var app = angular.module('LoR', ['ngRoute']);

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
});

app.controller('MeController', function($scope) {

});

app.controller('NewQuestionController', function($scope) {

});
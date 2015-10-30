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
	})
	.otherwise({
		redirectTo: '/'
	});
});

app.controller('HeaderController', function($scope, $http) {
	$scope.user = {};
	var init = function() {
		$http.get('http://localhost:8000/me')
			.then(function(resp) {
				$scope.user = resp.data;
				console.log(resp.data);
			});
	};

	init();
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
		x = document.getElementsByClassName("question-card");
		x[x.length - 1].style.visibility='hidden';
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
            //console.log('isThrowOut', offset, elementWidth, throwOutConfidence);
            return throwOutConfidence === 1;
        }
    };
});

app.controller('MeController', function($scope) {

});

app.controller('NewQuestionController', function($scope, $http) {
	$scope.question = {};
	$scope.error = '';

	$scope.uploadQuestion = function(body, left, right) {
		$scope.error = '';
		if (!body || body.trim() === '') {
			$scope.error = 'Question body cannot be empty';
			return;
		}
		if (!left || left.trim() === '') {
			$scope.error = 'Left answer cannot be empty';
			return;
		}
		if (!right || right.trim() === '') {
			$scope.error = 'Right answer cannot be empty';
			return;
		}
		var question = {
			question: body.trim(),
			left: left.trim(),
			right: right.trim()
		};
		console.log(question);
		$http.post('http://localhost:8000/questions/', question)
			.then(function(resp) {
				console.log(resp);
			}, function(resp) {
				console.log(resp);
			});
	};
});

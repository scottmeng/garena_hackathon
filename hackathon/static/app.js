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
	.when('/my-questions', {
		controller: 'MyQuestionsController',
		templateUrl: '/static/views/myQuestions.html'
	})
	.when('/my-answers', {
		controller: 'MyAnswersController',
		templateUrl: '/static/views/myAnswers.html'
	})
	.otherwise({
		redirectTo: '/'
	});
});

app.factory('HeaderState', function() {
	var HeaderState = {
		isHeaderVisible: true,
		test: false
	};
	return {
		getHeaderState: function() {
			return HeaderState;
		},
		setHeaderVisible: function(visible) {
			HeaderState.isHeaderVisible = visible;
		}
	};
});

app.factory('TabState', function() {
	var TabState = {
		isTabVisible: true,
		selectedTabIndex: 0
	};

	return {
		getTabState: function() {
			return TabState;
		},
		setTabVisible: function(visible) {
			TabState.isTabVisible = visible;
		},
		setTabSelection: function(tabIndex) {
			TabState.selectedTabIndex = tabIndex;
		}
	};
});

app.controller('HeaderController', function($scope, $http, HeaderState) {
	$scope.headerState = HeaderState.getHeaderState();

	var init = function() {
		$http.get('/me')
			.then(function(resp) {
				$scope.user = resp.data;
			});
	};

	init();
});

app.controller('TabController', function($scope, TabState) {
	$scope.tabState = TabState.getTabState();
});

app.controller('HomeController', function($scope, $http, HeaderState, TabState) {
	$scope.questions = [];
	$scope.topQn = null;
	$scope.leftProx = 0;
	$scope.rightProx = 0;

	var init = function() {
		HeaderState.setHeaderVisible(true);
		TabState.setTabVisible(false);

		$http.get('/questions')
			.then(function(resp) {
				console.log(resp);
				$scope.questions = resp.data;
				$scope.topQn = $scope.questions[$scope.questions.length - 1];
				console.log($scope.questions);
			}, function(resp) {
				console.log(resp);
			});
	};

	$scope.remove = function(index) {
		$scope.questions.splice(index, 1);
		$scope.topQn = $scope.questions[$scope.questions.length - 1];
		$scope.$apply();
	};

	$scope.throwoutleft = function(index, event, obj) {

	};

	$scope.throwoutright = function(index, event, obj) {

	};

	$scope.dragmove = function(event, obj) {
		var dir = obj.throwDirection;
		var prox = obj.throwOutConfidence;

		if (dir === 1) {
			// right
			$scope.leftProx = 0;
			$scope.rightProx = prox;
		} else {
			// left
			$scope.rightProx = 0;
			$scope.leftProx = prox;
		}

		$scope.$apply();
	};

	$scope.dragend = function(event, obj) {
		$scope.leftProx = 0;
		$scope.rightProx = 0;
		$scope.$apply();
	};

	$scope.skip = function(qn) {

	};

	$scope.report = function(qn) {

	};

    $scope.options = {
        throwOutConfidence: function (offset, elementWidth) {
            return Math.min(Math.abs(offset) / 200, 1);
        },
        isThrowOut: function (offset, elementWidth, throwOutConfidence) {
            //console.log('isThrowOut', offset, elementWidth, throwOutConfidence);
            return throwOutConfidence === 1;
        }
    };

    init();
});

app.controller('MeController', function($scope, HeaderState, TabState) {
	var init = function() {
		HeaderState.setHeaderVisible(false);
		TabState.setTabVisible(false);
	};
	init();
});

app.controller('MyQuestionsController', function($scope) {

});

app.controller('MyAnswersController', function($scope) {

});

app.controller('NewQuestionController', function($scope, $http, $location, HeaderState) {
	var init = function() {
		HeaderState.setHeaderVisible(false);
	};

	$scope.question = {};
	$scope.error = '';

	$scope.goBack = function() {
		$location.path('/#/');
	};

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
		$http.post('/questions/', question)
			.then(function(resp) {
				console.log(resp);
			}, function(resp) {
				console.log(resp);
			});
	};

	init();
});

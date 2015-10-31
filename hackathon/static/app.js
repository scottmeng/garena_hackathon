'use static';

var app = angular.module('LoR', ['ngRoute', 'gajus.swing']);

app.constant('VAL_ANW', {
	ANW_LEFT: 1,
	ANW_RIGHT: 2,
	ANW_SKIP: 3,
	ANW_REPORT: 4
});

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
		test: false,
		title: null
	};
	return {
		getHeaderState: function() {
			return HeaderState;
		},
		setHeaderVisible: function(visible, title) {
			HeaderState.isHeaderVisible = visible;
			HeaderState.title = title;
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

app.controller('HomeController', function($scope, $rootScope, $http, HeaderState, TabState, VAL_ANW) {
	$scope.questions = [];
	$scope.topQn = null;
	$scope.leftProx = 0;
	$scope.rightProx = 0;
	$scope.error = null;

	$scope.colors = [{
		selection: '#7D1935',
		border: '#4A96AD',
		txtBg: '#6FC3DC',
		bg: '#F5F3EE'
	}];

	$rootScope.bgColor = $scope.colors[0].bg;
	$rootScope.allowPadding = false;

	var init = function() {
		HeaderState.setHeaderVisible(false, null);
		TabState.setTabVisible(false);

		$http.get('/me')
			.then(function(resp) {
				$scope.user = resp.data;
			});

		getQuestions();
	};


	var getQuestions = function() {
		$http.get('/questions')
			.then(function(resp) {
				$scope.questions = resp.data;
				$scope.topQn = $scope.questions[$scope.questions.length - 1];
				console.log($scope.questions);
			}, function(resp) {
				console.log(resp);
			});
	};

	var updateAnswer = function(index, anw) {
		var qn = $scope.questions[index];
		$scope.questions.splice(index, 1);
		$scope.topQn = $scope.questions[$scope.questions.length - 1];

		if ($scope.questions.length === 0) {
			getQuestions();
		}

		var data = {
			'answer': anw
		};
		console.log(data);
		$http.post('/answers/' + qn.id + '/', data)
		.then(function(resp) {}, function(resp) {
			$scope.error = "network error! please try again later";
			console.log('updateAnswer', 'failed to update answer');
		});
	};

	$scope.throwoutleft = function(index, event, obj) {
		console.log(VAL_ANW);
		console.log
		updateAnswer(index, VAL_ANW.ANW_LEFT);
	};

	$scope.throwoutright = function(index, event, obj) {
		var qn = $scope.questions[index];
		updateAnswer(index, VAL_ANW.ANW_RIGHT);
	};

	$scope.dragstart = function(event, obj) {
		$scope.error = null;
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
		var index = $scope.questions.indexOf(qn);
		updateAnswer(index, VAL_ANW.ANW_SKIP);
	};

	$scope.report = function(qn) {
		var index = $scope.questions.indexOf(qn);
		updateAnswer(qn.id, VAL_ANW.ANW_REPORT);
	};

    $scope.options = {
        throwOutConfidence: function (offset, elementWidth) {
            return Math.min(Math.abs(offset) / 120, 1);
        },
        isThrowOut: function (offset, elementWidth, throwOutConfidence) {
            return throwOutConfidence === 1;
        }
    };

    init();
});

app.controller('MeController', function($scope, $rootScope, $http, HeaderState, TabState) {
	$scope.uniqueness = {};

	var init = function() {
		HeaderState.setHeaderVisible(true, 'Unique Me');
		TabState.setTabVisible(true);
		TabState.setTabSelection(0);
		$rootScope.bgColor = '#FFF';
		$rootScope.allowPadding = true;

		$http.get('/me')
			.then(function(resp) {
				$scope.user = resp.data;
				$scope.uniqueness.percentage = resp.data.uniqueness * 100;
				console.log(resp.data);

				if ($scope.uniqueness.percentage > 90) {
					$scope.uniqueness.label = 'Wow! You are more mysterious than unicorn!';
				} else if ($scope.uniqueness.percentage > 70) {
					$scope.uniqueness.label = 'A dragon you should be! Few have ever seen your trace.';
				} else if ($scope.uniqueness.percentage > 50) {
					$scope.uniqueness.label = 'You are just like a vampire - living in the society yet hard to spot.';
				} else if ($scope.uniqueness.percentage > 30) {
					$scope.uniqueness.label = 'Just like the Yetis, you live in a distant world.';
				} else {
					$scope.uniqueness.label = 'You are a perfectly normal human being and that shall be your uniqueness!';
				}
				console.log($scope.user);
			});
	};
	init();
});

app.controller('MyQuestionsController', function($scope, $rootScope, $http, HeaderState, TabState) {
	var init = function() {
		HeaderState.setHeaderVisible(true, 'My Questions');
		TabState.setTabVisible(true);
		TabState.setTabSelection(1);
		$rootScope.bgColor = '#FFF';
		$rootScope.allowPadding = true;

		$http.get('/questions/me/')
			.then(function(resp) {
				console.log(resp);
				$scope.questions = resp.data;
			});
	};
	init();
});

app.controller('MyAnswersController', function($scope, $rootScope, $http, HeaderState, TabState) {
	var init = function() {
		HeaderState.setHeaderVisible(true, 'My Answers');
		TabState.setTabVisible(true);
		TabState.setTabSelection(2);
		$rootScope.bgColor = '#FFF';
		$rootScope.allowPadding = true;

		$http.get('/answers')
			.then(function(resp) {
				console.log(resp);
				$scope.answers = resp.data;
			});
	};
	init();
});

app.controller('NewQuestionController', function($scope, $rootScope, $http, $location, HeaderState, TabState) {
	var init = function() {
		HeaderState.setHeaderVisible(true, 'Create Question');
		TabState.setTabVisible(false);
		$rootScope.bgColor = '#FFF';
		$rootScope.allowPadding = true;
	};

	$scope.question = {
		left: 'No',
		right: 'Yes'
	};
	$scope.error = null;

	$scope.goBack = function() {
		$location.path('/#/');
	};

	$scope.uploadQuestion = function(body, left, right) {
		$scope.error = '';

		if (!body) {
			$scope.error = 'Question body cannot be empty';
			return;
		} else {
			body = body.trim().replace(/[\"\'\\]/g, '');
			console.log(body);
			if (body === '') {
				$scope.error = 'Question body cannot be empty';
				return;
			}
		}

		if (!left) {
			$scope.error = 'Left answer cannot be empty';
			return;
		} else {
			left = left.trim().replace(/[\"\'\\]/g, '');
			if (left === '') {
				$scope.error = 'Left answer cannot be empty';
				return;
			}
		}

		if (!right) {
			$scope.error = 'Right answer cannot be empty';
			return;
		} else {
			right = right.trim().replace(/[\"\'\\]/g, '');
			if (right === '') {
				$scope.error = 'Right answer cannot be empty';
				return;
			}
		}

		var question = {
			question: body,
			left: left,
			right: right
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

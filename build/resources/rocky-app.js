/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

	module.exports = __webpack_require__(1);


/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

	var rocky = __webpack_require__(2);

	var timeoutID;

	var init = false,
	    stageWidth,
	    stageHeight,
	    centerx,
	    centery,
	    ctx

	var leftwidth, rightwidth;
	// 缓存黄金分隔计算结果

	var point;
	var numbers = 40;
	// 粒子点集与生成数

	var flag_time = true;
	// 是否更新时间

	function generatePoints() {
	    // 生成点集
	    point = [];
	    for (var i = 0; i < numbers; i++) {
	        point.push({
	                length: 20 + Math.floor(Math.random() * ((stageWidth - 20) / 2)),
	                deg: Math.PI / 180 * (Math.random() * 90 - Math.random() * 90),
	                offset: Math.random()
	            })
	            // 极坐标
	    }
	}

	rocky.on('draw', function(event) {
	    if (!init) {
	        ctx = event.context;
	        // 缓存Canvas上下文
	        stageWidth = ctx.canvas.clientWidth;
	        stageHeight = ctx.canvas.clientHeight;
	        centerx = stageWidth / 2;
	        centery = stageHeight / 2;
	        // 缓存舞台信息

	        leftwidth = Math.floor(stageWidth * 0.618);
	        rightwidth = stageWidth - Math.floor(stageWidth * 0.618);

	        init = true;
	        // 初始化完成
	    }

	    ctx.fillStyle = "white";
	    ctx.clearRect(leftwidth, 0, rightwidth, stageHeight);
	    // 重绘舞台

	    if (flag_time) {
	        ctx.clearRect(0, 0, ctx.canvas.clientWidth, ctx.canvas.clientHeight);

	        ctx.fillRect(0, 0, leftwidth, stageHeight);
	        // 绘制背景

	        var d = new Date();

	        var hours = d.getHours();
	        if (hours < 10) {
	            hours = "0" + hours;
	        }
	        var minutes = d.getMinutes();
	        if (minutes < 10) {
	            minutes = "0" + minutes;
	        }

	        var size = ctx.measureText(hours);
	        ctx.fillStyle = "folly";
	        ctx.textAlign = "center";
	        ctx.font = "42px bold numbers Leco-numbers";

	        var textarea = 60;
	        // 文字区域宽度
	        var xplace = 70;
	        var yplace = stageHeight / 2 - 20;
	        // 绘制坐标

	        var padding = 15;
	        ctx.fillText(hours, xplace, yplace - size.height - padding, textarea);
	        ctx.fillText(minutes, xplace, yplace + padding, textarea);

	        flag_time = false;
	    }


	    if (point == undefined) {
	        generatePoints();
	    }
	    for (var i in point) {
	        var p = point[i];
	        ctx.fillRect(leftwidth + p.length * Math.cos(p.deg), centery + p.length * Math.sin(p.deg), 2, 2);
	    }

	});

	rocky.on("secondchange", function() {
	    for (var i in point) {
	        point[i].deg += 0.2 * point[i].offset;
	        var deg = 180 / Math.PI * point[i].deg;
	        if (deg > 90) {
	            point[i].deg = Math.PI / 180 * -90;
	        }
	    }
	    rocky.requestDraw();
	})

	rocky.on("minutechange", function() {
	    flag_time = true;
	});

	rocky.on('hourchange', function(event) {
	    if (init) {
	        generatePoints();
	    }
	});

/***/ }),
/* 2 */
/***/ (function(module, exports) {

	module.exports = _rocky;


/***/ })
/******/ ]);
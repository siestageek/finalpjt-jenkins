var express = require('express');
var path = require('path');
var nunjucks = require('nunjucks');  // Nunjucks를 추가합니다.
var port = 3000
const promBundle = require('express-prom-bundle');
const metricsMiddleware = promBundle({includeMethod: true, includePath: true});

var app = express();
app.use(metricsMiddleware);

// Nunjucks 템플릿 엔진 설정
nunjucks.configure('views', { // 'views'는 Nunjucks 템플릿 파일들이 위치할 폴더입니다.
  autoescape: true,
  express: app
});

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

// 메인 페이지 라우트 예제 추가
app.get('/', function (req, res){
  res.render('index.html', { title: 'Welcome to Nunjucks' });  // index.html을 렌더링하고, 변수 전달
});

app.get('/api', function (req, res){
  res.json({message: 'Hello, World!!'})
});

// 서버 시작
app.listen(port, () => {
  console.log(`Frontend server on port ${port}`)
});

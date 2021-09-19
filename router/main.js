
var fs = require('fs');

module.exports = function(app) {
  app.get('/input', (req, res) => {
    res.render('input.html');
  })

  app.get('/crawl', (req, res) => {
    var prname = req.query.prname;
    var srname = req.query.srname;
    const spawn = require('child_process').spawn;
    const result = spawn('python', ['main.py', prname, srname]);
    var msg = '';
    result.stdout.on('data', function(data) {
        msg = data.toString();
        console.log(msg);
        const words = msg.split(' | ');
        console.log(words[0]);
        //console.log(words[1]);
        //console.log(msg);
        fs.readdir('./data', function(err,filelist) {
          var template = `
          <!doctype html>
          <html lang="en" class="h-100">
            <head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <meta name="description" content="">
              <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
              <meta name="generator" content="Hugo 0.88.1">
              <title>Cover Template · Bootstrap v5.1</title>

              <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/cover/">



              <!-- Bootstrap core CSS -->
          <link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">

              <style>
                .bd-placeholder-img {
                  font-size: 1.125rem;
                  text-anchor: middle;
                  -webkit-user-select: none;
                  -moz-user-select: none;
                  user-select: none;
                }

                @media (min-width: 768px) {
                  .bd-placeholder-img-lg {
                    font-size: 3.5rem;
                  }
                }
              </style>


              <!-- Custom styles for this template -->
              <link href="cover.css" rel="stylesheet">
            </head>
            <body class="d-flex h-100 text-center text-white bg-dark">

          <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
            <header class="mb-auto">
              <div>
                <h3 class="float-md-start mb-0">네이버 쇼핑 상품 찾기</h3>
                <nav class="nav nav-masthead justify-content-center float-md-end">
                  <a class="nav-link" href="/profile">Home</a>
                  <a class="nav-link active" aria-current="page" href="/input">페이지 검색</a>
                </nav>
              </div>
            </header>

            <main class="px-3">
              <h1>네이버 스마트스토어<br>페이지 검색 결과</h1>
              <p class="lead">
                <p class = "srresult">
                  상품이름: ${prname}<br>
                  검색 키워드: ${srname}<br>
                  위치: ${words[0]}페이지 ${words[1]}번째<br>
                </p>
              <p class="lead">
                <a href="/input" class="btn btn-lg btn-secondary fw-bold border-white bg-white">다시 검색</a>
              </p>
            </main>

            <footer class="mt-auto text-white-50">
              <p>Naver shopping product searcher, by <a href="https://github.com/legozoa" class="text-white" target='_blank'>Legozoa</a>.</p>
            </footer>
          </div>
            </body>
          </html>
          `;
          res.end(template);
        })
    });
    result.stderr.on('data', function(data) {
        msg = data.toString();
            //console.log(msg);
    });

  })

  app.get('/profile', (req, res) => {
    res.render('main.html');
  })

}

import React from 'react'
import { renderToString } from 'react-dom/server'
import App from './App'
import http from "http";
import cors from 'cors';
import { StaticRouter } from 'react-router-dom';

import process from "process";
import express from 'express';

const app  = express()
app.use(cors());
app.use(express.static("public"));
app.get('*.js', (req, res, next) => {
    req.url = req.url + '.br';
    res.set('Content-Encoding', 'br');
    next();
  });

app.get('**', (req, res) => {
    const markup = renderToString(
        <StaticRouter location={req.url} context={null}>
          <App />
        </StaticRouter>,
      );
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="M-Uwezo App">
    <meta name="keywords" content="M-Uwezo App">
    <meta name="author" content="Anthony Leiro">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>M-Uwezo App</title>
    <script defer type="text/javascript" src="bundle.js"></script>
    <link rel="manifest" href="manifest.json" />
    <link rel="stylesheet" type="text/css" href="main.bundle.css">
</head>
<body>
    <div id="app">${markup}</div>
</body>
</html>
    `
    res.set('Cache-Control', 'public, max-age=600, s-maxage=1200', 'Content-Encoding', 'brotli')
    res.send(html)
})

const port = process.env.PORT || 5000;

const server = http.createServer(app);

try {
  server.listen(port);
  server.on("listening", () => {
    console.log(`server started on ::${port}`);
  });
} catch (error) {
  console.log(error);
}

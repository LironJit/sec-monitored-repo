const express = require('express');
const vm = require('vm');

const app = express();

app.get('/', (req, res) => {
  const script = new vm.Script(req.query.script);
  script.runInThisContext();
});

app.listen(3000);

const express = require('express')
// import { spawn } from "child_process";
const app = express()
const port = 8081

app.get('/deploy_components', (req,res) => {
  const {spawn} = require('child_process');

  const child = spawn('docker', ['build','.','-t','test','-f','../Components/edge_detection/Dockerfile']);

  child.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
  });

  child.stderr.on('data', (data) =>{
      console.log(`stderr: ${data}`);
  });

  child.on('error', (error) => console.log(`error ${error.message}`));

  child.on('exit', (code,signal) =>{
    if(code) console.log(`Code: ${code}`);
    if(signal) console.log(`Code: ${signal}`); 
    console.log('Done!');

  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
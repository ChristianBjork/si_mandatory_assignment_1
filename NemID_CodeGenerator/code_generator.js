//Written by Christian Bjørk Christiansen

const express = require('express');
const sqlite3 = require('sqlite3');
const axios = require('axios');

var db = new sqlite3.Database('../NemID_ESB/nem_id_database.sqlite');
var app = express();

app.use(express.json());

app.post('/nemid-auth', ( req, res ) => {
    console.log("nemIdCode: " + req.body.nemIdCode);
    console.log("nemId: " + req.body.nemId);

    let nemIdCode = req.body.nemIdCode;
    let nemId = req.body.nemId;

    let generatedCode = Math.floor(Math.random() * 900000) + 100000;

    if (nemIdCode + nemId == "dataFromDB"){
        res.status(200).send({generatedCode: generatedCode})
    } else {

    }
})

//Test that server is up and running
app.get('/test', (req, res) => {
    res.status(200).send({ message: "Server is running just fine on port 8090... " })
});

app.listen(8089, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log("Listening on port 8090");
    }
});
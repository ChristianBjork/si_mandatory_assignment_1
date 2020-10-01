//Written by Christian Bjørk Christiansen
const express = require('express');

var app = express();

app.use(express.json());

app.post('/generate-password-nemID', async (req, res) => {
    console.log("nemId: " + req.body.nemId);
    console.log("cpr: " + req.body.cpr);

    let nemId = req.body.nemId;
    let cpr = req.body.cpr;

    let nemIdPassword = nemId.substr(0, 2) + cpr.substr(cpr.length - 2);
    console.log(nemIdPassword)
    res.status(200).send({ nemIdPassword: nemIdPassword })
});

//Test that server is up and running
app.get('/test', (req, res) => {
    res.status(200).send({ message: "Server is running just fine on port 8089... " })
});

app.listen(8089, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log("Listening on port 8089");
    }
});
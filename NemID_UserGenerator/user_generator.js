//Written by lasse Emil Poulsen & Christian Bjørk Christiansen

const express = require('express');
//var bodyParser = require('body-parser');

var app = express();

app.use(express.json());
// app.use(bodyParser.urlencoded({
//     extended: true
// }));

app.post('/generate-nemId', (req, res) => {
    console.log("Got response: " + res.statusCode);
    console.log("req", req.body.email)
    console.log("req", req.body.cpr)

    let cpr = req.body.cpr;
    
    let last_4_digits_of_CPR = cpr.substr(cpr.length - 4);
    let random_5_digit_number = Math.floor(Math.random() * 90000) + 10000;
    let nemId = random_5_digit_number + last_4_digits_of_CPR
    res.status(201).send({ nemID: nemId });
});


//Test that server is up and running
app.get('/test', (req, res) => {
    res.status(200).send({ message: "Server is running just fine on port 8088... " })
});


app.listen(8088, (err) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log("Listening on port 8088");
    }
});
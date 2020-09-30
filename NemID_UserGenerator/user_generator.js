const express = require('express');

var app = express();

app.use(express.json());

//Test that server is up and running
app.get('/test', (req, res) =>{
    res.status(200).send({message: "Server is running just fine on port 8088... "})
});


app.post('/generate-nemId', async(req, res) =>{
    console.log("Got response: " + res.statusCode);
    let cpr = req.body.cpr
    // let last_4_digits_of_CPR = cpr.substr(cpr.length - 4);
    // let random_5_digit_number = Math.floor(Math.random() * 10000)
    // let nemId = random_5_digit_number + last_4_digits_of_CPR
    // res.status(200).send({nemID: nemId});
    // res.status(200).send('Hello World');
    res.status(200).send(cpr)

} )


app.listen(8088, (err) => {
    if(err){
        console.log(err);
    }
    else{
        console.log("Listening on port 8088");
        console.log("ESB is configured...");
    }
});
const express = require("express");
const bodyParser = require("body-parser");
var sql = require("mssql");

const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));

app.get("/",function(req,res) {
  res.sendFile(__dirname+"/index.html");
});

const config = {
        user: 'admin',
        password: 'UQ19-XPN',
        server: 'neo4j-metadata.cjwdtb9o2fdi.us-east-1.rds.amazonaws.com',
        database: 'Metadata'
    };

app.get("/domain",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from Domain', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})

app.get("/dmnrel",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from DomainRelationship', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})

app.get("/BsnTms",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from BusinessTerms', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})

app.get("/TechTerms",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from TechnicalTerms', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})

app.get("/dtr",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from DomainTermsRelationship', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})

app.get("/btt",function(request,response){


      sql.connect(config, function (err) {

        if (err) console.log(err);

        // create Request object
        var request = new sql.Request();

        // query to the database and get the records
        request.query('select * from TechBusBridge', function (err, recordset) {

            if (err) console.log(err)
            // send records as a response
            response.send(recordset);

        });
    });

})






app.listen(process.env.PORT || 3000, function() {
  console.log("sever started on port 3000......")
});

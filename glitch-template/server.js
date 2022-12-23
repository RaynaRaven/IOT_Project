"use strict";

const express = require("express");
const logger = require("./utils/logger");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const fileUpload = require("express-fileupload");
const Items = require("./config.js");

const app = express();
app.use(cookieParser());
const exphbs = require("express-handlebars");
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static("public"));
app.use(fileUpload());
app.engine(
  ".hbs",
  exphbs({
    extname: ".hbs",
    defaultLayout: "main"
  })
);
app.set("view engine", ".hbs");
app.post("/create", async(req,res)=>{
    const data=req.body;
    console.log("Data of Users",data);
    await Items.push(data);
    res.send({msg:"Item Added"})
})

app.listen(3000, ()=>console.log("Up & Running *3000"))
const routes = require("./routes");
app.use("/", routes);

const listener = app.listen(process.env.PORT || 4000, function() {
  logger.info(`foodSaver started on port ${listener.address().port}`);
});

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

const mongoURI = `mongodb+srv://admin:aayush@mernstackapp.9r7ujgx.mongodb.net/`;
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => console.log("MongoDB connected"))
    .catch(err => console.error(err));
app.get("/", (req, res) => res.send("Hello World! Aayu....."));
app.get("/name", (req, res) => res.send("Hello from express! My name is Aayush Singh"));

app.listen(5000, () => console.log("Server running on port 5000"));
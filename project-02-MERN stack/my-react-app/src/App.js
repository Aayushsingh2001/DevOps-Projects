import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect (() => {
    axios
      .get("http://localhost:5321/")
      .then((res) => setMessage(res.data))
      .catch((err) => setMessage("Error fetching data"));
  }, [])

  return(
    <div style={{ textAlign: "center", marginTop: "50px"}}>
      <h1>API Response:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
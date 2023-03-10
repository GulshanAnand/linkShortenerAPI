const url = "http://127.0.0.1:5000/shorten";
const data = {
  url: "https://www.python.org",
  alias: "hello"
};

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

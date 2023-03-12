const url = "https://labwired.tech/shorten";
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

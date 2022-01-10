const axios = require('axios');
const apiKey = require('./config');
axios.get('http://api.openweathermap.org/data/2.5/weather?q=Madurai&appid='+apiKey)
  .then(response => {
    console.log("It's "+response.data.weather[0].main + ": "+response.data.weather[0].description);
    console.log("temperature: "+response.data.main.temp);
    console.log("pressure: "+response.data.main.pressure);
    console.log("humidity: "+response.data.main.humidity);
  })
  .catch(error => {
    console.log(error);
  });
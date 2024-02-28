fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
      $('#hello').text(data.hello);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

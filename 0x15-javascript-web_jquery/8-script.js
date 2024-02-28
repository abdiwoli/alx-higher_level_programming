fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(item => {
      $('#list_movies').append('<li>' + item.title + '</li>');
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });

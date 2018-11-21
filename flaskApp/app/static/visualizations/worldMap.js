function displayWorldMap() {
  Plotly.d3.csv("/static/florence.csv", function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
      }
  var data = [{
    type: 'choropleth',
    locationmode: 'country names',
    locations: unpack(rows, 'Country'),
    z: unpack(rows, 'Mentions'),
    text: unpack(rows, 'Country'),
    autocolorscale: true
  }];
  var layout = {
    title: 'Mentions associated with the event in this year',
    geo: {
        projection: {
            type: 'Mercator'
          }
        }
  };
  Plotly.plot(worldMapDisp, data, layout, {showLink: false});
  });
}

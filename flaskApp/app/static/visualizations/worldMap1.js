function displayWorldMap1(mapPath1)  {
  var width = 500,
    height = 500;

  var projection = d3.geo.mercator()
    .scale(width/2/Math.PI)
    .translate([width/2,height/2]);


  var svg1 = d3.select("#worldMapDisp1").append('svg')
    .attr("width", width)
    .attr("height", height)
    .style("background-color", 'white');

  var path = d3.geo.path()
    .projection(projection);

  var g = svg1.append("g");
  var scalefactor=1./14. ;

  d3.json("/static/worlddata.json", function(error, topology) {
    d3.csv(mapPath1, function(error, data) {
    g.selectAll("circle")
       .data(data)
       .enter()
       .append("circle")
       .attr("cx", function(d) {
          return projection([d.Longitude, d.Latitude])[0];
       })
       .attr("cy", function(d) {
          return projection([d.Longitude, d.Latitude])[1];
       })
       .attr('fill','steelblue')
       .attr('fill-opacity', .6)
       .attr("r", function(d) { return (d.radius)*4; })
       .on("mouseover", function(d) {
          d3.select(this).style("fill", "#FC0");
          var xPosition = projection([d.Longitude, d.Latitude])[0] ;
          var yPosition = projection([d.Longitude, d.Latitude])[1];
          g.append("text")
            .attr("id", "hoverLabel")
            .attr("x", xPosition)
            .attr("y", yPosition)
            .attr("text-anchor", "start")
            .attr("font-family", "ff-nuvo-sc-web-pro-1,ff-nuvo-sc-web-pro-2, sans-serif")
            .attr("font-size", "20px")
            .attr("fill", "black")
            .text(d.Country);
        })
        .on("mouseout", function(d) {
          d3.select(this).style("fill","steelblue");
          d3.select("#hoverLabel").remove();
        });
    g.selectAll("text")
      .data(data)
      .enter()
      .append("text")
      .attr("x", function(d) {
        return projection([d.Longitude, d.Latitude])[0];
       })
      .attr("y", function(d) {
        return projection([d.Longitude, d.Latitude])[1];
       })
      .attr("dy", -7)
      .style("fill", "black")
      .attr("text-anchor", "middle")
      .attr("font-size", "12px")
      .text(function(d) {return d.Mentions;})
  });
    g.selectAll("path")
      .attr("class", "countries")
      .data(topojson.object(topology, topology.objects.countries).geometries)
      .enter()
      .append("path")
      .attr("d", path)
      .attr("stroke", "white")
      .attr("stroke-width", "0.27px")
      .attr("fill", "grey")
  });
}

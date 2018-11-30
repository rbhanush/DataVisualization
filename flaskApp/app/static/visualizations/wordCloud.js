function displayWordCloud (frequency_list) {
  var color = d3.scale.linear()
                .domain([1,3,10,20,50])
                .range(["#66c2a5","#fc8d62","#8da0cb","#e78ac3","#a6d854"]);

  d3.layout.cloud().size([800, 300])
          .words(frequency_list)
          .rotate(0)
          .fontSize(function(d) { return d.size; })
          .on("end", draw)
          .start();

  function draw(words) {
      d3.select("#wordCloudDisp").append("svg")
              .attr("width", 850)
              .attr("height", 350)
              .attr("class", "wordcloud")
              .append("g")
              .attr("transform", "translate(320,200)")
              .selectAll("text")
              .data(words)
              .enter().append("text")
              .style("font-size", function(d) { return d.size + "px"; })
              .style("fill", function(d, i) { return color(i); })
              .attr("transform", function(d) {
                  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
              })
              .text(function(d) { return d.text; })
              .on("mouseover", function(){d3.select(this).style("font-size", "2.5em");})
              .on("mouseout", function(d){d3.select(this).style("font-size", d.size + "px");});
  }
}

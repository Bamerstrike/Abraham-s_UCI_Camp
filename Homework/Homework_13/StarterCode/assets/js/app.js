// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height",svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

var chooseXAxis = "Healthcare";
var chooseYAxis = "Poverty";

function xScale(data,chooseXAxis){
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(data, d=> d[chooseXAxis])*0.8],[d3.max(data, d=> d[chooseXAxis])*1.2])
        .range([0,width]);

    return xLinearScale;
}

function yScale(data,chooseYAxis){
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(data, d=> d[chooseYAxis])*0.8],[d3.max(data, d=> d[chooseYAxis])*1.2])
        .range([0,width]);

    return xLinearScale;
}
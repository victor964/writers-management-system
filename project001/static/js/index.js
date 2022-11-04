// // Graph
// var ctx = document.getElementById("myChart");

// var myChart = new Chart(ctx, {
//   type: "line",
//   data: {
//     labels: [
//       "Sunday",
//       "Monday",
//       "Tuesday",
//       "Wednesday",
//       "Thursday",
//       "Friday",
//       "Saturday",
//     ],
//     datasets: [
//       {
//         data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
//         lineTension: 0,
//         backgroundColor: "transparent",
//         borderColor: "#007bff",
//         borderWidth: 4,
//         pointBackgroundColor: "#007bff",
//       },
//     ],
//   },
//   options: {
//     scales: {
//       yAxes: [
//         {
//           ticks: {
//             beginAtZero: false,
//           },
//         },
//       ],
//     },
//     legend: {
//       display: false,
//     },
//   },
// });

// var header = document.getElementById("myDIV");
// var btns = header.getElementsByClassName("list-group-item");
// for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function() {
//         var current = document.getElementsByClassName("active");
//         current[0].className = current[0].className.replace(" active", "");
//         this.className += " active";
//     });
// }
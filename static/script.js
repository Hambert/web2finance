
  var requestURL = "/api";

  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          fillTable(jsonData=this.responseText);
      }
  };
  xmlhttp.open("GET", requestURL, true);
  xmlhttp.send();

    function fillTable(jsonData){
        // (B) PARSE THE JSON STRING INTO OBJECT FIRST
        //var data = '{"cnn_fug_now": {"value": 48.0, "sourceDate": "2021-02-26T17:04:00"}, "btc_fug_now": {"value": 56.0, "sourceDate": "2021-02-27T15:25:32.01939"}}';
      data = JSON.parse(jsonData);
        // console.table(data);
        

      var table = document.getElementById("fugTable")

      for (let key in data) {
        var d = new Date(data[key]["sourceDate"]);

        if (key=="cnn_fug_now"){
          document.getElementById("fug_cnn").innerHTML = data[key]["value"];
          gauge.set(data[key]["value"]);
          document.getElementById("fug_cnnDate").innerHTML = d.toLocaleString();
        } else if (key=="btc_fug_now"){
          document.getElementById("fug_crypto").innerHTML = data[key]["value"];
          gauge2.set(data[key]["value"]);
          document.getElementById("fug_cryptoDate").innerHTML = d.toLocaleString();;
        }
      }
    }

  /////// gauge

  var opts = {
      angle: 0, // The span of the gauge arc
      lineWidth: 0.29, // The line thickness
      radiusScale: 0.86, // Relative radius
      pointer: {
        length: 0.53, // // Relative to gauge radius
        strokeWidth: 0.046, // The thickness
        color: '#000000' // Fill color
      },
      limitMax: false,     // If false, max value increases automatically if value > maxValue
      limitMin: false,     // If true, the min value of the gauge will be fixed
      colorStart: '#6FADCF',   // Colors
      colorStop: '#8FC0DA',    // just experiment with them
      strokeColor: '#E0E0E0',  // to see which ones work best for you
      generateGradient: true,
      highDpiSupport: true,     // High resolution support
      
    };
    var target = document.getElementById('fug_cnnCanvas'); // your canvas element
    var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge.setTextField(document.getElementById("fug_cnnGauge"));
    gauge.maxValue = 100; // set max gauge value
    gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 10; // set animation speed (32 is default value)
    

    target = document.getElementById('fug_cryptoCanvas'); // your canvas element
    var gauge2 = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge2.setTextField(document.getElementById("fug_cryptoGauge"));
    gauge2.maxValue = 100; // set max gauge value
    gauge2.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge2.animationSpeed = 10; // set animation speed (32 is default value)

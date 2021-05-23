<template>
  <div>
    <h1 style="font-size: 20px; margin-top: 20px; margin-left: 40px">
      图形展示
    </h1>
    <div id="chart" style="width: 100%; height: 550px"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  data() {
    return {
      legend: [
        "AQI",
        "PM25",
        "PM25_24h",
        "PM10",
        "PM10_24h",
        "SO2",
        "SO2_24h",
        "NO2",
        "NO2_24h",
        "O3",
        "O3_24h",
        "O3_8h",
        "O3_8h_24h",
        "CO",
        "CO_24h",
      ],
      time: 0,
      date: [],
      AQI: [],
      PM25: [],
      PM25_24h: [],
      PM10: [],
      PM10_24h: [],
      SO2: [],
      SO2_24h: [],
      NO2: [],
      NO2_24h: [],
      O3: [],
      O3_24h: [],
      O3_8h: [],
      O3_8h_24h: [],
      CO: [],
      CO_24h: [],
      chosenSensor: this.$store.state.chosenSensor,
    };
  },
  methods: {
    drawChart() {
      var chartDom = document.getElementById("chart");
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: this.legend,
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: this.date,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            name: "AQI",
            type: "line",
            stack: "总量",
            data: this.AQI,
          },
          {
            name: "PM25",
            type: "line",
            stack: "总量",
            data: this.PM25,
          },
          {
            name: "PM25_24h",
            type: "line",
            stack: "总量",
            data: this.PM25_24h,
          },
          {
            name: "PM10",
            type: "line",
            stack: "总量",
            data: this.PM10,
          },
          {
            name: "PM10_24h",
            type: "line",
            stack: "总量",
            data: this.PM10_24h,
          },
          {
            name: "SO2",
            type: "line",
            stack: "总量",
            data: this.SO2,
          },
          {
            name: "SO2_24h",
            type: "line",
            stack: "总量",
            data: this.SO2_24h,
          },
          {
            name: "NO2",
            type: "line",
            stack: "总量",
            data: this.NO2,
          },
          {
            name: "NO2_24h",
            type: "line",
            stack: "总量",
            data: this.NO2_24h,
          },
          {
            name: "O3",
            type: "line",
            stack: "总量",
            data: this.O3,
          },
          {
            name: "O3_24h",
            type: "line",
            stack: "总量",
            data: this.O3_24h,
          },
          {
            name: "O3_8h",
            type: "line",
            stack: "总量",
            data: this.O3_8h,
          },
          {
            name: "O3_8h_24h",
            type: "line",
            stack: "总量",
            data: this.O3_8h_24h,
          },
          {
            name: "CO",
            type: "line",
            stack: "总量",
            data: this.CO,
          },
          {
            name: "CO_24h",
            type: "line",
            stack: "总量",
            data: this.CO_24h,
          },
        ],
      };

      option && myChart.setOption(option);
    },
    getYearValue() {
      var param = this.chosenSensor;
      this.chosenSensor = this.$store.state.chosenSensor;
      if (param != this.chosenSensor) {
        this.time++;
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "AQI",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.AQI = res.data.AQI;
            this.date = res.data.date;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "PM2.5",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.PM25 = res.data["PM2.5"];
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "PM2.5_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.PM25_24h = res.data["PM2.5_24h"];
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "PM10",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.PM10 = res.data.PM10;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "PM10_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.PM10_24h = res.data.PM10_24h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "SO2",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.SO2 = res.data.SO2;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "SO2_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.SO2_24h = res.data.SO2_24h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "NO2",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.NO2 = res.data.NO2;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "NO2_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.NO2_24h = res.data.NO2_24h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "O3",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.O3 = res.data.O3;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "O3_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.O3_24h = res.data.O3_24h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "O3_8h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.O3_8h = res.data.O3_8h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "O3_8h_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.O3_8h_24h = res.data.O3_8h_24h;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "CO",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.CO = res.data.CO;
          });
        this.axios
          .get("/api/getYearValue", {
            params: {
              site_id: this.$store.state.chosenSensor,
              name: "CO_24h",
            },
          })
          .then((res) => {
            console.log(res.data);
            this.CO_24h = res.data.CO_24h;
          });
      }
    },
    update() {
      this.getYearValue();
      this.drawChart()
    },
  },
  mounted: function () {
    window.setInterval(() => {
      setTimeout(this.update(), 0);
    }, 3000);
  },
  watch: {
    time(val, oldVal) {
      //普通的watch监听
      console.log("a: " + val, oldVal);
      this.drawChart();
    },
    PM25: {
      handler(newValue, oldValue) {
        for (let i = 0; i < newValue.length; i++) {
          if (oldValue[i] != newValue[i]) {
            this.drawChart();
            break;
          }
        }
      },
      deep: true,
    },
  },
};
</script>
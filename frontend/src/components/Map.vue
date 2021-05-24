<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="城市选择" name="first">
      <div id="map"></div>
    </el-tab-pane>

    <el-tab-pane label="信息确定" name="second">
      <div style="margin-top: 20px">
        <el-row :gutter="20">
          <el-col :span="6"><div class="grid-content"></div></el-col>
          <el-col :span="6"
            ><div class="grid-content">城市名：{{ city }}</div></el-col
          >
          <el-col :span="6">
            <div class="grid-content">
              <el-select v-model="valueblank" clearable placeholder="监控点选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="6"><div class="grid-content"></div></el-col>
        </el-row>
      </div>

      <div style="margin-top: 20px">
        <el-row :gutter="12">
          <el-col :span="4">
            <div class="grid-content"></div>
          </el-col>
          <el-col :span="16">
            <el-card shadow="always">
              <div class="test item">监控点信息：</div>
              <div class="test item">
                {{ msg }}
              </div>
            </el-card>
          </el-col>
          <el-col :span="4">
            <div class="grid-content"></div>
          </el-col>
        </el-row>
      </div>

      <el-row>
        <el-button
          type="primary"
          plain
          style="margin: 0 auto; display: block"
          @click="confirm"
          >确认</el-button
        >
      </el-row>
    </el-tab-pane>

    <el-tab-pane label="数据呈现" name="third">
      <el-table :data="tableData" :cell-style="style_for_cell" height="250">
        <el-table-column
          fixed
          align="center"
          prop="week"
          label="周次"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="AQI" label="AQI" width="120">
        </el-table-column>
        <el-table-column align="center" prop="PM25" label="PM2.5" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="PM2.5_24h"
          label="PM2.5_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="PM10" label="PM10" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="PM10_24h"
          label="PM10_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="SO2" label="SO2" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="SO2_24h"
          label="SO2_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="NO2" label="NO2" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="NO2_24h"
          label="NO2_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="O3" label="O3" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="O3_24h"
          label="O3_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="O3_8h" label="O3_8h" width="120">
        </el-table-column>
        <el-table-column
          align="center"
          prop="O3_8h_24h"
          label="O3_8h_24h"
          width="120"
        >
        </el-table-column>
        <el-table-column align="center" prop="CO" label="CO_24h" width="120">
        </el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
//import * as d3 from "d3";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

var map;
export default {
  data() {
    return {
      activeName: "first",
      city: "杭州市",
      msg: "经度：东经30.305878°  纬度：北纬120.079637°",
      options: [
        {
          value: "value1",
          label: "紫金港监控点",
        },
        {
          value: "value2",
          label: "玉泉监控点",
        },
        {
          value: "value3",
          label: "西溪监控点",
        },
        {
          value: "value4",
          label: "下沙监控点",
        },
      ],
      valueblank: "",
      rows:[[1,2,3],[1,2,3,4],[1,2,3]],
      tableData: [
        {
          week: "1",
          AQI: "3",
          PM25: "2",
        },
      ],
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    confirm() {
      this.activeName = "third";
    },
    style_for_cell(cell_data){
      // console.log(cell_data)
      return {
        opacity: Number(cell_data.row[cell_data.column.property])/3,
        "background-color": "#000000"
      }
    }
  },
  mounted() {
    map = L.map("map", {
      minZoom: 3,
      maxZoom: 14,
      center: [30.265237, 120.120192],
      zoom: 12,
      zoomSnap:0.1,
      zoomControl: true,
      attributionControl: false,
      touchZoom:true
    });
    this.map = map;
    window.map = map;
    const tileUrl =
      "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY3ktbGx1IiwiYSI6ImNraHZsMGYzYjBnNnMyc28yYXlvd256NnYifQ.TTfaDTXXNPAOAQ6_lqIFEg";
    L.tileLayer(tileUrl, {
      tileSize: 512,
      zoomOffset: -1,
    }).addTo(map);
    L.circle([30.305878, 120.079637],200,{
      color:'red',
      fillColor:'#f03',
      fillOpacity:0.5
    }).addTo(map).bindPopup("紫金港监控点");
    L.circle([30.265237, 120.120192],200,{
      color:'red',
      fillColor:'#f03',
      fillOpacity:0.5
    }).addTo(map).bindPopup("玉泉监控点");
    L.circle([30.2747, 120.063],200,{
      color:'red',
      fillColor:'#f03',
      fillOpacity:0.5
    }).addTo(map).bindPopup("西溪监控点");
    L.circle([30.3058, 120.348],200,{
      color:'red',
      fillColor:'#f03',
      fillOpacity:0.5
    }).addTo(map).bindPopup("下沙监控点");
    
    var popup = L.popup();
    function onMapClick(e){
      popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " +e.latlng.toString())
        .openOn(map);
    }
    map.on('click',onMapClick);

    fetch("test.json")
    .then(res=>{
      console.log(res)
      return res.json()
      })
    .then(data=>{
      console.log(data,this)
      this.tableData=data
      })
  }
};
</script>

<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.el-table td,
.el-table th {
  text-align: center;
}

#map{
  width: 100%;
  height: calc(100vh);
}
.row{

}
.cell{

}
</style>
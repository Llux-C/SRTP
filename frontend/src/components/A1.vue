<template>
<div>
<h1 style="font-size:20px;margin-top:20px;margin-left:40px">地区选择</h1>
<div style="display: flex;justify-content: center;">
  <div style="">
    <a-select :default-value="provinceData[0]" style="width: 120px;margin:10px" @change="handleProvinceChange">
      <a-select-option v-for="province in provinceData" :key="province">
        {{ province }}
      </a-select-option>
    </a-select>
    <a-select v-model="chosenCity" style="width: 120px;margin:10px" @change="handleCityChange">
      <a-select-option v-for="city in cities" :key="city">
        {{ city }}
      </a-select-option>
    </a-select>
    <a-select v-model="chosenSensor" style="width: 120px;margin:10px">
      <a-select-option v-for="sensor in sensors" :key="sensor">
        {{ sensor }}
      </a-select-option>
    </a-select>
    <a-button style="margin:10px">确定</a-button>
  </div>
</div>
</div>
</template>

<script>
const provinceData = ['Zhejiang', 'Jiangsu'];
const cityData = {
  Zhejiang: ['Hangzhou', 'Ningbo', 'Wenzhou'],
  Jiangsu: ['Nanjing', 'Suzhou', 'Zhenjiang'],
};
const sensorData = {
    Hangzhou:['传感器1', '传感器2', '传感器3'],
    Ningbo:['传感器1', '传感器2'],
    Wenzhou:['传感器1', '传感器2', '传感器3', '传感器4'],
    Nanjing:['传感器1'],
    Suzhou:['传感器1', '传感器2'],
    Zhenjiang:['传感器1', '传感器2', '传感器9'],
}
export default {
  data() {
    return {
      provinceData,
      cityData,
      cities: cityData[provinceData[0]],
      chosenCity: cityData[provinceData[0]][0],
      sensors:sensorData[cityData[provinceData[0]][0]],
      chosenSensor:sensorData[cityData[provinceData[0]][0]][0],
      
    };
  },
  methods: {
    handleProvinceChange(value) {
      this.cities = cityData[value];
      this.chosenCity = cityData[value][0];
    },
    handleCityChange(value) {
      this.sensors = sensorData[value];
      this.chosenSensor = sensorData[value][0];
    },
  },
};
</script>
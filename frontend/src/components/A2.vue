<template>
  <div>
    <h1 style="font-size: 20px; margin-top: 20px; margin-left: 40px">
      缺失率数据
    </h1>
    <div style="">
      <div style="">
        <a-table
          :columns="columns"
          :data-source="data"
          :pagination="ipagination1"
          :scroll="{ x: 500 }"
          @change="handleTableChange2"
        >
        </a-table>
      </div>
    </div>
  </div>
</template>

<script>
const columns = [
  {
    title: "周次",
    dataIndex: "week",
    width: "120px",
    fixed: "left",
  },
  {
    title: "AQI",
    dataIndex: "AQI",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.AQI)+")",
        }
      }
    }
  },
  {
    title: "PM2.5",
    dataIndex: "PM25",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.PM25)+")",
        }
      }
    }
  },
  {
    title: "PM2.5_24h",
    dataIndex: "PM25_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.PM25_24h)+")",
        }
      }
    }
  },
  {
    title: "SO2",
    dataIndex: "SO2",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.SO2)+")",
        }
      }
    }
  },
  {
    title: "SO2_24h",
    dataIndex: "SO2_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.SO2_24h)+")",
        }
      }
    }
  },
  {
    title: "NO2",
    dataIndex: "NO2",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.NO2)+")",
        }
      }
    }
  },
  {
    title: "NO2_24h",
    dataIndex: "NO2_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.NO2_24h)+")",
        }
      }
    }
  },
  {
    title: "O3",
    dataIndex: "O3",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.O3)+")",
        }
      }
    }
  },
  {
    title: "O3_24h",
    dataIndex: "O3_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.O3_24h)+")",
        }
      }
    }
  },
  {
    title: "O3_8h",
    dataIndex: "O3_8h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.O3_8h)+")",
        }
      }
    }
  },
  {
    title: "O3_8h_24h",
    dataIndex: "O3_8h_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.O3_8h_24h)+")",
        }
      }
    }
  },
  {
    title: "CO",
    dataIndex: "CO",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.CO)+")",
        }
      }
    }
  },
  {
    title: "CO_24h",
    dataIndex: "CO_24h",
    width: "120px",
    customCell:(record,rowIndex)=>{
      console.log(record,rowIndex)
      return{
        style:{
          "color": "#000000",
          "background-color": "rgba(255, 0, 0,"+Number(record.CO_24h)+")",
        }
      }
    }
  },
];

export default {
  data() {
    return {
      data: [],
      columns,
      chosenSensor: this.$store.state.chosenSensor,
      ipagination1: {
        current: 1,
        pageSize: 5,
        showTotal: (total, range) => {
          return (
            "第 " + range[0] + " ~ " + range[1] + " 条，共 " + total + " 条"
          );
        },
        showQuickJumper: true,
        showSizeChanger: false,
        total: 0,
      },
    };
  },
  methods: {
    //这个是实现表格分页跳转的函数
    handleTableChange2(pagination, filters, sorter) {
      this.ipagination1.current = pagination.current;
      this.ipagination1.pageSize = pagination.pageSize;
      filters;
      sorter;
    },
    getMissing() {
      var param = this.chosenSensor;
      this.chosenSensor = this.$store.state.chosenSensor;
      if (param != "" && param != this.chosenSensor) {
        this.axios
          .get("/api/getMissing", {
            params: {
              site_id: this.chosenSensor,
            },
          })
          .then((res) => {
            this.data=[]
            console.log(res.data);
            console.log(res.data.AQI);
            for (let i = 0; i <= 52; i++) {
              this.data.push({
                week:i+1,
                AQI: res.data.AQI[i],
                PM25: res.data.PM25[i],
                PM25_24h: res.data.PM25_24h[i],
                PM10: res.data.PM10[i],
                PM10_24h: res.data.PM10_24h[i],
                SO2: res.data.SO2[i],
                SO2_24h: res.data.SO2_24h[i],
                NO2: res.data.NO2[i],
                NO2_24h: res.data.NO2_24h[i],
                O3: res.data.O3[i],
                O3_24h: res.data.O3_24h[i],
                O3_8h: res.data.O3_8h[i],
                O3_8h_24h: res.data.O3_8h_24h[i],
                CO: res.data.CO[i],
                CO_24h: res.data.CO_24h[i],
              });
            }
          });
      }
    }
  },
  mounted() {
    window.setInterval(() => {
      setTimeout(this.getMissing(), 0);
    }, 100);
  },
};
</script>

<style scoped>
</style>
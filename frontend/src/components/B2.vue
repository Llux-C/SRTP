<template>
  <div>
    <h1 style="font-size: 20px; margin-top: 20px; margin-left: 40px">
      数据展示
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
    title: "时间",
    dataIndex: "hour",
    width: "120px",
    fixed: "left",
  },
];

export default {
  data() {
    return {
      data: [],
      columns,
      time1: this.$store.state.time,
      time2: this.$store.state.time,
      ipagination1: {
        current: 1,
        pageSize: 6,
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
    getColumn() {
      var param = this.time1;
      this.time1 = this.$store.state.time;
      if (param != this.time1) {
        console.log("getColumn");
        this.axios
          .get("/api/getSiteList", {
            params: {
              city: this.$store.state.chosenCity,
            },
          })
          .then((res) => {
            // console.log(res.data);
            this.columns = [
              {
                title: "时间",
                dataIndex: "hour",
                width: "120px",
                fixed: "left",
              },
            ];
            for (let i = 0; i < res.data.sites_list.length; i++) {
              this.columns.push({
                title: res.data.sites_list[i],
                dataIndex: res.data.sites_list[i],
                width: "120px",
              });
            }
            console.log(this.columns);
          });
      }
    },
    getValue() {
      var param = this.time2;
      this.time2 = this.$store.state.time;
      var pollu = this.$store.state.chosenWaste;
      if (this.$store.state.chosenWaste == "PM25") pollu = "PM2.5";
      if (this.$store.state.chosenWaste == "PM25_24h") pollu = "PM2.5_24h";
      if (param != this.time2) {
        console.log("getValue");
        this.axios
          .get("/api/getValue", {
            params: {
              city: this.$store.state.chosenCity,
              date: this.$store.state.chosenDate,
              pollu: pollu,
              fill: this.$store.state.fill,
            },
          })
          .then((res) => {
            this.data = [];
            // var d = JSON.stringify(res.data)
            // var e = JSON.parse(d)
            // console.log(e.hour)

            for (let i = 0; i <= 23; i++) {
              let json = {
                hour: i,
              };
              for (let j = 1; j < this.columns.length; j++) {
                let param = this.columns[j].title;

                // console.log(res.data)
                // console.log(param)
                // console.log(res.data[param])
                var todo = res.data[param][i]

                var dot = String(todo).indexOf(".");
                if (dot != -1) {
                  var dotCnt = String(todo).substring(dot + 1, todo.length);
                  if (dotCnt.length > 2) {
                    todo = todo.toFixed(2);
                  }
                }

                if (todo == 0) json[param] = "";
                else json[param] = todo;
              }
              this.data.push(json);
            }
            console.log(this.data);
          });
      }
    },
  },
  mounted() {
    window.setInterval(() => {
      setTimeout(this.getColumn(), 0);
    }, 1000);
    window.setInterval(() => {
      setTimeout(this.getValue(), 0);
    }, 1000);
  },
};
</script>

<style scoped>
</style>
<template>
<div>
<h1 style="font-size:20px;margin-top:20px;margin-left:40px">数据展示</h1>
<div style="display: flex;justify-content: center;">
  <div style="">
      <a-table
        :columns="columns"
        :data-source="data"
        :pagination="ipagination1"
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
    title: 'CO2',
    dataIndex: 'CO2',
    width: '20%',	
  },
  {
    title: 'SO2',
    dataIndex: 'SO2',
    width: '20%',	
  },
  {
    title: 'CO',
    dataIndex: 'CO',
    width: '20%',	
  },
  {
    title: 'NO',
    dataIndex: 'NO',
    width: '20%',	
  },
  {
    title: 'NO2',
    dataIndex: 'NO2',
    width: '20%',	
  },
];

const data = [];
for (let i = 1; i <=10; i++) {
  data.push({
    key: i,
    CO2: `File ${i}`,
    SO2: 'xlsx',
    CO:1,
    NO:2,
    NO2:i,
  });
}

export default{
    data()
    {
        return{
            data,
            columns,
            ipagination1:{
                current:1,
                pageSize:5,
                showTotal:(total,range)=>{
                    return '第 ' + range[0] + ' ~ ' +range[1] + ' 条，共 ' +total + ' 条'
                },
                showQuickJumper:true,
                showSizeChanger:false,
                total:0
            },
        }
    },
    methods: {
    //这个是实现表格分页跳转的函数
        handleTableChange2(pagination,filters,sorter){
            this.ipagination1.current = pagination.current
            this.ipagination1.pageSize = pagination.pageSize
            filters
            sorter
        },
    },
}
</script>
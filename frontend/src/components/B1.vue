<template>
  <div>
    <h1 style="font-size: 20px; margin-top: 20px; margin-left: 40px">
      地区选择
    </h1>
    <div style="display: flex; justify-content: center">
      <div style="">
        <a-select
          default-value="北京"
          style="width: 120px; margin: 10px"
          @change="handleProvinceChange"
        >
          <a-select-option v-for="prov in provs" :key="prov.value">
            {{ prov.value }}
          </a-select-option>
        </a-select>
        <a-select v-model="chosenCity" style="width: 120px; margin: 10px" @change="handleCityChange">
          <a-select-option v-for="city in citys" :key="city.value">
            {{ city.value }}
          </a-select-option>
        </a-select>
        <a-select v-model="chosenDate" style="width: 120px; margin: 10px">
          <a-select-option v-for="date in dates" :key="date">
            {{ date }}
          </a-select-option>
        </a-select>
        <a-select v-model="chosenWaste" style="width: 120px; margin: 10px">
          <a-select-option v-for="waste in wastes" :key="waste">
            {{ waste }}
          </a-select-option>
        </a-select>
      </div>
      <br />
    </div>
    <div style="display: flex; justify-content: center">
      <a-button style="margin: 10px" @click="chosen_unfilled">填充之前</a-button>
      <a-button style="margin: 10px" @click="chosen_filled">填充之后</a-button>
    </div>
    <div>
      <div id="map"></div>
    </div>
  </div>
</template>
<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";

var map;
const provs = [
  { label: "北京", value: "北京" },
  { label: "天津", value: "天津" },
  { label: "河北省", value: "河北省" },
  { label: "山西省", value: "山西省" },
  { label: "内蒙古自治区", value: "内蒙古自治区" },
  { label: "辽宁省", value: "辽宁省" },
  { label: "吉林省", value: "吉林省" },
  { label: "黑龙江省", value: "黑龙江省" },
  { label: "上海", value: "上海" },
  { label: "江苏省", value: "江苏省" },
  { label: "浙江省", value: "浙江省" },
  { label: "安徽省", value: "安徽省" },
  { label: "福建省", value: "福建省" },
  { label: "江西省", value: "江西省" },
  { label: "山东省", value: "山东省" },
  { label: "河南省", value: "河南省" },
  { label: "湖北省", value: "湖北省" },
  { label: "湖南省", value: "湖南省" },
  { label: "广东省", value: "广东省" },
  { label: "广西壮族自治区", value: "广西壮族自治区" },
  { label: "海南省", value: "海南省" },
  { label: "重庆", value: "重庆" },
  { label: "四川省", value: "四川省" },
  { label: "贵州省", value: "贵州省" },
  { label: "云南省", value: "云南省" },
  { label: "西藏自治区", value: "西藏自治区" },
  { label: "陕西省", value: "陕西省" },
  { label: "甘肃省", value: "甘肃省" },
  { label: "青海省", value: "青海省" },
  { label: "宁夏回族自治区", value: "宁夏回族自治区" },
  { label: "新疆维吾尔自治区", value: "新疆维吾尔自治区" },
  { label: "台湾省", value: "台湾省" },
  { label: "香港特别行政区", value: "香港特别行政区" },
  { label: "澳门特别行政区", value: "澳门特别行政区" },
];
export default {
  data() {
    return {
      provs: provs,
      chosenCity: "北京",
      citys: [],
      sensors: [],
      chosenProv: "",
      chosenDate: "",
      chosenWaste: "",
      wastes: [
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
      dates: [
        "20170101",
        "20170102",
        "20170103",
        "20170104",
        "20170105",
        "20170106",
        "20170107",
        "20170108",
        "20170109",
        "20170110",
        "20170111",
        "20170112",
        "20170113",
        "20170114",
        "20170115",
        "20170116",
        "20170117",
        "20170118",
        "20170119",
        "20170120",
        "20170121",
        "20170122",
        "20170123",
        "20170124",
        "20170125",
        "20170126",
        "20170127",
        "20170128",
        "20170129",
        "20170130",
        "20170131",
        "20170201",
        "20170202",
        "20170203",
        "20170204",
        "20170205",
        "20170206",
        "20170207",
        "20170208",
        "20170209",
        "20170210",
        "20170211",
        "20170212",
        "20170213",
        "20170214",
        "20170215",
        "20170216",
        "20170217",
        "20170218",
        "20170219",
        "20170220",
        "20170221",
        "20170222",
        "20170223",
        "20170224",
        "20170225",
        "20170226",
        "20170227",
        "20170228",
        "20170301",
        "20170302",
        "20170303",
        "20170304",
        "20170305",
        "20170306",
        "20170307",
        "20170308",
        "20170309",
        "20170310",
        "20170311",
        "20170312",
        "20170313",
        "20170314",
        "20170315",
        "20170316",
        "20170317",
        "20170318",
        "20170319",
        "20170320",
        "20170321",
        "20170322",
        "20170323",
        "20170324",
        "20170325",
        "20170326",
        "20170327",
        "20170328",
        "20170329",
        "20170330",
        "20170331",
        "20170401",
        "20170402",
        "20170403",
        "20170404",
        "20170405",
        "20170406",
        "20170407",
        "20170408",
        "20170409",
        "20170410",
        "20170411",
        "20170412",
        "20170413",
        "20170414",
        "20170415",
        "20170416",
        "20170417",
        "20170418",
        "20170419",
        "20170420",
        "20170421",
        "20170422",
        "20170423",
        "20170424",
        "20170425",
        "20170426",
        "20170427",
        "20170428",
        "20170429",
        "20170430",
        "20170501",
        "20170502",
        "20170503",
        "20170504",
        "20170505",
        "20170506",
        "20170507",
        "20170508",
        "20170509",
        "20170510",
        "20170511",
        "20170512",
        "20170513",
        "20170514",
        "20170515",
        "20170516",
        "20170517",
        "20170518",
        "20170519",
        "20170520",
        "20170521",
        "20170522",
        "20170523",
        "20170524",
        "20170525",
        "20170526",
        "20170527",
        "20170528",
        "20170529",
        "20170530",
        "20170531",
        "20170601",
        "20170602",
        "20170603",
        "20170604",
        "20170605",
        "20170606",
        "20170607",
        "20170608",
        "20170609",
        "20170610",
        "20170611",
        "20170612",
        "20170613",
        "20170614",
        "20170615",
        "20170616",
        "20170617",
        "20170618",
        "20170619",
        "20170620",
        "20170621",
        "20170622",
        "20170623",
        "20170624",
        "20170625",
        "20170626",
        "20170627",
        "20170628",
        "20170629",
        "20170630",
        "20170701",
        "20170702",
        "20170703",
        "20170704",
        "20170705",
        "20170706",
        "20170707",
        "20170708",
        "20170709",
        "20170710",
        "20170711",
        "20170712",
        "20170713",
        "20170714",
        "20170715",
        "20170716",
        "20170717",
        "20170718",
        "20170719",
        "20170720",
        "20170721",
        "20170722",
        "20170723",
        "20170724",
        "20170725",
        "20170726",
        "20170727",
        "20170728",
        "20170729",
        "20170730",
        "20170731",
        "20170801",
        "20170802",
        "20170803",
        "20170804",
        "20170805",
        "20170806",
        "20170807",
        "20170808",
        "20170809",
        "20170810",
        "20170811",
        "20170812",
        "20170813",
        "20170814",
        "20170815",
        "20170816",
        "20170817",
        "20170818",
        "20170819",
        "20170820",
        "20170821",
        "20170822",
        "20170823",
        "20170824",
        "20170825",
        "20170826",
        "20170827",
        "20170828",
        "20170829",
        "20170830",
        "20170831",
        "20170901",
        "20170902",
        "20170903",
        "20170904",
        "20170905",
        "20170906",
        "20170907",
        "20170908",
        "20170909",
        "20170910",
        "20170911",
        "20170912",
        "20170913",
        "20170914",
        "20170915",
        "20170916",
        "20170917",
        "20170918",
        "20170919",
        "20170920",
        "20170921",
        "20170922",
        "20170923",
        "20170924",
        "20170925",
        "20170926",
        "20170927",
        "20170928",
        "20170929",
        "20170930",
        "20171001",
        "20171002",
        "20171003",
        "20171004",
        "20171005",
        "20171006",
        "20171007",
        "20171008",
        "20171009",
        "20171010",
        "20171011",
        "20171012",
        "20171013",
        "20171014",
        "20171015",
        "20171016",
        "20171017",
        "20171018",
        "20171019",
        "20171020",
        "20171021",
        "20171022",
        "20171023",
        "20171024",
        "20171025",
        "20171026",
        "20171027",
        "20171028",
        "20171029",
        "20171030",
        "20171031",
        "20171101",
        "20171102",
        "20171103",
        "20171104",
        "20171105",
        "20171106",
        "20171107",
        "20171108",
        "20171109",
        "20171110",
        "20171111",
        "20171112",
        "20171113",
        "20171114",
        "20171115",
        "20171116",
        "20171117",
        "20171118",
        "20171119",
        "20171120",
        "20171121",
        "20171122",
        "20171123",
        "20171124",
        "20171125",
        "20171126",
        "20171127",
        "20171128",
        "20171129",
        "20171130",
        "20171201",
        "20171202",
        "20171203",
        "20171204",
        "20171205",
        "20171206",
        "20171207",
        "20171208",
        "20171209",
        "20171210",
        "20171211",
        "20171212",
        "20171213",
        "20171214",
        "20171215",
        "20171216",
        "20171217",
        "20171218",
        "20171219",
        "20171220",
        "20171221",
        "20171222",
        "20171223",
        "20171224",
        "20171225",
        "20171226",
        "20171227",
        "20171228",
        "20171229",
        "20171230",
        "20171231",
      ],
    };
  },
  methods: {
    handleProvinceChange(value) {
      console.log(value);
      let tempCity = [];
      this.citys = [];
      this.selectCity = "";
      let allCity = [
        {
          prov: "北京",
          label: "北京",
        },
        {
          prov: "天津",
          label: "天津",
        },
        {
          prov: "河北省",
          label: "石家庄",
        },
        {
          prov: "河北省",
          label: "唐山",
        },
        {
          prov: "河北省",
          label: "秦皇岛",
        },
        {
          prov: "河北省",
          label: "邯郸",
        },
        {
          prov: "河北省",
          label: "邢台",
        },
        {
          prov: "河北省",
          label: "保定",
        },
        {
          prov: "河北省",
          label: "张家口",
        },
        {
          prov: "河北省",
          label: "承德",
        },
        {
          prov: "河北省",
          label: "沧州",
        },
        {
          prov: "河北省",
          label: "廊坊",
        },
        {
          prov: "河北省",
          label: "衡水",
        },
        {
          prov: "山西省",
          label: "太原",
        },
        {
          prov: "山西省",
          label: "大同",
        },
        {
          prov: "山西省",
          label: "阳泉",
        },
        {
          prov: "山西省",
          label: "长治",
        },
        {
          prov: "山西省",
          label: "晋城",
        },
        {
          prov: "山西省",
          label: "朔州",
        },
        {
          prov: "山西省",
          label: "晋中",
        },
        {
          prov: "山西省",
          label: "运城",
        },
        {
          prov: "山西省",
          label: "忻州",
        },
        {
          prov: "山西省",
          label: "临汾",
        },
        {
          prov: "山西省",
          label: "吕梁",
        },
        {
          prov: "内蒙古自治区",
          label: "呼和浩特",
        },
        {
          prov: "内蒙古自治区",
          label: "包头",
        },
        {
          prov: "内蒙古自治区",
          label: "乌海",
        },
        {
          prov: "内蒙古自治区",
          label: "赤峰",
        },
        {
          prov: "内蒙古自治区",
          label: "通辽",
        },
        {
          prov: "内蒙古自治区",
          label: "鄂尔多斯",
        },
        {
          prov: "内蒙古自治区",
          label: "呼伦贝尔",
        },
        {
          prov: "内蒙古自治区",
          label: "巴彦淖尔",
        },
        {
          prov: "内蒙古自治区",
          label: "乌兰察布",
        },
        {
          prov: "内蒙古自治区",
          label: "兴安盟",
        },
        {
          prov: "内蒙古自治区",
          label: "锡林郭勒盟",
        },
        {
          prov: "内蒙古自治区",
          label: "阿拉善盟",
        },
        {
          prov: "辽宁省",
          label: "沈阳",
        },
        {
          prov: "辽宁省",
          label: "大连",
        },
        {
          prov: "辽宁省",
          label: "鞍山",
        },
        {
          prov: "辽宁省",
          label: "抚顺",
        },
        {
          prov: "辽宁省",
          label: "本溪",
        },
        {
          prov: "辽宁省",
          label: "丹东",
        },
        {
          prov: "辽宁省",
          label: "锦州",
        },
        {
          prov: "辽宁省",
          label: "营口",
        },
        {
          prov: "辽宁省",
          label: "阜新",
        },
        {
          prov: "辽宁省",
          label: "辽阳",
        },
        {
          prov: "辽宁省",
          label: "盘锦",
        },
        {
          prov: "辽宁省",
          label: "铁岭",
        },
        {
          prov: "辽宁省",
          label: "朝阳",
        },
        {
          prov: "辽宁省",
          label: "葫芦岛",
        },
        {
          prov: "吉林省",
          label: "长春",
        },
        {
          prov: "吉林省",
          label: "吉林",
        },
        {
          prov: "吉林省",
          label: "四平",
        },
        {
          prov: "吉林省",
          label: "辽源",
        },
        {
          prov: "吉林省",
          label: "通化",
        },
        {
          prov: "吉林省",
          label: "白山",
        },
        {
          prov: "吉林省",
          label: "松原",
        },
        {
          prov: "吉林省",
          label: "白城",
        },
        {
          prov: "吉林省",
          label: "延边朝鲜族自治州",
        },
        {
          prov: "黑龙江省",
          label: "哈尔滨",
        },
        {
          prov: "黑龙江省",
          label: "齐齐哈尔",
        },
        {
          prov: "黑龙江省",
          label: "鸡西",
        },
        {
          prov: "黑龙江省",
          label: "鹤岗",
        },
        {
          prov: "黑龙江省",
          label: "双鸭山",
        },
        {
          prov: "黑龙江省",
          label: "大庆",
        },
        {
          prov: "黑龙江省",
          label: "伊春",
        },
        {
          prov: "黑龙江省",
          label: "佳木斯",
        },
        {
          prov: "黑龙江省",
          label: "七台河",
        },
        {
          prov: "黑龙江省",
          label: "牡丹江",
        },
        {
          prov: "黑龙江省",
          label: "黑河",
        },
        {
          prov: "黑龙江省",
          label: "绥化",
        },
        {
          prov: "黑龙江省",
          label: "大兴安岭地区",
        },
        {
          prov: "上海",
          label: "上海",
        },
        {
          prov: "江苏省",
          label: "南京",
        },
        {
          prov: "江苏省",
          label: "无锡",
        },
        {
          prov: "江苏省",
          label: "徐州",
        },
        {
          prov: "江苏省",
          label: "常州",
        },
        {
          prov: "江苏省",
          label: "苏州",
        },
        {
          prov: "江苏省",
          label: "南通",
        },
        {
          prov: "江苏省",
          label: "连云港",
        },
        {
          prov: "江苏省",
          label: "淮安",
        },
        {
          prov: "江苏省",
          label: "盐城",
        },
        {
          prov: "江苏省",
          label: "扬州",
        },
        {
          prov: "江苏省",
          label: "镇江",
        },
        {
          prov: "江苏省",
          label: "泰州",
        },
        {
          prov: "江苏省",
          label: "宿迁",
        },
        {
          prov: "浙江省",
          label: "杭州",
        },
        {
          prov: "浙江省",
          label: "宁波",
        },
        {
          prov: "浙江省",
          label: "温州",
        },
        {
          prov: "浙江省",
          label: "嘉兴",
        },
        {
          prov: "浙江省",
          label: "湖州",
        },
        {
          prov: "浙江省",
          label: "绍兴",
        },
        {
          prov: "浙江省",
          label: "金华",
        },
        {
          prov: "浙江省",
          label: "衢州",
        },
        {
          prov: "浙江省",
          label: "舟山",
        },
        {
          prov: "浙江省",
          label: "台州",
        },
        {
          prov: "浙江省",
          label: "丽水",
        },
        {
          prov: "安徽省",
          label: "合肥",
        },
        {
          prov: "安徽省",
          label: "芜湖",
        },
        {
          prov: "安徽省",
          label: "蚌埠",
        },
        {
          prov: "安徽省",
          label: "淮南",
        },
        {
          prov: "安徽省",
          label: "马鞍山",
        },
        {
          prov: "安徽省",
          label: "淮北",
        },
        {
          prov: "安徽省",
          label: "铜陵",
        },
        {
          prov: "安徽省",
          label: "安庆",
        },
        {
          prov: "安徽省",
          label: "黄山",
        },
        {
          prov: "安徽省",
          label: "滁州",
        },
        {
          prov: "安徽省",
          label: "阜阳",
        },
        {
          prov: "安徽省",
          label: "宿州",
        },
        {
          prov: "安徽省",
          label: "六安",
        },
        {
          prov: "安徽省",
          label: "亳州",
        },
        {
          prov: "安徽省",
          label: "池州",
        },
        {
          prov: "安徽省",
          label: "宣城",
        },
        {
          prov: "福建省",
          label: "福州",
        },
        {
          prov: "福建省",
          label: "厦门",
        },
        {
          prov: "福建省",
          label: "莆田",
        },
        {
          prov: "福建省",
          label: "三明",
        },
        {
          prov: "福建省",
          label: "泉州",
        },
        {
          prov: "福建省",
          label: "漳州",
        },
        {
          prov: "福建省",
          label: "南平",
        },
        {
          prov: "福建省",
          label: "龙岩",
        },
        {
          prov: "福建省",
          label: "宁德",
        },
        {
          prov: "江西省",
          label: "南昌",
        },
        {
          prov: "江西省",
          label: "景德镇",
        },
        {
          prov: "江西省",
          label: "萍乡",
        },
        {
          prov: "江西省",
          label: "九江",
        },
        {
          prov: "江西省",
          label: "新余",
        },
        {
          prov: "江西省",
          label: "鹰潭",
        },
        {
          prov: "江西省",
          label: "赣州",
        },
        {
          prov: "江西省",
          label: "吉安",
        },
        {
          prov: "江西省",
          label: "宜春",
        },
        {
          prov: "江西省",
          label: "抚州",
        },
        {
          prov: "江西省",
          label: "上饶",
        },
        {
          prov: "山东省",
          label: "济南",
        },
        {
          prov: "山东省",
          label: "青岛",
        },
        {
          prov: "山东省",
          label: "淄博",
        },
        {
          prov: "山东省",
          label: "枣庄",
        },
        {
          prov: "山东省",
          label: "东营",
        },
        {
          prov: "山东省",
          label: "烟台",
        },
        {
          prov: "山东省",
          label: "潍坊",
        },
        {
          prov: "山东省",
          label: "济宁",
        },
        {
          prov: "山东省",
          label: "泰安",
        },
        {
          prov: "山东省",
          label: "威海",
        },
        {
          prov: "山东省",
          label: "日照",
        },
        {
          prov: "山东省",
          label: "莱芜",
        },
        {
          prov: "山东省",
          label: "临沂",
        },
        {
          prov: "山东省",
          label: "德州",
        },
        {
          prov: "山东省",
          label: "聊城",
        },
        {
          prov: "山东省",
          label: "滨州",
        },
        {
          prov: "山东省",
          label: "菏泽",
        },
        {
          prov: "河南省",
          label: "郑州",
        },
        {
          prov: "河南省",
          label: "开封",
        },
        {
          prov: "河南省",
          label: "洛阳",
        },
        {
          prov: "河南省",
          label: "平顶山",
        },
        {
          prov: "河南省",
          label: "安阳",
        },
        {
          prov: "河南省",
          label: "鹤壁",
        },
        {
          prov: "河南省",
          label: "新乡",
        },
        {
          prov: "河南省",
          label: "焦作",
        },
        {
          prov: "河南省",
          label: "濮阳",
        },
        {
          prov: "河南省",
          label: "许昌",
        },
        {
          prov: "河南省",
          label: "漯河",
        },
        {
          prov: "河南省",
          label: "三门峡",
        },
        {
          prov: "河南省",
          label: "南阳",
        },
        {
          prov: "河南省",
          label: "商丘",
        },
        {
          prov: "河南省",
          label: "信阳",
        },
        {
          prov: "河南省",
          label: "周口",
        },
        {
          prov: "河南省",
          label: "驻马店",
        },
        {
          prov: "河南省",
          label: "省直辖县级行政区划",
        },
        {
          prov: "湖北省",
          label: "武汉",
        },
        {
          prov: "湖北省",
          label: "黄石",
        },
        {
          prov: "湖北省",
          label: "十堰",
        },
        {
          prov: "湖北省",
          label: "宜昌",
        },
        {
          prov: "湖北省",
          label: "襄阳",
        },
        {
          prov: "湖北省",
          label: "鄂州",
        },
        {
          prov: "湖北省",
          label: "荆门",
        },
        {
          prov: "湖北省",
          label: "孝感",
        },
        {
          prov: "湖北省",
          label: "荆州",
        },
        {
          prov: "湖北省",
          label: "黄冈",
        },
        {
          prov: "湖北省",
          label: "咸宁",
        },
        {
          prov: "湖北省",
          label: "随州",
        },
        {
          prov: "湖北省",
          label: "恩施土家族苗族自治州",
        },
        {
          prov: "湖北省",
          label: "省直辖县级行政区划",
        },
        {
          prov: "湖北省",
          label: "仙桃",
        },
        {
          prov: "湖北省",
          label: "潜江",
        },
        {
          prov: "湖北省",
          label: "天门",
        },
        {
          prov: "湖北省",
          label: "神农架林区",
        },
        {
          prov: "湖南省",
          label: "长沙",
        },
        {
          prov: "湖南省",
          label: "株洲",
        },
        {
          prov: "湖南省",
          label: "湘潭",
        },
        {
          prov: "湖南省",
          label: "衡阳",
        },
        {
          prov: "湖南省",
          label: "邵阳",
        },
        {
          prov: "湖南省",
          label: "岳阳",
        },
        {
          prov: "湖南省",
          label: "常德",
        },
        {
          prov: "湖南省",
          label: "张家界",
        },
        {
          prov: "湖南省",
          label: "益阳",
        },
        {
          prov: "湖南省",
          label: "郴州",
        },
        {
          prov: "湖南省",
          label: "永州",
        },
        {
          prov: "湖南省",
          label: "怀化",
        },
        {
          prov: "湖南省",
          label: "娄底",
        },
        {
          prov: "湖南省",
          label: "湘西土家族苗族自治州",
        },
        {
          prov: "广东省",
          label: "广州",
        },
        {
          prov: "广东省",
          label: "韶关",
        },
        {
          prov: "广东省",
          label: "深圳",
        },
        {
          prov: "广东省",
          label: "珠海",
        },
        {
          prov: "广东省",
          label: "汕头",
        },
        {
          prov: "广东省",
          label: "佛山",
        },
        {
          prov: "广东省",
          label: "江门",
        },
        {
          prov: "广东省",
          label: "湛江",
        },
        {
          prov: "广东省",
          label: "茂名",
        },
        {
          prov: "广东省",
          label: "肇庆",
        },
        {
          prov: "广东省",
          label: "惠州",
        },
        {
          prov: "广东省",
          label: "梅州",
        },
        {
          prov: "广东省",
          label: "汕尾",
        },
        {
          prov: "广东省",
          label: "河源",
        },
        {
          prov: "广东省",
          label: "阳江",
        },
        {
          prov: "广东省",
          label: "清远",
        },
        {
          prov: "广东省",
          label: "东莞",
        },
        {
          prov: "广东省",
          label: "中山",
        },
        {
          prov: "广东省",
          label: "潮州",
        },
        {
          prov: "广东省",
          label: "揭阳",
        },
        {
          prov: "广东省",
          label: "云浮",
        },
        {
          prov: "广西壮族自治区",
          label: "南宁",
        },
        {
          prov: "广西壮族自治区",
          label: "柳州",
        },
        {
          prov: "广西壮族自治区",
          label: "桂林",
        },
        {
          prov: "广西壮族自治区",
          label: "梧州",
        },
        {
          prov: "广西壮族自治区",
          label: "北海",
        },
        {
          prov: "广西壮族自治区",
          label: "防城港",
        },
        {
          prov: "广西壮族自治区",
          label: "钦州",
        },
        {
          prov: "广西壮族自治区",
          label: "贵港",
        },
        {
          prov: "广西壮族自治区",
          label: "玉林",
        },
        {
          prov: "广西壮族自治区",
          label: "百色",
        },
        {
          prov: "广西壮族自治区",
          label: "贺州",
        },
        {
          prov: "广西壮族自治区",
          label: "河池",
        },
        {
          prov: "广西壮族自治区",
          label: "来宾",
        },
        {
          prov: "广西壮族自治区",
          label: "崇左",
        },
        {
          prov: "海南省",
          label: "海口",
        },
        {
          prov: "海南省",
          label: "三亚",
        },
        {
          prov: "海南省",
          label: "三沙",
        },
        {
          prov: "海南省",
          label: "省直辖县级行政区划",
        },
        {
          prov: "海南省",
          label: "五指山",
        },
        {
          prov: "海南省",
          label: "琼海",
        },
        {
          prov: "海南省",
          label: "儋州",
        },
        {
          prov: "海南省",
          label: "文昌",
        },
        {
          prov: "海南省",
          label: "万宁",
        },
        {
          prov: "海南省",
          label: "东方",
        },
        {
          prov: "海南省",
          label: "定安县",
        },
        {
          prov: "海南省",
          label: "屯昌县",
        },
        {
          prov: "海南省",
          label: "澄迈县",
        },
        {
          prov: "海南省",
          label: "临高县",
        },
        {
          prov: "海南省",
          label: "白沙黎族自治县",
        },
        {
          prov: "海南省",
          label: "昌江黎族自治县",
        },
        {
          prov: "海南省",
          label: "乐东黎族自治县",
        },
        {
          prov: "海南省",
          label: "陵水黎族自治县",
        },
        {
          prov: "海南省",
          label: "保亭黎族苗族自治县",
        },
        {
          prov: "海南省",
          label: "琼中黎族苗族自治县",
        },
        {
          prov: "重庆",
          label: "重庆",
        },
        {
          prov: "四川省",
          label: "成都",
        },
        {
          prov: "四川省",
          label: "自贡",
        },
        {
          prov: "四川省",
          label: "攀枝花",
        },
        {
          prov: "四川省",
          label: "泸州",
        },
        {
          prov: "四川省",
          label: "德阳",
        },
        {
          prov: "四川省",
          label: "绵阳",
        },
        {
          prov: "四川省",
          label: "广元",
        },
        {
          prov: "四川省",
          label: "遂宁",
        },
        {
          prov: "四川省",
          label: "内江",
        },
        {
          prov: "四川省",
          label: "乐山",
        },
        {
          prov: "四川省",
          label: "南充",
        },
        {
          prov: "四川省",
          label: "眉山",
        },
        {
          prov: "四川省",
          label: "宜宾",
        },
        {
          prov: "四川省",
          label: "广安",
        },
        {
          prov: "四川省",
          label: "达州",
        },
        {
          prov: "四川省",
          label: "雅安",
        },
        {
          prov: "四川省",
          label: "巴中",
        },
        {
          prov: "四川省",
          label: "资阳",
        },
        {
          prov: "四川省",
          label: "阿坝藏族羌族自治州",
        },
        {
          prov: "四川省",
          label: "甘孜藏族自治州",
        },
        {
          prov: "四川省",
          label: "凉山彝族自治州",
        },
        {
          prov: "贵州省",
          label: "贵阳",
        },
        {
          prov: "贵州省",
          label: "六盘水",
        },
        {
          prov: "贵州省",
          label: "遵义",
        },
        {
          prov: "贵州省",
          label: "安顺",
        },
        {
          prov: "贵州省",
          label: "毕节",
        },
        {
          prov: "贵州省",
          label: "铜仁",
        },
        {
          prov: "贵州省",
          label: "黔西南布依族苗族自治州",
        },
        {
          prov: "贵州省",
          label: "黔东南苗族侗族自治州",
        },
        {
          prov: "贵州省",
          label: "黔南布依族苗族自治州",
        },
        {
          prov: "云南省",
          label: "昆明",
        },
        {
          prov: "云南省",
          label: "曲靖",
        },
        {
          prov: "云南省",
          label: "玉溪",
        },
        {
          prov: "云南省",
          label: "保山",
        },
        {
          prov: "云南省",
          label: "昭通",
        },
        {
          prov: "云南省",
          label: "丽江",
        },
        {
          prov: "云南省",
          label: "普洱",
        },
        {
          prov: "云南省",
          label: "临沧",
        },
        {
          prov: "云南省",
          label: "楚雄彝族自治州",
        },
        {
          prov: "云南省",
          label: "红河哈尼族彝族自治州",
        },
        {
          prov: "云南省",
          label: "文山壮族苗族自治州",
        },
        {
          prov: "云南省",
          label: "西双版纳傣族自治州",
        },
        {
          prov: "云南省",
          label: "大理白族自治州",
        },
        {
          prov: "云南省",
          label: "德宏傣族景颇族自治州",
        },
        {
          prov: "云南省",
          label: "怒江傈僳族自治州",
        },
        {
          prov: "云南省",
          label: "迪庆藏族自治州",
        },
        {
          prov: "西藏自治区",
          label: "拉萨",
        },
        {
          prov: "西藏自治区",
          label: "昌都地区",
        },
        {
          prov: "西藏自治区",
          label: "山南地区",
        },
        {
          prov: "西藏自治区",
          label: "日喀则地区",
        },
        {
          prov: "西藏自治区",
          label: "那曲地区",
        },
        {
          prov: "西藏自治区",
          label: "阿里地区",
        },
        {
          prov: "西藏自治区",
          label: "林芝地区",
        },
        {
          prov: "陕西省",
          label: "西安",
        },
        {
          prov: "陕西省",
          label: "铜川",
        },
        {
          prov: "陕西省",
          label: "宝鸡",
        },
        {
          prov: "陕西省",
          label: "咸阳",
        },
        {
          prov: "陕西省",
          label: "渭南",
        },
        {
          prov: "陕西省",
          label: "延安",
        },
        {
          prov: "陕西省",
          label: "汉中",
        },
        {
          prov: "陕西省",
          label: "榆林",
        },
        {
          prov: "陕西省",
          label: "安康",
        },
        {
          prov: "陕西省",
          label: "商洛",
        },
        {
          prov: "甘肃省",
          label: "兰州",
        },
        {
          prov: "甘肃省",
          label: "嘉峪关",
        },
        {
          prov: "甘肃省",
          label: "金昌",
        },
        {
          prov: "甘肃省",
          label: "白银",
        },
        {
          prov: "甘肃省",
          label: "天水",
        },
        {
          prov: "甘肃省",
          label: "武威",
        },
        {
          prov: "甘肃省",
          label: "张掖",
        },
        {
          prov: "甘肃省",
          label: "平凉",
        },
        {
          prov: "甘肃省",
          label: "酒泉",
        },
        {
          prov: "甘肃省",
          label: "庆阳",
        },
        {
          prov: "甘肃省",
          label: "定西",
        },
        {
          prov: "甘肃省",
          label: "陇南",
        },
        {
          prov: "甘肃省",
          label: "临夏回族自治州",
        },
        {
          prov: "甘肃省",
          label: "甘南藏族自治州",
        },
        {
          prov: "青海省",
          label: "西宁",
        },
        {
          prov: "青海省",
          label: "海东",
        },
        {
          prov: "青海省",
          label: "海北藏族自治州",
        },
        {
          prov: "青海省",
          label: "黄南藏族自治州",
        },
        {
          prov: "青海省",
          label: "海南藏族自治州",
        },
        {
          prov: "青海省",
          label: "果洛藏族自治州",
        },
        {
          prov: "青海省",
          label: "玉树藏族自治州",
        },
        {
          prov: "青海省",
          label: "海西蒙古族藏族自治州",
        },
        {
          prov: "宁夏回族自治区",
          label: "银川",
        },
        {
          prov: "宁夏回族自治区",
          label: "石嘴山",
        },
        {
          prov: "宁夏回族自治区",
          label: "吴忠",
        },
        {
          prov: "宁夏回族自治区",
          label: "固原",
        },
        {
          prov: "宁夏回族自治区",
          label: "中卫",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "乌鲁木齐",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "克拉玛依",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "吐鲁番地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "哈密地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "昌吉回族自治州",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "博尔塔拉蒙古自治州",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "巴音郭楞蒙古自治州",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "阿克苏地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "克孜勒苏柯尔克孜自治州",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "喀什地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "和田地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "伊犁哈萨克自治州",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "塔城地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "阿勒泰地区",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "自治区直辖县级行政区划",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "石河子",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "阿拉尔",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "图木舒克",
        },
        {
          prov: "新疆维吾尔自治区",
          label: "五家渠",
        },
        {
          prov: "台湾省",
          label: "台北",
        },
        {
          prov: "台湾省",
          label: "高雄",
        },
        {
          prov: "台湾省",
          label: "基隆",
        },
        {
          prov: "台湾省",
          label: "台中",
        },
        {
          prov: "台湾省",
          label: "台南",
        },
        {
          prov: "台湾省",
          label: "新竹",
        },
        {
          prov: "台湾省",
          label: "嘉义",
        },
        {
          prov: "台湾省",
          label: "省直辖",
        },
        {
          prov: "香港特别行政区",
          label: "香港岛",
        },
        {
          prov: "香港特别行政区",
          label: "九龙",
        },
        {
          prov: "香港特别行政区",
          label: "新界",
        },
        {
          prov: "澳门特别行政区",
          label: "澳门半岛",
        },
        {
          prov: "澳门特别行政区",
          label: "澳门离岛",
        },
        {
          prov: "澳门特别行政区",
          label: "无堂区划分区域",
        },
      ];
      for (var val of allCity) {
        if (value == val.prov) {
          console.log(val);
          tempCity.push({ label: val.label, value: val.label });
        }
      }
      this.citys = tempCity;
      console.log(this.citys);
    },
    chosen_unfilled() {
      this.$store.state.chosenCity = this.chosenCity;
      this.$store.state.chosenWaste = this.chosenWaste;
      this.$store.state.chosenDate = this.chosenDate;
      this.$store.state.fill = 0;
      this.$store.state.time += 1;
      console.log(this.$store.state.chosenCity);
      console.log(this.$store.state.chosenWaste);
      console.log(this.$store.state.chosenDate);
      console.log(this.$store.state.fill);
      console.log(this.$store.state.time);
    },
    chosen_filled() {
      this.$store.state.chosenCity = this.chosenCity;
      this.$store.state.chosenWaste = this.chosenWaste;
      this.$store.state.chosenDate = this.chosenDate;
      this.$store.state.fill = 1;
      this.$store.state.time += 1;
      console.log(this.$store.state.chosenCity);
      console.log(this.$store.state.chosenWaste);
      console.log(this.$store.state.chosenDate);
      console.log(this.$store.state.fill);
      console.log(this.$store.state.time);
    },
    drawMap() {
      map = L.map("map", {
        minZoom: 3,
        maxZoom: 14,
        center: this.center,
        zoom: 10,
        zoomSnap: 0.1,
        zoomControl: true,
        attributionControl: false,
        touchZoom: true,
      });
      this.map = map;
      window.map = map;
      const tileUrl =
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY3ktbGx1IiwiYSI6ImNraHZsMGYzYjBnNnMyc28yYXlvd256NnYifQ.TTfaDTXXNPAOAQ6_lqIFEg";
      L.tileLayer(tileUrl, {
        tileSize: 512,
        zoomOffset: -1,
      }).addTo(map);
      var popup = L.popup();
      function onMapClick(e) {
        popup
          .setLatLng(e.latlng)
          .setContent("You clicked the map at " + e.latlng.toString())
          .openOn(map);
      }
      map.on("click", onMapClick);
    },
    handleCityChange(value) {
      this.axios
        .get("/api/getSiteList", {
          params: {
            city: value,
          },
        })
        .then((res) => {
          console.log(res);
          console.log(res.data);
          this.sensors = res.data.sites_list;
          var point = this.sensors[0];
          console.log(point);
          this.axios
            .get("/api/getLocation", {
              params: {
                site_id: point,
              },
            })
            .then((r) => {
              console.log(r.data);
              this.center = r.data.location;
              map.setView(this.center, 10);
            });

          var locations = [];
          for (let i = 0; i < this.sensors.length; i++) {
            this.axios
              .get("/api/getLocation", {
                params: {
                  site_id: this.sensors[i],
                },
              })
              .then((r) => {
                locations.push(r.data.location);
                L.circle(r.data.location, 600, {
                  color: "#d7c6ff",
                  fillColor: "#0000ff",
                  fillOpacity: 0.5,
                })
                  .addTo(map)
                  .bindPopup(this.sensors[i]);
              });
          }
        });
    },
  },
  mounted: function () {
    // this.handleCityChange()
    this.$store.state.time = 0;
    this.handleCityChange("北京")
    this.drawMap();
  },
};
</script>

<style scoped>
#map {
  margin: 0 auto;
  width: 80%;
  height: 400px;
}
</style>
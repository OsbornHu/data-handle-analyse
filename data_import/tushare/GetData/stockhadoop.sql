CREATE TABLE stockbasics (
  code string COMMENT '代码',
  name string COMMENT '名称',
  industry string COMMENT '所属行业',
  area string COMMENT '地区',
  pe float COMMENT '市盈率',
  outstanding float COMMENT '流通股本(亿)',
  totals float COMMENT '总股本(亿)',
  totalAssets float COMMENT '总资产(万)',
  liquidAssets float COMMENT '流动资产',
  fixedAssets float COMMENT '固定资产',
  reserved float COMMENT '公积金',
  reservedPerShare float COMMENT '每股公积金',
  esp float COMMENT '每股收益',
  bvps float COMMENT '每股净资',
  pb float COMMENT '市净率',
  timeToMarket bigint COMMENT '上市日期',
  undp float COMMENT '未分利润',
  perundp float COMMENT '每股未分配',
  rev float COMMENT '收入同比(%)',
  profit float COMMENT '利润同比(%)',
  gpr float COMMENT '毛利率(%)',
  npr float COMMENT '净利润率(%)',
  holders float COMMENT '股东人数'
) ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','



CREATE TABLE stock_history (
  code string COMMENT '股票代码',
  open float COMMENT '开盘价',
  high float COMMENT '最高价',
  close float COMMENT '收盘价',
  low float COMMENT '最低价',
  volume float COMMENT '成交量',
  price_change float COMMENT '价格变动',
  p_change float COMMENT '涨跌幅',
  ma5 float COMMENT '5日均价',
  ma10 float COMMENT '10日均价',
  ma20 float COMMENT '20日均价',
  v_ma5 float COMMENT '5日均量',
  v_ma10 float COMMENT '10日均量',
  v_ma20 float COMMENT '20日均量',
stock_date string comment '日期，用于分区字段'
)  
  
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ','
  
  
  drop table stock_history


select * from stockbasics
select * from stock_history

select count(code) from stock_history




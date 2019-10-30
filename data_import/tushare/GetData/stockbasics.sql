CREATE TABLE `stockbasics` (
  `code` varchar(10) DEFAULT NULL COMMENT '代码',
  `name` varchar(50) DEFAULT NULL COMMENT '名称',
  `industry` varchar(50) DEFAULT NULL COMMENT '所属行业',
  `area` varchar(50) DEFAULT NULL COMMENT '地区',
  `pe` double DEFAULT NULL COMMENT '市盈率',
  `outstanding` double DEFAULT NULL COMMENT '流通股本(亿)',
  `totals` double DEFAULT NULL COMMENT '总股本(亿)',
  `totalAssets` double DEFAULT NULL COMMENT '总资产(万)',
  `liquidAssets` double DEFAULT NULL COMMENT '流动资产',
  `fixedAssets` double DEFAULT NULL COMMENT '固定资产',
  `reserved` double DEFAULT NULL COMMENT '公积金',
  `reservedPerShare` double DEFAULT NULL COMMENT '每股公积金',
  `esp` double DEFAULT NULL COMMENT '每股收益',
  `bvps` double DEFAULT NULL COMMENT '每股净资',
  `pb` double DEFAULT NULL COMMENT '市净率',
  `timeToMarket` bigint(20) DEFAULT NULL COMMENT '上市日期',
  `undp` double DEFAULT NULL COMMENT '未分利润',
  `perundp` double DEFAULT NULL COMMENT '每股未分配',
  `rev` double DEFAULT NULL COMMENT '收入同比(%)',
  `profit` double DEFAULT NULL COMMENT '利润同比(%)',
  `gpr` double DEFAULT NULL COMMENT '毛利率(%)',
  `npr` double DEFAULT NULL COMMENT '净利润率(%)',
  `holders` double DEFAULT NULL COMMENT '股东人数',
  KEY `stock_basics_index01` (`code`),
  KEY `stock_basics_index02` (`area`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


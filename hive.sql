CREATE TABLE stock_company (
ts_code string,
exch string,
chairman string,
manager string,
secretary string ,
reg_capital float ,
setup_date string ,
province string,
city string,
introduction string,
website string,
email string,
office string,
employees int,
main_business string,
business_scope string
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','

CREATE INDEX stock_company_index ON TABLE stock_company(ts_code) 
AS 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' WITH deferred REBUILD IN TABLE stock_company_index_table

drop table stock_company

create table forecast(
ts_code string,
ann_date string,
end_date string,
type string,
p_change_min string,
p_change_max string,
net_profit_min string
)ROW FORMAT DELIMITED 
 FIELDS TERMINATED BY ','
 
 drop table forecast
 
 create table income(
 ts_code string,
 ann_date string,
 f_ann_date string,
 end_date string,
 report_type string,
 comp_type string,
 basic_eps float,
 diluted_eps float,
 total_revenue float,
 revenue float,
 int_income float,
 prem_earned float,
 comm_income float,
 n_commis_income float,
 n_oth_income float,
 prem_income float,
 une_prem_reser float,
 n_sec_tb_income float,
 n_sec_uw_income float,
 n_asset_mg_income float,
 oth_b_income float,

 total_cogs float,
 prem_refund float,
 compens_payout float,
 reser_insur_liab float,
 div_payt float,
 reins_exp float,
 oper_exp float,
 other_bus_cost float,
 operate_profit float,
 total_profit float,
 income_tax float,
 n_income float,
 n_income_attr_p float,
 minority_gain float,
 oth_compr_income float,
 t_compr_income float,
 compr_inc_attr_p float,
 compr_inc_attr_m_s float,
 ebit float,
 ebitda float,
 insurance_exp float,
 undist_profit float,
 distable_profit float,
 update_flag string
 
 )ROW FORMAT DELIMITED 
   FIELDS TERMINATED BY ','
   
   drop table income
 
 select * from forecast
 
 select * from stock_company where ts_code='002475.SZ'

select total_revenue+revenue from income where ts_code='600690.SH'

select count(ts_code) from stock_company

select count(ts_code),ts_code from stock_company group by ts_code having count(ts_code)>1



create table balancesheet(
ts_code string,
ann_date string,
f_ann_date string,
end_date string,
report_type string,
comp_type string,
total_share float,
cap_rese float,
undistr_porfit float,
surplus_rese float,
special_rese float,
money_cap float,
trad_asset float,
notes_receiv float,
accounts_receiv float,
oth_receiv float,
prepayment float,
div_receiv float,
int_receiv float,
total_cur_assets float,
time_deposits float,
oth_assets float,
fix_assets float,
r_and_d float,
cash_reser_cb float,
indep_acct_assets float,
total_assets float,
lt_borr float,
st_borr float,
estimated_liab float,
acc_receivable float,
payables float
)ROW FORMAT DELIMITED 
 FIELDS TERMINATED BY ','
 
 select * from balancesheet
 
 create table cashflow(
 ts_code string,
 ann_date string,
 end_date string,
 comp_type string,
 report_type string,
 net_profit float,
 finan_exp float,
 free_cashflow float
 )ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ','
 
 
CREATE SCHEMA IF NOT EXISTS  Real_Time_Financial_Insights_Using_Change_Data_Capture_CDC;
USE SCHEMA Real_Time_Financial_Insights_Using_Change_Data_Capture_CDC;

/*---------------------------*/
-- Create our Warehouse
/*---------------------------*/

-- data science virtual cluster
CREATE VCLUSTER IF NOT EXISTS cdc_ds_vc
   VCLUSTER_SIZE = XSMALL
   VCLUSTER_TYPE = ANALYTICS
   AUTO_SUSPEND_IN_SECOND = 60
   AUTO_RESUME = TRUE
   COMMENT  'data science VCLUSTER for cdc';

-- Use our VCLUSTER
USE VCLUSTER cdc_ds_wh;
/*---------------------------*/
-- sql completion note
/*---------------------------*/
SELECT 'cdc sql is now complete' AS note;

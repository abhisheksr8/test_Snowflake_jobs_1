{{
  config({    
    "materialized": "table",
    "full_refresh": true
  })
}}

WITH qa_test_Automation_seed_job_snowflake AS (

  SELECT * 
  
  FROM {{ ref('qa_test_Automation_seed_job_snowflake')}}

)

SELECT *

FROM qa_test_Automation_seed_job_snowflake

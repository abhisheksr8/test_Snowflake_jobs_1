{% snapshot test_modelanother_Automation_Snowflake_jobs_model %}
{{
  config({    
    "alias": "test_Automation_Snowflake_jobs_model_1764535983270",
    "invalidate_hard_deletes": true,
    "strategy": "timestamp",
    "target_schema": "qa_upload_schema",
    "unique_key": ["ID"],
    "updated_at": "UPDATED_AT"
  })
}}

WITH test_Automation_Snowflake_jobs_model AS (

  SELECT *
  
  FROM {{ ref('test_Automation_Snowflake_jobs_model')}}

)

SELECT *

FROM test_Automation_Snowflake_jobs_model

{% endsnapshot %}

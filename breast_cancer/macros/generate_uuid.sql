{% macro generate_uuid() %}
    md5(random()::text || clock_timestamp()::text)::uuid
{% endmacro %}
{% macro generate_deterministic_uuid(table_name) %}
    md5(
        {%- set columns = adapter.get_columns_in_relation(table_name) -%}
        {%- for column in columns %}
            coalesce(cast({{ column.name }} as text), '') {% if not loop.last %} || '|' || {% endif %}
        {%- endfor %}
    )::uuid
{% endmacro %}
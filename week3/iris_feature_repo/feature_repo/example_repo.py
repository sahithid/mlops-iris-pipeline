from datetime import timedelta

from feast import BigQuerySource, Entity, Feature, FeatureView, ValueType, Field
from feast.types import Float64, Int64

iris_entity = Entity(name="iris_id", join_keys=["iris_id"], value_type=ValueType.INT64,)

table = "gentle-presence-472611-u8.feast_iris_data.iris_features"

iris_data_source = BigQuerySource(
    table=table,
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

iris_feature_view = FeatureView(
    name="iris_feature_view",
    entities=[iris_entity],
    ttl=timedelta(weeks=52),
    schema=[
        Field(name="sepal_length", dtype=Float64),
        Field(name="sepal_width", dtype=Float64),
        Field(name="petal_length", dtype=Float64),
        Field(name="petal_width", dtype=Float64),
    ],
    source=iris_data_source,
    tags={"team": "iris_species"},
)
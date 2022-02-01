from feast import FeatureStore

features = [
    "driver_hourly_stats:conv_rate",
]

fs = FeatureStore(repo_path=".")
online_features = fs.get_online_features(
    features=features,
    entity_rows=[
        {"driver_id": 1001},
	{"driver_id": 1002},
        {"driver_id": 1003}]
).to_dict()

print(online_features)

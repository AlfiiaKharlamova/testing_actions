from feast import FeatureStore

features = [
    "driver_hourly_stats:conv_rate",
    "driver_hourly_stats:acc_rate",
    "driver_hourly_stats:avg_daily_trips"
]

fs = FeatureStore(repo_path="in_bug/")
online_features = fs.get_online_features(
    features=features,
    entity_rows=[
        {"driver_id": 1001},
	{"driver_id": 1002},
        {"driver_id": 1003}]
).to_dict()

print(online_features)

from google.cloud import aiplatform

# Set your feature store location and ID
LOCATION = "us-central1"
FEATURESTORE_ID = "your-feature-store-id"

# Set the ID of the feature to replace
FEATURE_ID = "your-feature-id"

# Set the new value of the feature
NEW_VALUE = "new-feature-value"

# Initialize the FeaturestoreClient
client_options = {"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
client = aiplatform.gapic.FeaturestoreServiceClient(client_options=client_options)

# Get the current version of the feature
feature_path = client.feature_path(project="projects/your-project-id", location=LOCATION, featurestore=FEATURESTORE_ID, feature=FEATURE_ID)
feature = client.get_feature(name=feature_path)

# Build the new feature
new_feature = aiplatform.gapic.Feature(
    description=feature.description,
    valueType=feature.valueType,
    id=feature.id,
    name=feature.name,
    etag=feature.etag,
    labels=feature.labels,
    featurestore=feature.featurestore,
    createTime=feature.createTime,
    updateTime=feature.updateTime,
    monitoringConfigs=feature.monitoringConfigs,
    monitoringStats=feature.monitoringStats,
    featureValue=aiplatform.gapic.FeatureValue(stringValue=NEW_VALUE)
)

# Update the feature
update_mask = aiplatform.gapic.field_mask.FieldMask(paths=["feature_value"])
update_feature_request = aiplatform.gapic.UpdateFeatureRequest(feature=new_feature, update_mask=update_mask)
client.update_feature(update_feature_request)

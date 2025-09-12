resource "google_cloudfunctions2_function" "census" {
    name    = "extract-census"
    location = var.gcp_region

    build_config {
        runtime = "python311"
        entry_point = "main"
        source {
            storage_source {
                bucket = google_storage_bucket.code_bucket.name
                object = google_storage_bucket_object.census_zip.name
            }
        }
    }

    service_config {
        available_memory = "512M"
        timeout_seconds = 300
        environment_variables = {
            GCP_PROJECT             = var.gcp_project
            BIGQUERY_DATASET_BRONZE = var.bigquery_dataset_bronze
            CENSUS_API_KEY          = var.census_api_key
            CENSUS_API_URL          = var.census_api_url
            CENSUS_API_DATASET      = var.census_api_dataset
            CONFIG_PATH             = "configs/series_config.yml"
        }
    }
}

resource "google_cloud_scheduler_job" "census" {
    name = "census-monthly"
    schedule = "0 0 1 * *"
    http_target {
        http_method = "GET"
        uri = google_cloudfunctions2_function.census.service_config[0].uri
    }
}
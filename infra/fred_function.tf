resource "google_cloudfunctions2_function" "fred" {
    name     = "extract-fred"
    location = var.gcp_region

    build_config {
        runtime = "python311"
        entry_point = "main"
        source {
            storage_source {
                bucket = google_storage_bucket.code_bucket.name
                object = google_storage_bucket_object.fred_zip.name
            }
        }
    }

    service_config {
    available_memory = "512M"
    timeout_seconds  = 300
        environment_variables = {
            GCP_PROJECT             = var.gcp_project
            BIGQUERY_DATASET_BRONZE = var.bigquery_dataset_bronze
            FRED_API_KEY            = var.fred_api_key
            FRED_API_URL            = var.fred_api_url
            CONFIG_PATH             = "configs/series_config.yml"
        }
    }
}

resource "google_cloud_scheduler_job" "fred" {
    name = "fred-monthly"
    schedule = "0 0 1 * *"
    http_target {
        http_method = "GET"
        uri = google_cloudfunctions2_function.fred.service_config[0].uri
    }
}
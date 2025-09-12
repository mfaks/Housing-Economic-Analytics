output "census_function_uri" {
  value = google_cloudfunctions2_function.census.service_config[0].uri
}

output "fred_function_uri" {
  value = google_cloudfunctions2_function.fred.service_config[0].uri
}

output "census_scheduler_name" {
  value = google_cloud_scheduler_job.census.name
}

output "fred_scheduler_name" {
  value = google_cloud_scheduler_job.fred.name
}
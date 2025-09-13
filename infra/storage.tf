resource "google_storage_bucket" "code_bucket" {
  name     = "${var.gcp_project}-function-code"
  location = var.gcp_region
}

resource "google_storage_bucket_object" "fred_zip" {
  name   = "fred.zip"
  bucket = google_storage_bucket.code_bucket.name
  source = "${path.module}/fred_function.zip"
}

resource "google_storage_bucket_object" "census_zip" {
  name   = "census.zip"
  bucket = google_storage_bucket.code_bucket.name
  source = "${path.module}/census_function.zip"
}
variable "gcp_project" {
  type = string
}

variable "gcp_region" {
  type    = string
  default = "us-central1"
}

variable "census_api_key" {}
variable "census_api_url" {}
variable "census_api_dataset" {}
variable "fred_api_key" {}
variable "fred_api_url" {}
variable "bigquery_dataset_bronze" {}
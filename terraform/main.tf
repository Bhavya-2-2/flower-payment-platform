terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "payment_api" {
  name  = "flower-payment-api-terraform"
  image = "flower-payment-api:1.0"

  ports {
    internal = 5000
    external = 5001
  }
}

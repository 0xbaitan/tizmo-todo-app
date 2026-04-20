#!/usr/bin/env bash
#
# terraform.sh - Terraform management script
# Usage: ./terraform.sh [install|uninstall|verify|upgrade]
#

set -e

DEFAULT_INSTALL_DIR="${HOME}/.local/bin"

get_latest_version() {
  VERSION=$(curl -s https://checkpoint-api.hashicorp.com/v1/beta/terraform | grep -o '"version":"[^"]*' | cut -d'"' -f4)
  echo "$VERSION"
}

install_terraform() {
  # Check if terraform is already installed
  if command -v terraform &> /dev/null; then
    CURRENT_VERSION=$(terraform version 2>/dev/null | grep -oP 'v\K[0-9.]+' || echo "unknown")
    LATEST_VERSION=$(get_latest_version)

    echo "terraform is already installed: v${CURRENT_VERSION}"
    echo "Latest version: v${LATEST_VERSION}"
    echo ""
    echo "Options:"
    echo "  [u] Upgrade to latest version"
    echo "  [r] Uninstall and do a fresh installation"
    echo "  [x] Exit"
    echo ""
    printf "Choose an option [u/r/x]: "
    read -r choice

    case "$choice" in
      u|U)
        echo "Upgrading to v${LATEST_VERSION}..."
        do_install
        return
        ;;
      r|R)
        echo "Uninstalling current version and doing fresh installation..."
        uninstall_terraform
        ;;
      x|X)
        echo "Exiting."
        exit 0
        ;;
      *)
        echo "Invalid option. Exiting."
        exit 1
        ;;
    esac
  fi

  echo "Enter install location [default: ${DEFAULT_INSTALL_DIR}]:"
  read -r INSTALL_DIR
  INSTALL_DIR="${INSTALL_DIR:-$DEFAULT_INSTALL_DIR}"

  do_install "$INSTALL_DIR"
}

do_install() {
  INSTALL_DIR="${1:-$DEFAULT_INSTALL_DIR}"

  mkdir -p "$INSTALL_DIR"

  VERSION=$(get_latest_version)
  echo "Installing terraform v${VERSION}..."

  curl -sLo "/tmp/terraform.zip" "https://releases.hashicorp.com/terraform/${VERSION}/terraform_${VERSION}_linux_amd64.zip"
  unzip -o "/tmp/terraform.zip" -d "$INSTALL_DIR"
  rm -f "/tmp/terraform.zip"

  echo "terraform v${VERSION} installed to ${INSTALL_DIR}/terraform"
}

uninstall_terraform() {
  # If terraform is not installed, exit
  if ! command -v terraform &> /dev/null; then
    echo "terraform is not installed."
    exit 0
  fi

  echo "Enter install location [default: ${DEFAULT_INSTALL_DIR}]:"
  read -r INSTALL_DIR
  INSTALL_DIR="${INSTALL_DIR:-$DEFAULT_INSTALL_DIR}"

  rm -f "${INSTALL_DIR}/terraform"
  echo "terraform uninstalled from ${INSTALL_DIR}"
}

verify_terraform() {
  if command -v terraform &> /dev/null; then
    terraform version
  else
    echo "terraform not found in PATH"
    exit 1
  fi
}

upgrade_terraform() {
  if ! command -v terraform &> /dev/null; then
    echo "terraform is not installed. Use 'install' command instead."
    exit 1
  fi

  CURRENT_VERSION=$(terraform version 2>/dev/null | grep -oP 'v\K[0-9.]+' || echo "unknown")
  LATEST_VERSION=$(get_latest_version)

  echo "Current version: ${CURRENT_VERSION}"
  echo "Latest version: ${LATEST_VERSION}"

  if [ "$CURRENT_VERSION" = "$LATEST_VERSION" ]; then
    echo "Already on latest version"
    exit 0
  fi

  echo "Upgrading to terraform v${LATEST_VERSION}..."
  do_install
}

case "$1" in
  install) install_terraform ;;
  uninstall) uninstall_terraform ;;
  verify) verify_terraform ;;
  upgrade) upgrade_terraform ;;
  *) echo "Usage: $0 {install|uninstall|verify|upgrade}" ;;
esac

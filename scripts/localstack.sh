#!/bin/bash

set -e

ENV_FILE_PATH="aws/environments/development/.env"
COMPOSE_FILE="aws/environments/development/docker-compose.yml"

# -----------------------------------------------------------------------------
# Usage
# -----------------------------------------------------------------------------

usage() {
  echo "Usage: $0 <command> [-- args]"
  echo ""
  echo "Commands:"
  echo "  start    Start LocalStack"
  echo "  stop     Stop LocalStack"
  echo ""
  echo "Examples:"
  echo "  $0 start"
  echo "  $0 start -- --build"
  echo "  $0 stop"
  exit 1
}

# -----------------------------------------------------------------------------
# Sub Commands
# -----------------------------------------------------------------------------

start() {
  docker compose -f "$COMPOSE_FILE" up -d "$@"
}

stop() {
  docker compose -f "$COMPOSE_FILE" down "$@"
}



# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

main() {
  if [ $# -lt 1 ]; then
    usage
  fi

  local command="$1"
  shift

  case "$command" in
    start)
      start "$@"
      ;;
    stop)
      stop "$@"
      ;;
    *)
      usage
      ;;
  esac
}


# -----------------------------------------------------------------------------
# Load environment variables from .env file
# -----------------------------------------------------------------------------
if [ -f "$ENV_FILE_PATH" ]; then
  set -o allexport
  source "$ENV_FILE_PATH"
  set +o allexport
else
  echo "Warning: .env file not found at $ENV_FILE_PATH. Using default environment variables."
fi

main "$@"